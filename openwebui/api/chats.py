import logging
from typing import List, Any, Optional

import httpx

from ..exceptions import APIError, AuthenticationError, ConnectionError, NotFoundError
from ..open_web_ui_client.open_web_ui_client import AuthenticatedClient, models
from ..open_web_ui_client.open_web_ui_client.types import Response, UNSET

# Import functions from the generated low-level client
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

log = logging.getLogger(__name__)


class ChatsAPI:
    """Provides high-level async methods for interacting with the Chats API."""

    def __init__(self, client: AuthenticatedClient):
        self._client = client

    def _handle_response(self, response: Response) -> Any:
        """A centralized way to handle API responses and errors."""
        log.debug(f"Received API response with status code: {response.status_code}")
        if 200 <= response.status_code < 300:
            log.debug("Request successful, returning parsed response.")
            return response.parsed

        # Check for specific, known error types first
        if response.status_code == 401:
            log.error("Authentication failed (401). Check your API key.")
            raise AuthenticationError("Invalid or missing API key.")
        if response.status_code == 404:
            log.warning(f"Resource not found (404) at {getattr(response, 'url', 'unknown URL')}.")
            raise NotFoundError("The requested resource was not found.")

        # Fallback for other HTTP errors
        log.error(f"API Error {response.status_code}: {response.text}")
        raise APIError(
            message=f"Received unexpected status code: {response.status_code}",
            status_code=response.status_code,
        )

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

            completion_data = self._handle_response(completion_response)
            assistant_content = completion_data["choices"][0]["message"]["content"]
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

            new_chat = self._handle_response(create_response)
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

            model = chat_details.chat.additional_properties.get("models")[0]
            messages = chat_details.chat.additional_properties.get("messages", [])
            messages.append({"role": "user", "content": prompt})

            log.debug(f"Step 2/3: Sending continued prompt to model '{model}'.")
            completion_payload = models.GenerateChatCompletionOpenaiChatCompletionsPostFormData()
            completion_payload.additional_properties = {"model": model, "messages": messages, "stream": False}

            completion_response = (
                await generate_chat_completion_openai_chat_completions_post.asyncio_detailed(
                    client=self._client, body=completion_payload
                )
            )
            completion_data = self._handle_response(completion_response)
            assistant_response = completion_data["choices"][0]["message"]["content"]

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

            updated_chat = self._handle_response(update_response)
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
            response = await get_session_user_chat_list_api_v1_chats_list_get.asyncio_detailed(
                client=self._client
            )
            return self._handle_response(response)
        except httpx.ConnectError as e:
            raise ConnectionError(f"A network error occurred: {e}") from e

    async def get(self, chat_id: str) -> models.ChatResponse:
        """
        Fetches the full details and message history of a specific chat.
        """
        log.info(f"Getting details for chat_id: {chat_id}")
        try:
            response = await get_chat_by_id_api_v1_chats_id_get.asyncio_detailed(
                id=chat_id, client=self._client
            )
            return self._handle_response(response)
        except httpx.ConnectError as e:
            raise ConnectionError(f"A network error occurred: {e}") from e

    async def delete(self, chat_id: str) -> bool:
        """
        Deletes a chat by its ID.
        """
        log.info(f"Deleting chat with ID: {chat_id}")
        try:
            response = await delete_chat_by_id_api_v1_chats_id_delete.asyncio_detailed(
                id=chat_id, client=self._client
            )
            # The API might not return a parsed value, just 200 OK.
            # Handle cases where response.parsed might be None.
            return True if response.status_code == 200 else self._handle_response(response)
        except httpx.ConnectError as e:
            raise ConnectionError(f"A network error occurred: {e}") from e

    async def rename(self, chat_id: str, new_title: str) -> models.ChatResponse:
        """
        Renames (updates the title of) an existing chat.
        """
        log.info(f"Renaming chat '{chat_id}' to '{new_title}'.")
        try:
            # Step 1: Get the existing chat details (full object for update)
            log.debug(f"Fetching chat details for renaming: {chat_id}")
            chat_details = await self.get(chat_id)  # Reuse existing get method

            # Step 2: Update only the title
            chat_details.title = new_title

            # Step 3: Reconstruct the ChatForm body for the update API call
            # The update endpoint expects a ChatForm object. We need to create it
            # from the modified ChatResponse details.

            # The chat content itself is within chat_details.chat.additional_properties
            chat_data_payload = models.ChatFormChat()
            chat_data_payload.additional_properties = chat_details.chat.additional_properties

            update_payload = models.ChatForm(
                chat=chat_data_payload,
                # Properly pass folder_id, accounting for UNSET
                folder_id=chat_details.folder_id if chat_details.folder_id is not UNSET else UNSET,
            )

            log.debug(f"Sending update request for chat: {chat_id}")
            response = await update_chat_by_id_api_v1_chats_id_post.asyncio_detailed(
                id=chat_id, client=self._client, body=update_payload
            )

            updated_chat = self._handle_response(response)
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

            folder_details = self._handle_response(folder_response)

            # FIX: Check if folder_details.items is None before accessing .chats
            # If items is None, there are no chats in the folder.
            chats_in_folder = (
                folder_details.items.chats if folder_details.items and folder_details.items.chats else []
            )

            log.info(f"Found {len(chats_in_folder)} chats in folder '{folder_id}'.")
            return chats_in_folder

        except httpx.ConnectError as e:
            raise ConnectionError(f"A network error occurred: {e}") from e
