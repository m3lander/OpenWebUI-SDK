import os
import pytest
from unittest.mock import MagicMock, AsyncMock
from click.testing import CliRunner
from dotenv import load_dotenv
from openwebui.client import OpenWebUI
from openwebui.exceptions import OpenWebUIError, NotFoundError
from datetime import datetime
import asyncio  # Make sure asyncio is imported at the top

from openwebui.open_web_ui_client.open_web_ui_client import models

# Load the main .env file to get the default URL
load_dotenv()
DEFAULT_SERVER_URL = os.getenv("OPENWEBUI_URL")

# Explicitly load the pytest_asyncio plugin for session scope fixtures
pytest_plugins = ["pytest_asyncio"]


def pytest_addoption(parser):
    """Adds a custom command-line option to pytest."""
    parser.addoption(
        "--server-url",
        action="store",
        default=None,
        help="Specify the base URL for the API server to test against.",
    )


@pytest.fixture(scope="session")
def server_url(request):
    """
    Provides the server URL for tests, using a hierarchy of configurations.
    Strips any trailing slashes to prevent double-slash issues.
    """
    url = request.config.getoption("--server-url")
    if url:
        return url.rstrip("/")

    url_from_env = os.getenv("TEST_SERVER_URL")
    if url_from_env:
        return url_from_env.rstrip("/")

    if DEFAULT_SERVER_URL:
        return DEFAULT_SERVER_URL.rstrip("/")

    pytest.fail("Server URL not configured. Use --server-url, TEST_SERVER_URL, or OPENWEBUI_URL in .env.")


@pytest.fixture
def runner():
    """Provides a Click test runner instance for CLI tests."""
    return CliRunner()


# For SDK unit tests, we provide a real client but mock out the underlying HTTP calls.
@pytest.fixture
def sdk_client():
    """Provides an instance of the OpenWebUI SDK client for testing."""
    # FIX: Change server_url to base_url, as required by OpenWebUI.__init__
    return OpenWebUI(api_key="test_api_key", base_url="http://localhost:8080")


# For CLI unit tests, we mock out the OpenWebUI client entirely.
@pytest.fixture
def mock_sdk_client(mocker):
    """
    Mocks the OpenWebUI high-level SDK client.

    This fixture patches `openwebui.cli.main.OpenWebUI`
    so that CLI commands interact with an easily controllable mock.
    """
    # Create mocks for the high-level API modules (FoldersAPI, ChatsAPI)
    # Assign AsyncMock directly to the methods that are awaitable.
    mock_folders_api = MagicMock()
    mock_folders_api.create = AsyncMock()
    mock_folders_api.list = AsyncMock()
    mock_folders_api.delete = AsyncMock()

    mock_chats_api = MagicMock()
    mock_chats_api.create = AsyncMock()
    mock_chats_api.continue_chat = AsyncMock()
    mock_chats_api.list = AsyncMock()  # This is the SDK's list all chats, not list messages
    mock_chats_api.get = AsyncMock()  # This is the SDK's get chat details
    mock_chats_api.rename = AsyncMock()
    mock_chats_api.delete = AsyncMock()
    mock_chats_api.list_by_folder = AsyncMock()

    # --- FIX: Add mock for the KnowledgeBaseAPI ---
    mock_knowledge_api = MagicMock()
    mock_knowledge_api.create = AsyncMock()
    mock_knowledge_api.list_all = AsyncMock()
    mock_knowledge_api.list_files = AsyncMock()
    mock_knowledge_api.upload_file = AsyncMock()
    mock_knowledge_api.upload_directory = AsyncMock()
    mock_knowledge_api.update_file = AsyncMock()
    mock_knowledge_api.delete_file = AsyncMock()
    mock_knowledge_api.delete_all_files_from_kb = AsyncMock()

    # Create the main sdk client mock instance
    mock_client_instance = MagicMock()
    mock_client_instance.folders = mock_folders_api
    mock_client_instance.chats = mock_chats_api
    mock_client_instance.knowledge = mock_knowledge_api  # <-- Assign the new mock

    # Patch the __init__ of the OpenWebUI class used within the CLI module
    # to return our mock instance. This means OpenWebUI() in CLI code
    # will yield mock_client_instance.
    mocker.patch("openwebui.cli.main.OpenWebUI", return_value=mock_client_instance)

    return mock_client_instance


