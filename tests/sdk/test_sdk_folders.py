import pytest
from unittest.mock import MagicMock

from openwebui.exceptions import AuthenticationError, NotFoundError
from openwebui.open_web_ui_client.open_web_ui_client import models
from openwebui.open_web_ui_client.open_web_ui_client.types import Response

# Mark all tests in this file as async
pytestmark = pytest.mark.asyncio


async def test_folders_list_success(mocker, sdk_client):
    """Test successful folder listing."""
    # Mock the generated client's function
    mock_api_func = mocker.patch("openwebui.api.folders.get_folders.asyncio_detailed")

    # Simulate a successful API response
    mock_folder_list = [
        models.FolderModel(id="1", name="Test Folder", user_id="test_user", created_at=0, updated_at=0)
    ]
    mock_response = MagicMock(spec=Response)
    mock_response.status_code = 200
    mock_response.parsed = mock_folder_list
    mock_api_func.return_value = mock_response

    # Call the SDK method
    folders = await sdk_client.folders.list()

    # Assertions
    assert len(folders) == 1
    assert folders[0].name == "Test Folder"
    mock_api_func.assert_called_once()


async def test_folders_list_auth_error(mocker, sdk_client):
    """Test folder listing with an authentication error."""
    mock_api_func = mocker.patch("openwebui.api.folders.get_folders.asyncio_detailed")

    # Simulate a 401 Unauthorized response
    mock_response = MagicMock(spec=Response)
    mock_response.status_code = 401
    mock_api_func.return_value = mock_response

    with pytest.raises(AuthenticationError):
        await sdk_client.folders.list()


async def test_folder_create_success(mocker, sdk_client):
    """Test successful folder creation."""
    mock_api_func = mocker.patch("openwebui.api.folders.create_folder.asyncio_detailed")

    mock_folder = models.FolderModel(
        id="new-folder", name="New Folder", user_id="test_user", created_at=0, updated_at=0
    )
    mock_response = MagicMock(spec=Response)
    mock_response.status_code = 200
    mock_response.parsed = mock_folder
    mock_api_func.return_value = mock_response

    new_folder = await sdk_client.folders.create(name="New Folder")

    assert new_folder.id == "new-folder"
    mock_api_func.assert_called_once()
    # Check that it was called with the correct body
    call_args = mock_api_func.call_args[1]
    assert isinstance(call_args["body"], models.FolderForm)
    assert call_args["body"].name == "New Folder"


async def test_folder_delete_success(mocker, sdk_client):
    """Test successful folder deletion."""
    mock_api_func = mocker.patch("openwebui.api.folders.delete_folder_by_id.asyncio_detailed")

    mock_response = MagicMock(spec=Response)
    mock_response.status_code = 200
    mock_response.parsed = True
    mock_api_func.return_value = mock_response

    success = await sdk_client.folders.delete(folder_id="folder-to-delete")

    assert success is True
    mock_api_func.assert_called_once_with(id="folder-to-delete", client=sdk_client._client)


async def test_folder_delete_not_found(mocker, sdk_client):
    """Test deleting a folder that does not exist."""
    mock_api_func = mocker.patch("openwebui.api.folders.delete_folder_by_id.asyncio_detailed")

    mock_response = MagicMock(spec=Response)
    mock_response.status_code = 404
    mock_api_func.return_value = mock_response

    with pytest.raises(NotFoundError):
        await sdk_client.folders.delete(folder_id="non-existent-folder")
