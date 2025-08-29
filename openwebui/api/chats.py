import logging
from typing import List, Optional

import httpx

from ..exceptions import ConnectionError
from ..utils.api_utils import handle_api_response  # NEW IMPORT for centralized handler

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
from ..open_web_ui_client.open_web_ui_client.types import UNSET  # Still needed for function signature


log = logging.getLogger(__name__)


class ChatsAPI:
    """Provides high-level async methods for interacting with the Chats API."""

    def __init__(self, client: AuthenticatedClient):
        self._client = client

    async def create(self, model: str, prompt: str, folder_id: Optional[str] = None) -> models.ChatResponse:
        """Creates a new chat session by first getting an LLM response and then saving the full conversation."""
        log.info(f"Creating new chat with model '{model}'.")
        try:
            log.debug("Step 1/2: Getting LLM completion.")
            completion_payload = models.GenerateChatCompletionOpenaiChatCompletionsPostFormData()
            completion_payload.additional_properties = {
                "model": model,
                "messages": [{"role": "user", "content": prompt}],
                "stream": False,
            }

            completion_response = (
                await generate_chat_completion_openai_chat_completions_post.asyncio_detailed(
                    client=self._client, body=completion_payload
                )
            )
            # Use the centralized handler
            completion_data = handle_api_response(completion_response, "LLM completion")
            assistant_content = completion_data["choices"][0]["message"][
                "content"
            ]  # Assuming completion_data is a dict here
            log.debug("LLM completion received successfully.")

            # Step 2: Create the chat session with the full conversation
            log.debug("Step 2/2: Saving full conversation to a new chat session.")
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
            # Use the centralized handler
            new_chat = handle_api_response(create_response, "chat creation")
            log.info(f"Successfully created new chat with ID: {new_chat.id}")
            return new_chat

        except httpx.ConnectError as e:
            raise ConnectionError(f"A network error occurred: {e}") from e

    async def continue_chat(self, chat_id: str, prompt: str) -> models.ChatResponse:
        """Adds a new message to an existing chat and gets a response from the LLM."""
        log.info(f"Continuing chat with ID: {chat_id}")
        try:
            log.debug(f"Step 1/3: Fetching history for chat_id='{chat_id}'.")
            chat_details = await self.get(chat_id)  # Reuse existing get method

            model = chat_details.chat.additional_properties.get("models")[
                0
            ]  # Assumes chat_details is models.ChatResponse
            messages = chat_details.chat.additional_properties.get(
                "messages", []
            )  # Assumes chat_details is models.ChatResponse
            messages.append({"role": "user", "content": prompt})

            log.debug(f"Step 2/3: Sending continued prompt to model '{model}'.")
            completion_payload = models.GenerateChatCompletionOpenaiChatCompletionsPostFormData()
            completion_payload.additional_properties = {"model": model, "messages": messages, "stream": False}

            completion_response = (
                await generate_chat_completion_openai_chat_completions_post.asyncio_detailed(
                    client=self._client, body=completion_payload
                )
            )
            # Use the centralized handler
            completion_data = handle_api_response(completion_response, "LLM completion for continue chat")
            assistant_response = completion_data["choices"][0]["message"][
                "content"
            ]  # Assuming completion_data is a dict here

            log.debug(f"Step 3/3: Appending assistant's response and updating chat '{chat_id}' on server.")
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

            # Use the centralized handler
            updated_chat = handle_api_response(update_response, "chat update")
            log.info(f"Successfully updated chat with ID: {chat_id}")
            return updated_chat

        except httpx.ConnectError as e:
            raise ConnectionError(f"A network error occurred: {e}") from e

    async def list(self) -> List[models.ChatTitleIdResponse]:
        """
        Retrieves a list of all chat titles and IDs for the authenticated user.
        Returns:
            A list of ChatTitleIdResponse objects.
        """
        log.info("Listing all chats for the user.")
        try:
            response = await get_session_user_chat_list_api_v1_chats_list_get.asyncio_detailed(
                client=self._client
            )
            # Use the centralized handler
            return handle_api_response(response, "chat list")
        except httpx.ConnectError as e:
            raise ConnectionError(f"A network error occurred: {e}") from e

    async def get(self, chat_id: str) -> models.ChatResponse:
        """
        Fetches the full details and message history of a specific chat.
        Returns:
            A ChatResponse object containing chat details.
        """
        log.info(f"Getting details for chat_id: {chat_id}")
        try:
            response = await get_chat_by_id_api_v1_chats_id_get.asyncio_detailed(
                id=chat_id, client=self._client
            )
            # Use the centralized handler
            return handle_api_response(response, f"chat details for ID {chat_id}")
        except httpx.ConnectError as e:
            raise ConnectionError(f"A network error occurred: {e}") from e

    async def delete(self, chat_id: str) -> bool:
        """
        Deletes a chat by its ID.
        Returns:
            True if the deletion was successful.
        """
        log.info(f"Deleting chat with ID: {chat_id}")
        try:
            response = await delete_chat_by_id_api_v1_chats_id_delete.asyncio_detailed(
                id=chat_id, client=self._client
            )
            # handle_api_response will return True for successful deletes
            return handle_api_response(response, f"chat deletion for ID {chat_id}")
        except httpx.ConnectError as e:
            raise ConnectionError(f"A network error occurred: {e}") from e

    async def rename(self, chat_id: str, new_title: str) -> models.ChatResponse:
        """
        Renames (updates the title of) an existing chat.
        Returns:
            A ChatResponse object representing the updated chat.
        """
        log.info(f"Renaming chat '{chat_id}' to '{new_title}'.")
        try:
            # Step 1: Get the existing chat details (full object for update)
            log.debug(f"Fetching chat details for renaming: {chat_id}")
            chat_details = await self.get(chat_id)  # Reuse existing get method

            # Step 2: Update only the title
            chat_details.title = new_title

            # Step 3: Reconstruct the ChatForm body for the update API call
            # The chat content itself is within chat_details.chat.additional_properties
            chat_data_payload = models.ChatFormChat()
            chat_data_payload.additional_properties = chat_details.chat.additional_properties

            update_payload = models.ChatForm(
                chat=chat_data_payload,
                folder_id=chat_details.folder_id if chat_details.folder_id is not UNSET else UNSET,
            )

            log.debug(f"Sending update request for chat: {chat_id}")
            response = await update_chat_by_id_api_v1_chats_id_post.asyncio_detailed(
                id=chat_id, client=self._client, body=update_payload
            )

            # Use the centralized handler
            updated_chat = handle_api_response(response, "chat rename")
            log.info(f"Successfully renamed chat '{chat_id}' to '{updated_chat.title}'.")
            return updated_chat

        except httpx.ConnectError as e:
            raise ConnectionError(f"A network error occurred: {e}") from e

    async def list_by_folder(self, folder_id: str) -> List[models.ChatTitleIdResponse]:
        """
        Lists all chat IDs and titles within a specific folder.

        Notes:
        The Open WebUI API documentation suggests that `GET /api/v1/folders/{id}`
        returns a `FolderModel` which contains an `items` field.
        This `items` field may contain chats.

        This method retrieves folder details and extracts chats from its `items` property.

        Args:
            folder_id (str): The ID of the folder to list chats from.

        Returns:
            List[models.ChatTitleIdResponse]: A list of chat title and ID objects.

        Raises:
            NotFoundError: If the folder with the given ID does not exist.
            AuthenticationError, APIError, ConnectionError
        """
        log.info(f"Listing chats for folder_id: {folder_id}")
        try:
            # Use the generated folders client to get folder details
            log.debug(f"Fetching folder details for ID: {folder_id} to list its chats.")

            folder_response = await get_folder_by_id_api_v1_folders_id_get.asyncio_detailed(
                id=folder_id, client=self._client
            )
            # Use the centralized handler
            folder_details = handle_api_response(folder_response, f"folder details for {folder_id}")

            # FIX: Check if folder_details.items is None before accessing .chats
            # If items is None, there are no chats in the folder.
            chats_in_folder = (
                folder_details.items.chats if folder_details.items and folder_details.items.chats else []
            )

            log.info(f"Found {len(chats_in_folder)} chats in folder '{folder_id}'.")
            return chats_in_folder

        except httpx.ConnectError as e:
            raise ConnectionError(f"A network error occurred: {e}") from e
