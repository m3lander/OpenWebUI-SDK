from unittest.mock import MagicMock

# Import the CLI application object
from openwebui.cli.main import cli

# Import generated models as specs for mocks where appropriate
from openwebui.open_web_ui_client.open_web_ui_client import models


def test_kb_create_cli_success(runner, mock_sdk_client):
    """Test `owui kb create` command for successful KB creation."""
    # The mock for this was already correct, no changes needed.
    mock_kb_response = MagicMock(spec=models.KnowledgeResponse)
    mock_kb_response.id = "new-kb-123"
    mock_kb_response.name = "My New KB"
    mock_kb_response.description = "A test knowledge base"

    mock_sdk_client.knowledge.create.return_value = mock_kb_response
    result = runner.invoke(cli, ["kb", "create", "My New KB", "--description", "A test knowledge base"])

    assert result.exit_code == 0
    assert "✅ Successfully created Knowledge Base:" in result.output
    assert "Name: My New KB" in result.output
    assert "ID:   new-kb-123" in result.output


def test_kb_list_kbs_cli_success(runner, mock_sdk_client):
    """Test `owui kb list-kbs` command with successful SDK call."""
    # FIX: Explicitly create mock objects and set their attributes.
    kb1 = MagicMock(spec=models.KnowledgeResponse)
    kb1.id = "kb1"
    kb1.name = "Proj Docs"
    kb1.description = "Docs for proj A"

    kb2 = MagicMock(spec=models.KnowledgeResponse)
    kb2.id = "kb2"
    kb2.name = "Team Data"
    kb2.description = "Data for team B"

    mock_kbs_list = [kb1, kb2]
    mock_sdk_client.knowledge.list_all.return_value = mock_kbs_list

    result = runner.invoke(cli, ["kb", "list-kbs"])

    assert result.exit_code == 0
    assert "Found Knowledge Bases:" in result.output
    # Now the assertions will work because the .name attribute returns a string.
    assert "Name: Proj Docs" in result.output
    assert "Desc: Docs for proj A" in result.output
    assert "Name: Team Data" in result.output


def test_kb_list_kbs_cli_empty(runner, mock_sdk_client):
    """Test `owui kb list-kbs` command when no KBs exist."""
    # This test was already correct.
    mock_sdk_client.knowledge.list_all.return_value = []
    result = runner.invoke(cli, ["kb", "list-kbs"])
    assert result.exit_code == 0
    assert "No knowledge bases found on the server." in result.output


def test_kb_list_files_cli_success(runner, mock_sdk_client):
    """Test `owui kb list-files` command with successful SDK call."""
    # FIX: Mock the nested structure correctly.
    # Create a mock for the `meta` object that has an `additional_properties` attribute.
    meta1 = MagicMock()
    meta1.additional_properties = {"name": "doc.pdf", "collection_name": "kb/doc.pdf"}

    meta2 = MagicMock()
    meta2.additional_properties = {"name": "image.png", "collection_name": "kb/image.png"}

    file1 = MagicMock(spec=models.FileMetadataResponse)
    file1.id = "file1"
    file1.meta = meta1

    file2 = MagicMock(spec=models.FileMetadataResponse)
    file2.id = "file2"
    file2.meta = meta2

    mock_sdk_client.knowledge.list_files.return_value = [file1, file2]

    result = runner.invoke(cli, ["kb", "list-files", "kb-abc"])

    assert result.exit_code == 0
    assert "Found 2 Files for KB 'kb-abc':" in result.output
    assert "Filename: doc.pdf" in result.output
    assert "Path:     kb/doc.pdf" in result.output


def test_kb_upload_file_cli_success(runner, mock_sdk_client, tmp_path):
    """Test `owui kb upload-file` command for successful file upload."""
    # This test was already correct.
    dummy_file = tmp_path / "upload_test.txt"
    dummy_file.write_text("Hello, World!")

    mock_uploaded_file_response = MagicMock(spec=models.FileModelResponse)
    mock_uploaded_file_response.id = "uploaded-file-id"
    mock_uploaded_file_response.filename = dummy_file.name
    mock_sdk_client.knowledge.upload_file.return_value = mock_uploaded_file_response

    result = runner.invoke(cli, ["kb", "upload-file", str(dummy_file), "--kb-id", "kb-upload-target"])

    assert result.exit_code == 0
    assert (
        "✅ Successfully uploaded 'upload_test.txt' (ID: uploaded-file-id) to KB 'kb-upload-target'."
        in result.output
    )


def test_kb_upload_dir_cli_success(runner, mock_sdk_client, tmp_path):
    """Test `owui kb upload-dir` command for successful directory upload."""
    (tmp_path / "subdir").mkdir()
    (tmp_path / "file1.txt").write_text("content1")
    (tmp_path / "subdir" / "file2.md").write_text("content2")

    mock_uploaded_files = [
        MagicMock(spec=models.FileModelResponse, id="uploaded-file1-id", filename="file1.txt"),
        MagicMock(spec=models.FileModelResponse, id="uploaded-file2-id", filename="file2.md"),
    ]
    mock_sdk_client.knowledge.upload_directory.return_value = mock_uploaded_files

    result = runner.invoke(cli, ["kb", "upload-dir", str(tmp_path), "--kb-id", "kb-dir-target"])

    assert result.exit_code == 0
    # FIX: Use an f-string to check for the correct directory name.
    assert f"✅ Successfully uploaded 2 files from '{tmp_path.name}' to KB 'kb-dir-target'." in result.output


def test_kb_delete_file_cli_success(runner, mock_sdk_client):
    """Test `owui kb delete-file` command with user confirmation."""
    # This test was already correct.
    mock_sdk_client.knowledge.delete_file.return_value = True
    result = runner.invoke(cli, ["kb", "delete-file", "file-to-delete-id"], input="y\n")
    assert result.exit_code == 0
    assert "✅ Successfully deleted file with ID: file-to-delete-id." in result.output


def test_kb_delete_file_cli_aborted(runner, mock_sdk_client):
    """Test `owui kb delete-file` command when user aborts."""
    # This test was already correct.
    mock_sdk_client.knowledge.delete_file.return_value = False
    result = runner.invoke(cli, ["kb", "delete-file", "file-id-ignored"], input="n\n")
    assert result.exit_code == 1
    assert "Aborted." in result.output


def test_kb_delete_all_files_cli_success(runner, mock_sdk_client):
    """Test `owui kb delete-all-files` command with `--yes` flag."""
    mock_sdk_client.knowledge.delete_all_files_from_kb.return_value = {"successful": 5, "failed": 0}

    result = runner.invoke(cli, ["kb", "delete-all-files", "kb-to-clear", "--yes"])

    assert result.exit_code == 0
    assert "✅ All files deleted successfully." in result.output
    assert "Successfully deleted: 5" in result.output
    # FIX: Do not assert the "Failed" line when there are no failures.
    assert "Failed to delete" not in result.output


def test_kb_delete_all_files_cli_partial_failure(runner, mock_sdk_client):
    """Test `owui kb delete-all-files` command with partial failure and `--yes` flag."""
    # This test was already correct.
    mock_sdk_client.knowledge.delete_all_files_from_kb.return_value = {"successful": 3, "failed": 2}
    result = runner.invoke(cli, ["kb", "delete-all-files", "kb-to-clear", "--yes"])
    assert result.exit_code == 1
    assert "❌ Completed with 2 errors during deletion." in result.output
    assert "Successfully deleted: 3" in result.output
    assert "Failed to delete: 2" in result.output
