import logging
from typing import List

import httpx

from ..exceptions import ConnectionError
from ..utils.api_utils import handle_api_response  # NEW IMPORT for centralized handler

# Import the generated client, models, and specific api functions
from ..open_web_ui_client.open_web_ui_client import AuthenticatedClient, models
from ..open_web_ui_client.open_web_ui_client.api.folders import (
    get_folders_api_v1_folders_get as get_folders,
    create_folder_api_v1_folders_post as create_folder,
    delete_folder_by_id_api_v1_folders_id_delete as delete_folder_by_id,
)


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
            return handle_api_response(response, "folder list")
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
            return handle_api_response(response, "folder creation")
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
            # handle_api_response will return True for successful deletes (e.g. 200 OK with no body)
            return handle_api_response(response, f"folder deletion for ID {folder_id}")
        except httpx.ConnectError as e:
            raise ConnectionError(f"A network error occurred: {e}") from e
