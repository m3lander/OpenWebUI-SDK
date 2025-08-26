from unittest.mock import MagicMock

# Import the CLI application object
from openwebui.cli.main import cli

# Import generated models as specs for mocks where appropriate
from openwebui.open_web_ui_client.open_web_ui_client import models


# --- Test Cases for Chat Commands ---


def test_chat_create_cli_success(runner, mock_sdk_client):
    """Test `owui chat create` command for successful chat creation."""
    mock_chat_response = MagicMock(spec=models.ChatResponse, id="new-chat-xyz", title="Test Chat")
    mock_chat_response.chat.additional_properties = {
        "messages": [
            {"role": "user", "content": "User prompt."},
            {"role": "assistant", "content": "Assistant response."},
        ]
    }
    mock_sdk_client.chats.create.return_value = mock_chat_response

    result = runner.invoke(cli, ["chat", "create", "Initial prompt"])

    assert result.exit_code == 0
    assert "✅ Success! New chat created with ID: new-chat-xyz" in result.output
    assert "Assistant Response:" in result.output
    assert "Assistant response." in result.output


def test_chat_continue_cli_success(runner, mock_sdk_client):
    """Test `owui chat continue` command for successful chat continuation."""
    mock_updated_chat = MagicMock(spec=models.ChatResponse, id="existing-chat-id", title="Continued Chat")
    mock_updated_chat.chat.additional_properties = {
        "messages": [
            {"role": "user", "content": "Old user msg."},
            {"role": "assistant", "content": "Old assistant msg."},
            {"role": "user", "content": "New user msg."},
            {"role": "assistant", "content": "New assistant response."},
        ]
    }
    mock_sdk_client.chats.continue_chat.return_value = mock_updated_chat

    result = runner.invoke(cli, ["chat", "continue", "existing-chat-id", "New user prompt"])

    assert result.exit_code == 0
    assert "✅ Success! Chat existing-chat-id updated." in result.output
    assert "Assistant Response:" in result.output
    assert "New assistant response." in result.output


def test_chat_list_messages_cli_success(runner, mock_sdk_client):
    """Test `owui chat list` command for successfully listing messages."""
    mock_chat_details = MagicMock(spec=models.ChatResponse, title="My Chat Title")
    mock_chat_details.chat.additional_properties = {
        "messages": [
            {"role": "user", "content": "First user message."},
            {"role": "assistant", "content": "First assistant message."},
            {"role": "user", "content": "Second user message."},
        ]
    }
    mock_sdk_client.chats.get.return_value = mock_chat_details
    result = runner.invoke(cli, ["chat", "list", "chat-id-to-list"])  # cli calls with positional arg
    assert result.exit_code == 0
    assert "Messages for Chat 'My Chat Title'" in result.output
    assert "---" in result.output
    assert "User:\nFirst user message.\n\n" in result.output
    assert "Assistant:\nFirst assistant message.\n\n" in result.output
    assert "User:\nSecond user message.\n\n" in result.output

    # FIX: Change assert_awaited_once_with to expect a positional argument
    mock_sdk_client.chats.get.assert_awaited_once_with("chat-id-to-list")


def test_chat_rename_cli_success(runner, mock_sdk_client):
    """Test `owui chat rename` command for successful renaming."""
    mock_sdk_client.chats.rename.return_value = MagicMock(title="Renamed Chat")

    result = runner.invoke(cli, ["chat", "rename", "chat-id-rename", "Renamed Chat"])

    assert result.exit_code == 0
    assert "✅ Chat 'chat-id-rename' renamed to 'Renamed Chat'." in result.output
    mock_sdk_client.chats.rename.assert_awaited_once_with(chat_id="chat-id-rename", new_title="Renamed Chat")


def test_chat_delete_cli_success(runner, mock_sdk_client):
    """Test `owui chat delete` command with user confirmation."""
    mock_sdk_client.chats.delete.return_value = True

    result = runner.invoke(cli, ["chat", "delete", "chat-to-delete"], input="y\n")

    assert result.exit_code == 0
    assert "✅ Chat 'chat-to-delete' deleted successfully." in result.output
    mock_sdk_client.chats.delete.assert_awaited_once_with(chat_id="chat-to-delete")


def test_chat_delete_cli_aborted(runner, mock_sdk_client):
    """Test `owui chat delete` when user aborts."""
    mock_sdk_client.chats.delete.return_value = False  # Or just not configure it
    result = runner.invoke(cli, ["chat", "delete", "doesnt-matter"], input="n\n")

    # FIX: Expect exit_code 1 due to click.Abort() in main.py
    assert result.exit_code == 1
    assert "Aborted." in result.output
    mock_sdk_client.chats.delete.assert_not_awaited()