# For Integration tests, we need a live client that connects to a real server.
@pytest.fixture(scope="session")
async def sdk_live_client(server_url):  # Uses the event loop managed by pytest_asyncio
    """
    Provides a live OpenWebUI SDK client for integration tests.
    Ensures the client is closed after all tests in the session.
    """
    api_key = os.getenv("OPENWEBUI_API_KEY")
    if not api_key:
        pytest.fail("OPENWEBUI_API_KEY environment variable not set for integration tests.")

    # Create the client instance and explicitly manage its lifecycle
    # This pattern ensures the client is entered/exited within the fixture's scope,
    # aligning with pytest_asyncio's loop management.
    client = OpenWebUI(
        base_url=server_url, api_key=api_key, timeout=60
    )  # Increased timeout for live LLM calls

    # Manually call __aenter__ to set up the client
    await client.__aenter__()
    try:
        yield client  # Yield the client for the tests to use
    finally:
        # Manually call aclose to ensure httpx resources are released
        # This is where the RuntimeError usually happens if the loop is considered closed too soon.
        # Adding a small delay can sometimes help with race conditions, but ideal fix
        # is to ensure the cleanup is ordered correctly by pytest_asyncio.
        await asyncio.sleep(1)
        await client.aclose()


@pytest.fixture(scope="function")
async def test_folder_id(sdk_live_client):
    """
    Creates a unique folder for a test function and cleans it up afterwards.
    """
    folder_name = f"integration_test_folder_{datetime.now().strftime('%Y%m%d%H%M%S%f')}"
    folder_obj = None
    try:
        folder_obj = await sdk_live_client.folders.create(name=folder_name)
        # FIX: Access attributes using .get() notation for robustness
        yield folder_obj.get("id")
    except OpenWebUIError as e:
        pytest.fail(f"Could not prepare test folder: {e}")
    finally:
        # FIX: Access attributes using .get() notation for robustness during cleanup
        if isinstance(folder_obj, dict) and folder_obj.get("id"):
            try:
                await sdk_live_client.folders.delete(folder_obj.get("id"))
                print(f"\nCleaned up folder: {folder_obj.get('id')}")
            except OpenWebUIError as e:
                print(f"\nWarning: Could not clean up folder {folder_obj.get('id')}: {e}")
        elif hasattr(folder_obj, "id"):  # Fallback for models.FolderModel
            try:
                await sdk_live_client.folders.delete(folder_obj.id)
                print(f"\nCleaned up folder: {folder_obj.id}")
            except OpenWebUIError as e:
                print(f"\nWarning: Could not clean up folder {folder_obj.id}: {e}")


@pytest.fixture(scope="function")
async def test_kb_id(sdk_live_client):
    """
    Creates a unique knowledge base for a test function and cleans it up afterwards.
    Yields the ID of the created knowledge base.
    """
    kb_name = f"integration_test_kb_{datetime.now().strftime('%Y%m%d%H%M%S%f')}"
    kb_obj = None
    try:
        # Create the knowledge base
        kb_obj = await sdk_live_client.knowledge.create(name=kb_name, description=f"Test KB for {kb_name}")

        # Ensure it's a models.KnowledgeResponse object and extract ID
        # This handles the case where handle_api_response might return a raw dict from the patch
        if isinstance(kb_obj, dict) and "id" in kb_obj:
            yield kb_obj["id"]
        elif isinstance(kb_obj, models.KnowledgeResponse):
            yield kb_obj.id  # Direct access for models.KnowledgeResponse
        else:
            pytest.fail(f"Knowledge base creation returned unexpected type: {type(kb_obj)}. Raw: {kb_obj}")

    except OpenWebUIError as e:
        pytest.fail(f"Could not prepare test knowledge base: {e}")
    finally:
        # Clean up: delete all files first, then the KB
        kb_to_delete_id = None
        if isinstance(kb_obj, models.KnowledgeResponse) and kb_obj.id:
            kb_to_delete_id = kb_obj.id
        elif isinstance(kb_obj, dict) and kb_obj.get("id"):
            kb_to_delete_id = kb_obj["id"]

        if kb_to_delete_id:
            print(f"\n--- Cleaning up KB: {kb_to_delete_id} ---")
            try:
                # Attempt to delete all files in case any were left
                await sdk_live_client.knowledge.delete_all_files_from_kb(kb_to_delete_id)
                print(f"Cleaned up all files in KB: {kb_to_delete_id}")
            except Exception as e:
                print(f"Warning: Failed to delete files from KB {kb_to_delete_id} during cleanup: {e}")

            try:
                # Assuming a delete method on KnowledgeBaseAPI for deleting the KB itself
                await sdk_live_client.knowledge.delete(kb_to_delete_id)
                print(f"Cleaned up KB: {kb_to_delete_id}")
            except NotFoundError:
                print(f"KB '{kb_to_delete_id}' already disappeared during cleanup.")
            except OpenWebUIError as e:
                print(f"Warning: Could not delete KB {kb_to_delete_id} during cleanup: {e}")
