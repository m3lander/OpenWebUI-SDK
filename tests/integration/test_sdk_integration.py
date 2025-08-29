import pytest
import os
from datetime import datetime

from openwebui.client import OpenWebUI
from openwebui.exceptions import OpenWebUIError, NotFoundError

# Mark all tests in this file as async
pytestmark = pytest.mark.asyncio

# Explicitly load the pytest_asyncio plugin for session scope fixtures
pytest_plugins = ["pytest_asyncio"]


@pytest.fixture(scope="session")
async def sdk_live_client(server_url):  # Removed asyncio_loop as a direct dependency here
    """
    Provides a live OpenWebUI SDK client for integration tests.
    Ensures the client is closed after all tests in the session.
    """
    # Use the server_url from conftest.py which pulls from env vars
    api_key = os.getenv("OPENWEBUI_API_KEY")
    if not api_key:
        pytest.fail("OPENWEBUI_API_KEY environment variable not set for integration tests.")

    # Initialize the client within the session's event loop context
    # Use the 'async with client:' pattern to ensure proper aclose()
    try:
        # OpenWebUI itself is an async context manager, so passing it to this
        # fixture will manage its lifecycle.
        client = OpenWebUI(
            base_url=server_url, api_key=api_key, timeout=60
        )  # Increased timeout for live LLM calls
        # We need to explicitly run __aenter__ because pytest's async fixtures
        # expect the aenter/aexit to be handled within the fixture itself.
        await client.__aenter__()
        yield client  # Yield the client for the tests to use
    finally:
        # This ensures __aexit__ is called when the fixture tears down
        await client.__aexit__(None, None, None)


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
        # Cast to dict for type checker if your SDK is typed strictly and returns models.
        # If folder_obj is an actual models.FolderModel (an attrs object), .id is correct.
        if isinstance(folder_obj, dict):
            yield folder_obj.get("id")
        else:  # Assume it's a models.FolderModel
            yield folder_obj.id
    except OpenWebUIError as e:
        pytest.fail(f"Could not prepare test folder: {e}")
    finally:
        # FIX: Access attributes using .get() notation for robustness during cleanup
        # Need to check if it's a dict or an object
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


# --- Integration Test Scenarios ---
# @pytest.mark.skip(reason="Broken")
async def test_full_chat_workflow_with_folder(sdk_live_client, test_folder_id):
    """
    Tests creating a chat, continuing it, listing messages, renaming,
    and then cleaning up, all within a dedicated folder.
    """
    chat_id = None  # Initialize to None for cleanup in case of early failure
    folder_id = test_folder_id  # Use the ID from the fixture

    try:
        # 1. Create a new chat within the test folder
        initial_prompt = "Tell me a very short story about a brave mouse."
        model_name = "gemini-2.5-flash"  # Use a model available on your Open WebUI instance

        print(f"\n--- Creating chat in folder '{folder_id}' ---")
        new_chat = await sdk_live_client.chats.create(
            model=model_name, prompt=initial_prompt, folder_id=folder_id
        )
        # FIX: Be defensive - use .get() for dict-like access, but still expect certain keys.
        chat_id = new_chat.get("id") if isinstance(new_chat, dict) else new_chat.id
        assert chat_id is not None
        # Access nested structures defensively
        messages_from_chat = (
            new_chat.get("chat", {}).get("additional_properties", {}).get("messages")
            if isinstance(new_chat, dict)
            else new_chat.chat.additional_properties.get("messages")
        )
        assert messages_from_chat is not None

        # FIX: Changed LLM assertion to be less brittle
        response_content = messages_from_chat[-1].get("content", "")
        assert len(response_content) > 10  # Check it's not empty and has some length
        assert (
            "mouse" in response_content.lower() or "story" in response_content.lower()
        )  # Check for relevant keyword

        title_from_chat = new_chat.get("title") if isinstance(new_chat, dict) else new_chat.title
        print(f"Created chat ID: {chat_id}, Title: {title_from_chat}")

        # 2. Continue the chat
        followup_prompt = "What was the mouse's name?"
        print(f"\n--- Continuing chat '{chat_id}' ---")
        updated_chat = await sdk_live_client.chats.continue_chat(chat_id, followup_prompt)
        assert (updated_chat.get("id") if isinstance(updated_chat, dict) else updated_chat.id) == chat_id
        messages_from_updated_chat = (
            updated_chat.get("chat", {}).get("additional_properties", {}).get("messages")
            if isinstance(updated_chat, dict)
            else updated_chat.chat.additional_properties.get("messages")
        )
        assert len(messages_from_updated_chat) > 2

        # FIX: Changed LLM assertion to be less brittle
        updated_response_content = messages_from_updated_chat[-1].get("content", "")
        assert len(updated_response_content) > 10  # Check it's not empty and has some length
        assert "name" in updated_response_content.lower()  # Should mention a name

        print(f"Chat continued. Latest assistant content: {updated_response_content}")

        # 3. List messages in the chat
        print(f"\n--- Listing messages for chat '{chat_id}' ---")
        fetched_chat = await sdk_live_client.chats.get(chat_id)
        assert (fetched_chat.get("id") if isinstance(fetched_chat, dict) else fetched_chat.id) == chat_id
        messages_from_fetched_chat = (
            fetched_chat.get("chat", {}).get("additional_properties", {}).get("messages")
            if isinstance(fetched_chat, dict)
            else fetched_chat.chat.additional_properties.get("messages")
        )
        assert len(messages_from_fetched_chat) == len(messages_from_updated_chat)
        print(f"Fetched {len(messages_from_fetched_chat)} messages.")

        # 4. Rename the chat
        new_title = "The Brave Mouse Story"
        print(f"\n--- Renaming chat '{chat_id}' to '{new_title}' ---")
        renamed_chat = await sdk_live_client.chats.rename(chat_id, new_title)
        assert (renamed_chat.get("id") if isinstance(renamed_chat, dict) else renamed_chat.id) == chat_id
        assert (
            renamed_chat.get("title") if isinstance(renamed_chat, dict) else renamed_chat.title
        ) == new_title
        print(
            f"Chat renamed to: {(renamed_chat.get('title') if isinstance(renamed_chat, dict) else renamed_chat.title)}"
        )

        # 5. Verify chat exists in folder
        print(f"\n--- Verifying chat '{chat_id}' in folder '{folder_id}' ---")
        chats_in_folder = await sdk_live_client.chats.list_by_folder(folder_id)
        assert any((c.get("id") if isinstance(c, dict) else c.id) == chat_id for c in chats_in_folder)
        print(f"Chat '{chat_id}' found in folder '{folder_id}'.")

    except Exception as e:
        pytest.fail(f"Full chat workflow failed: {e}")
    finally:
        # 6. Delete the chat (cleanup)
        if chat_id:
            print(f"\n--- Deleting chat '{chat_id}' ---")
            try:
                delete_success = await sdk_live_client.chats.delete(chat_id)
                assert delete_success is True
                print(f"Chat '{chat_id}' deleted successfully.")
            except NotFoundError:  # Catch specific errors
                print(f"Chat '{chat_id}' already deleted (or not found during cleanup).")
            except OpenWebUIError as e:  # Catch general SDK errors
                print(f"Warning: Could not delete chat {chat_id} during cleanup: {e}")
