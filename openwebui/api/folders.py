import httpx
import logging
from typing import List, Any

from ..exceptions import APIError, AuthenticationError, ConnectionError, NotFoundError

# Import the generated client, models, and specific api functions
from ..open_web_ui_client.open_web_ui_client import AuthenticatedClient, models
from ..open_web_ui_client.open_web_ui_client.api.folders import (
    get_folders_api_v1_folders_get as get_folders,
    create_folder_api_v1_folders_post as create_folder,
    delete_folder_by_id_api_v1_folders_id_delete as delete_folder_by_id,
)
from ..open_web_ui_client.open_web_ui_client.types import Response

log = logging.getLogger(__name__)


class FoldersAPI:
    """Provides high-level async methods for interacting with the Folders API."""

    def __init__(self, client: AuthenticatedClient):
        self._client = client

    async def list(self) -> List[models.FolderModel]:
        """
        Retrieves a list of all folders for the authenticated user.

        Returns:
            A list of FolderModel objects.
        """
        try:
            log.info("Listing all folders.")
            response = await get_folders.asyncio_detailed(client=self._client)
            return self._handle_response(response)
        except httpx.ConnectError as e:
            raise ConnectionError(f"A network error occurred: {e}") from e

    async def create(self, name: str) -> models.FolderModel:
        """
        Creates a new folder.

        Args:
            name: The name for the new folder.

        Returns:
            The newly created FolderModel object.
        """
        try:
            log.info(f"Creating new folder with name: '{name}'")
            form_data = models.FolderForm(name=name)
            response = await create_folder.asyncio_detailed(client=self._client, body=form_data)
            return self._handle_response(response)
        except httpx.ConnectError as e:
            raise ConnectionError(f"A network error occurred: {e}") from e

    async def delete(self, folder_id: str) -> bool:
        """
        Deletes a folder by its ID.

        Args:
            folder_id: The ID of the folder to delete.

        Returns:
            True if the deletion was successful.
        """
        try:
            log.info(f"Deleting folder with ID: {folder_id}")
            response = await delete_folder_by_id.asyncio_detailed(id=folder_id, client=self._client)
            return self._handle_response(response)
        except httpx.ConnectError as e:
            raise ConnectionError(f"A network error occurred: {e}") from e

    def _handle_response(self, response: Response) -> Any:
        """A centralized way to handle API responses and errors."""
        log.debug(f"Received API response: {response.status_code}")
        if 200 <= response.status_code < 300:
            log.debug("Request successful.")
            return response.parsed

        if response.status_code == 401:
            log.error("Authentication failed. Check your API key.")
            raise AuthenticationError("Invalid or missing API key.")
        if response.status_code == 404:
            log.warning("Resource not found.")
            raise NotFoundError("The requested resource was not found.")

        log.error(f"API Error {response.status_code}: {response}")
        raise APIError(
            message=f"Received unexpected status code: {response.status_code}",
            status_code=response.status_code,
        )
