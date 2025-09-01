import logging
from typing import List, Optional, Any

import httpx

# Import the new KnowledgeBaseAPI to perform RAG queries
from .knowledge import KnowledgeBaseAPI
from ..exceptions import APIError, AuthenticationError, ConnectionError, NotFoundError
from ..utils.api_utils import handle_api_response

# Import the generated client, models, and specific api functions
from ..open_web_ui_client.open_web_ui_client import AuthenticatedClient, models
from ..open_web_ui_client.open_web_ui_client.api.chats import (
    create_new_chat_api_v1_chats_new_post,
    get_session_user_chat_list_api_v1_chats_list_get,
    get_chat_by_id_api_v1_chats_id_get,
    update_chat_by_id_api_v1_chats_id_post,
    delete_chat_by_id_api_v1_chats_id_delete,
)
from ..open_web_ui_client.open_web_ui_client.api.openai import (
    generate_chat_completion_openai_chat_completions_post,
)
from ..open_web_ui_client.open_web_ui_client.api.folders import get_folder_by_id_api_v1_folders_id_get
from ..open_web_ui_client.open_web_ui_client.types import UNSET

log = logging.getLogger(__name__)


class ChatsAPI:
    """Provides high-level async methods for interacting with the Chats API."""

    def __init__(self, client: AuthenticatedClient):
        self._client = client
        # Instantiate KnowledgeBaseAPI to be used for RAG operations
        self.knowledge = KnowledgeBaseAPI(client)

    async def create(
            self,
            model: str,
            prompt: str,
            folder_id: Optional[str] = None,
            kb_ids: Optional[List[str]] = None,
            k: Optional[int] = None,
            k_reranker: Optional[int] = None,
            r: Optional[float] = None,
            hybrid: Optional[bool] = None,
            hybrid_bm25_weight: Optional[float] = None,
    ) -> models.ChatResponse:
        """
        Creates a new chat session. If kb_ids are provided, it performs a RAG query
        to augment the prompt with context from the knowledge base(s).
        """
        log.info(f"Creating new chat with model '{model}'.")

        final_prompt = prompt

        # --- RAG WORKFLOW ADDITION ---
        if kb_ids:
            print(kb_ids)
            log.info(f"RAG workflow activated. Querying KBs {kb_ids} for context.")
            try:
                retrieved_chunks = await self.knowledge.query(
                    prompt,
                    kb_ids,
                    k=k,
                    k_reranker=k_reranker,
                    r=r,
                    hybrid=hybrid,
                    hybrid_bm25_weight=hybrid_bm25_weight
                )
                if retrieved_chunks:
                    # Combine the retrieved chunks into a single context string.
                    # This assumes each chunk is a dict with a 'content' field.
                    retrieved_context = "\n\n---\n\n".join(
                        [chunk.get("content", "") for chunk in retrieved_chunks if isinstance(chunk, dict)])

                    if retrieved_context:  # Ensure there's actually content before augmenting
                        final_prompt = (
                            f"Please use the following context to answer the question.\n\n"
                            f"--- Context ---\n{retrieved_context}\n\n"
                            f"--- Question ---\n{prompt}"
                        )
                        log.debug("Prompt augmented with retrieved context from KB(s).")
                    else:
                        log.warning(f"Retrieved chunks from KB(s) {kb_ids} had no usable content.")
                else:
                    log.warning(f"No chunks retrieved from KB(s) {kb_ids} for the prompt.")
            except Exception as e:
                log.error(f"Failed to query knowledge base(s) {kb_ids}. Proceeding without RAG. Error: {e}")
        # --- END RAG WORKFLOW ---

        try:
            log.debug("Step 1/2: Getting LLM completion.")
            completion_payload = models.GenerateChatCompletionOpenaiChatCompletionsPostFormData()
            completion_payload.additional_properties = {
                "model": model,
                "messages": [{"role": "user", "content": final_prompt}],
                "stream": False,
            }

            completion_response = await generate_chat_completion_openai_chat_completions_post.asyncio_detailed(
                client=self._client, body=completion_payload
            )
            completion_data = handle_api_response(completion_response, "LLM completion")
            assistant_content = completion_data["choices"][0]["message"]["content"]
            log.debug("LLM completion received successfully.")

            log.debug("Step 2/2: Saving full conversation to a new chat session.")
            # Important: Store the original prompt in the chat history, not the augmented one.
            full_messages = [
                {"role": "user", "content": prompt},
                {"role": "assistant", "content": assistant_content},
            ]
            chat_data = models.ChatFormChat()
            chat_data.additional_properties = {"models": [model], "messages": full_messages}
            create_payload = models.ChatForm(chat=chat_data, folder_id=folder_id or UNSET)

            create_response = await create_new_chat_api_v1_chats_new_post.asyncio_detailed(
                client=self._client, body=create_payload
            )
            new_chat = handle_api_response(create_response, "chat creation")
            log.info(f"Successfully created new chat with ID: {new_chat.id}")
            return new_chat

        except httpx.ConnectError as e:
            raise ConnectionError(f"A network error occurred: {e}") from e

    async def continue_chat(
            self,
            chat_id: str,
            prompt: str,
            kb_ids: Optional[List[str]] = None,
            k: Optional[int] = None,
            k_reranker: Optional[int] = None,
            r: Optional[float] = None,
            hybrid: Optional[bool] = None,
            hybrid_bm25_weight: Optional[float] = None,
    ) -> models.ChatResponse:
        """
        Adds a new message to an existing chat. If kb_ids are provided, it performs a RAG query
        to augment the prompt with context from the knowledge base(s).
        """
        log.info(f"Continuing chat with ID: {chat_id}")

        final_prompt = prompt

        # --- RAG WORKFLOW ADDITION ---
        if kb_ids:
            log.info(f"RAG workflow activated for continuation. Querying KBs {kb_ids} for context.")
            try:
                retrieved_chunks = await self.knowledge.query(
                    prompt,
                    kb_ids,
                    k=k,
                    k_reranker=k_reranker,
                    r=r,
                    hybrid=hybrid,
                    hybrid_bm25_weight=hybrid_bm25_weight
                )
                if retrieved_chunks:
                    retrieved_context = "\n\n---\n\n".join(
                        [chunk.get("content", "") for chunk in retrieved_chunks if isinstance(chunk, dict)])
                    if retrieved_context:
                        final_prompt = (
                            f"Please use the following context to answer the question.\n\n"
                            f"--- Context ---\n{retrieved_context}\n\n"
                            f"--- Question ---\n{prompt}"
                        )
                        log.debug("Follow-up prompt augmented with retrieved context.")
                    else:
                        log.warning(f"Retrieved chunks from KB(s) {kb_ids} had no usable content for follow-up.")
                else:
                    log.warning(f"No chunks retrieved from KB(s) {kb_ids} for the follow-up prompt.")
            except Exception as e:
                log.error(f"Failed to query knowledge base(s) {kb_ids}. Proceeding without RAG. Error: {e}")
        # --- END RAG WORKFLOW ---

        try:
            log.debug(f"Step 1/3: Fetching history for chat_id='{chat_id}'.")
            chat_details = await self.get(chat_id)

            model = chat_details.chat.additional_properties.get("models")[0]
            messages = chat_details.chat.additional_properties.get("messages", [])
            messages.append({"role": "user", "content": final_prompt})

            log.debug(f"Step 2/3: Sending continued prompt to model '{model}'.")
            completion_payload = models.GenerateChatCompletionOpenaiChatCompletionsPostFormData()
            completion_payload.additional_properties = {"model": model, "messages": messages, "stream": False}

            completion_response = await generate_chat_completion_openai_chat_completions_post.asyncio_detailed(
                client=self._client, body=completion_payload
            )
            completion_data = handle_api_response(completion_response, "LLM completion for continue chat")
            assistant_response = completion_data["choices"][0]["message"]["content"]

            log.debug(f"Step 3/3: Appending assistant's response and updating chat '{chat_id}' on server.")
            # Important: Replace the augmented prompt with the original for a clean history
            messages[-1] = {"role": "user", "content": prompt}
            messages.append({"role": "assistant", "content": assistant_response})

            updated_chat_data = models.ChatFormChat()
            updated_chat_data.additional_properties = chat_details.chat.additional_properties
            updated_chat_data.additional_properties["messages"] = messages

            update_payload = models.ChatForm(
                chat=updated_chat_data,
                folder_id=chat_details.folder_id if chat_details.folder_id is not UNSET else UNSET,
            )

            update_response = await update_chat_by_id_api_v1_chats_id_post.asyncio_detailed(
                id=chat_id, client=self._client, body=update_payload
            )

            updated_chat = handle_api_response(update_response, "chat update")
            log.info(f"Successfully updated chat with ID: {chat_id}")
            return updated_chat

        except httpx.ConnectError as e:
            raise ConnectionError(f"A network error occurred: {e}") from e
    async def list(self) -> List[models.ChatTitleIdResponse]:
        """
        Retrieves a list of all chat titles and IDs for the authenticated user.
        """
        log.info("Listing all chats for the user.")
        try:
            response = await get_session_user_chat_list_api_v1_chats_list_get.asyncio_detailed(client=self._client)
            return handle_api_response(response, "chat list")
        except httpx.ConnectError as e:
            raise ConnectionError(f"A network error occurred: {e}") from e

    async def get(self, chat_id: str) -> models.ChatResponse:
        """
        Fetches the full details and message history of a specific chat.
        """
        log.info(f"Getting details for chat_id: {chat_id}")
        try:
            response = await get_chat_by_id_api_v1_chats_id_get.asyncio_detailed(id=chat_id, client=self._client)
            return handle_api_response(response, f"chat details for ID {chat_id}")
        except httpx.ConnectError as e:
            raise ConnectionError(f"A network error occurred: {e}") from e

    async def delete(self, chat_id: str) -> bool:
        """Deletes a chat by its ID."""
        log.info(f"Deleting chat with ID: {chat_id}")
        try:
            response = await delete_chat_by_id_api_v1_chats_id_delete.asyncio_detailed(id=chat_id, client=self._client)
            return handle_api_response(response, f"chat deletion for ID {chat_id}")
        except httpx.ConnectError as e:
            raise ConnectionError(f"A network error occurred: {e}") from e

    async def rename(self, chat_id: str, new_title: str) -> models.ChatResponse:
        """Renames (updates the title of) an existing chat."""
        log.info(f"Renaming chat '{chat_id}' to '{new_title}'.")
        try:
            chat_details = await self.get(chat_id)
            chat_details.title = new_title

            chat_data_payload = models.ChatFormChat()
            chat_data_payload.additional_properties = chat_details.chat.additional_properties

            update_payload = models.ChatForm(
                chat=chat_data_payload,
                folder_id=chat_details.folder_id if chat_details.folder_id is not UNSET else UNSET,
            )

            response = await update_chat_by_id_api_v1_chats_id_post.asyncio_detailed(
                id=chat_id, client=self._client, body=update_payload
            )

            updated_chat = handle_api_response(response, "chat rename")
            log.info(f"Successfully renamed chat '{chat_id}' to '{updated_chat.title}'.")
            return updated_chat
        except httpx.ConnectError as e:
            raise ConnectionError(f"A network error occurred: {e}") from e

    async def list_by_folder(self, folder_id: str) -> List[models.ChatTitleIdResponse]:
        """Lists all chat IDs and titles within a specific folder."""
        log.info(f"Listing chats for folder_id: {folder_id}")
        try:
            folder_response = await get_folder_by_id_api_v1_folders_id_get.asyncio_detailed(id=folder_id,
                                                                                            client=self._client)
            folder_details = handle_api_response(folder_response, f"folder details for {folder_id}")

            chats_in_folder = folder_details.items.chats if folder_details.items and folder_details.items.chats else []
            log.info(f"Found {len(chats_in_folder)} chats in folder '{folder_id}'.")
            return chats_in_folder
        except httpx.ConnectError as e:
            raise ConnectionError(f"A network error occurred: {e}") from e