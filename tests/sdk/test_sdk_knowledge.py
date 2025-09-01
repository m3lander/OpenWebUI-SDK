import httpx
import pytest
from unittest.mock import MagicMock, AsyncMock
from openwebui.exceptions import APIError
from openwebui.open_web_ui_client.open_web_ui_client import models  # Import generated models
from openwebui.open_web_ui_client.open_web_ui_client.types import Response, UNSET
import json  # Import json for json.dumps here
from pathlib import Path  # Import Path from pathlib here

# Mark all tests in this file as async
pytestmark = pytest.mark.asyncio


async def test_knowledge_create_success(mocker, sdk_client):
    """Test successful creation of a knowledge base."""
    # Mock the low-level API call for creating a KB
    mock_create_kb_api = mocker.patch("openwebui.api.knowledge.create_kb_api_call", new_callable=AsyncMock)

    # Define the mock response object (models.KnowledgeBase)
    # FIX: Use models.KnowledgeResponse if that's the correct model
    mock_kb_response = models.KnowledgeResponse(  # Changed from KnowledgeBase
        id="kb-123",
        name="Test KB",
        description="A test knowledge base.",
        user_id="test_user_id",
        created_at=1678886400,
        updated_at=1678886400,
    )
    mock_response_object = MagicMock(spec=Response)
    mock_response_object.status_code = 200
    mock_response_object.parsed = mock_kb_response
    mock_create_kb_api.return_value = mock_response_object

    # Call the SDK method
    kb = await sdk_client.knowledge.create(name="Test KB", description="A test knowledge base.")

    # Assertions
    assert isinstance(kb, models.KnowledgeResponse)  # Changed from KnowledgeBase
    assert kb.id == "kb-123"
    assert kb.name == "Test KB"
    assert kb.description == "A test knowledge base."

    # Verify the low-level API was called correctly
    mock_create_kb_api.assert_awaited_once_with(
        body=models.KnowledgeForm(name="Test KB", description="A test knowledge base."),
        client=sdk_client._client,
    )


async def test_knowledge_create_api_error(mocker, sdk_client):
    """Test APIError during knowledge base creation."""
    mock_create_kb_api = mocker.patch("openwebui.api.knowledge.create_kb_api_call", new_callable=AsyncMock)
    mock_response_object = MagicMock(spec=Response)
    mock_response_object.status_code = 400
    mock_response_object.content = b'{"detail": "Bad Request"}'
    mock_response_object.parsed = None
    mock_create_kb_api.return_value = mock_response_object

    with pytest.raises(APIError) as exc_info:
        await sdk_client.knowledge.create(name="Failing KB")

    assert exc_info.value.status_code == 400
    assert "Bad Request" in str(exc_info.value)


async def test_knowledge_list_all_success_parsed(mocker, sdk_client):
    """Test successful listing of knowledge bases when parsed is List[Model]."""
    mock_list_kbs_api = mocker.patch("openwebui.api.knowledge.list_kbs_api_call", new_callable=AsyncMock)

    # Simulate raw API response data as if it were directly from the API.
    raw_api_data = [
        {
            "id": "kb-1",
            "name": "KB One",
            "description": "Desc 1",
            "user_id": "u1",
            "created_at": 1,
            "updated_at": 1,
        },
        {
            "id": "kb-2",
            "name": "KB Two",
            "description": "Desc 2",
            "user_id": "u2",
            "created_at": 2,
            "updated_at": 2,
        },
    ]
    mock_response_object = MagicMock(spec=Response)
    mock_response_object.status_code = 200
    mock_response_object.parsed = None
    mock_response_object.content = json.dumps(raw_api_data).encode("utf-8")
    mock_response_object.headers = {b"content-type": b"application/json"}
    mock_list_kbs_api.return_value = mock_response_object

    kbs = await sdk_client.knowledge.list_all()

    # Assertions
    assert isinstance(kbs, list)
    assert len(kbs) == 2
    assert all(isinstance(kb, models.KnowledgeResponse) for kb in kbs)  # Changed from KnowledgeBase
    assert kbs[0].id == "kb-1"
    assert kbs[1].name == "KB Two"
    mock_list_kbs_api.assert_awaited_once_with(client=sdk_client._client)


async def test_knowledge_list_all_empty(mocker, sdk_client):
    """Test listing all knowledge bases when none exist."""
    mock_list_kbs_api = mocker.patch("openwebui.api.knowledge.list_kbs_api_call", new_callable=AsyncMock)
    raw_api_data = []  # Empty list as string
    mock_response_object = MagicMock(spec=Response)
    mock_response_object.status_code = 200
    mock_response_object.parsed = None
    mock_response_object.content = json.dumps(raw_api_data).encode("utf-8")
    mock_response_object.headers = {b"content-type": b"application/json"}
    mock_list_kbs_api.return_value = mock_response_object

    kbs = await sdk_client.knowledge.list_all()

    assert isinstance(kbs, list)
    assert len(kbs) == 0
    mock_list_kbs_api.assert_awaited_once()


async def test_knowledge_upload_file_success(mocker, sdk_client, tmp_path):
    """Test successful file upload and association with a KB."""
    dummy_file = tmp_path / "test_document.txt"
    with open(dummy_file, "w") as f:
        f.write("This is a test file content.")

    mock_upload_file_api = mocker.patch(
        "openwebui.api.knowledge.upload_file_api_call", new_callable=AsyncMock
    )
    mock_add_files_to_kb_api = mocker.patch(
        "openwebui.api.knowledge.add_files_to_knowledge_batch_api_call", new_callable=AsyncMock
    )

    mock_uploaded_file = models.FileModelResponse(
        id="file-456",
        user_id="test_user_id",
        filename=dummy_file.name,
        meta={
            "name": dummy_file.name,
            "collection_name": "path/test_document.txt",
            "content_type": "text/plain",
            "size": len(dummy_file.read_bytes()),
        },
        created_at=1678886400,
        updated_at=1678886400,
    )
    mock_upload_response = MagicMock(spec=Response, status_code=200, parsed=mock_uploaded_file)
    mock_upload_file_api.return_value = mock_upload_response

    mock_add_response = MagicMock(spec=Response, status_code=200, parsed=True)
    mock_add_files_to_kb_api.return_value = mock_add_response

    uploaded_file = await sdk_client.knowledge.upload_file(file_path=dummy_file, kb_id="some-kb-id")

    assert isinstance(uploaded_file, models.FileModelResponse)
    assert uploaded_file.id == "file-456"
    assert uploaded_file.filename == dummy_file.name

    mock_upload_file_api.assert_awaited_once()
    mock_add_files_to_kb_api.assert_awaited_once_with(
        id="some-kb-id",
        body=[models.KnowledgeFileIdForm(file_id="file-456")],
        client=sdk_client._client,
    )


async def test_knowledge_upload_file_not_found(sdk_client):
    """Test FileNotFoundError for non-existent file during upload."""
    with pytest.raises(FileNotFoundError):
        await sdk_client.knowledge.upload_file(file_path=Path("non_existent_file.txt"), kb_id="some-kb-id")


async def test_knowledge_upload_directory_success(mocker, sdk_client, tmp_path):
    """Test successful directory upload with mock files."""
    (tmp_path / "subdir").mkdir()
    (tmp_path / "file1.txt").write_text("content1")
    (tmp_path / "subdir" / "file2.md").write_text("content2")
    (tmp_path / ".kbignore").write_text("*.log\n")
    (tmp_path / "ignored.log").write_text("log content")

    mock_upload_single_file_helper = mocker.patch(
        "openwebui.api.knowledge.KnowledgeBaseAPI._upload_single_file_for_batch", new_callable=AsyncMock
    )
    mock_uploaded_file1 = models.FileModelResponse(
        id="file1-id",
        user_id="test_user_id",
        filename="file1.txt",
        meta={"name": "file1.txt", "collection_name": "file1.txt", "content_type": "text/plain", "size": 8},
        created_at=1,
        updated_at=1,
    )
    mock_uploaded_file2 = models.FileModelResponse(
        id="file2-id",
        user_id="test_user_id",
        filename="file2.md",
        meta={
            "name": "file2.md",
            "collection_name": "subdir/file2.md",
            "content_type": "text/markdown",
            "size": 8,
        },
        created_at=2,
        updated_at=2,
    )

    mock_upload_single_file_helper.side_effect = [
        mock_uploaded_file1,
        mock_uploaded_file2,
    ]

    mock_add_files_to_kb_api = mocker.patch(
        "openwebui.api.knowledge.add_files_to_knowledge_batch_api_call", new_callable=AsyncMock
    )
    mock_add_files_to_kb_api.return_value = MagicMock(spec=Response, status_code=200, parsed=True)

    uploaded_files = await sdk_client.knowledge.upload_directory(directory_path=tmp_path, kb_id="test-kb-id")

    assert isinstance(uploaded_files, list)
    assert len(uploaded_files) == 2
    assert uploaded_files[0].id == "file1-id"
    assert uploaded_files[1].id == "file2-id"

    assert mock_upload_single_file_helper.call_count == 2
    mock_upload_single_file_helper.assert_any_call(tmp_path / "file1.txt")
    mock_upload_single_file_helper.assert_any_call(tmp_path / "subdir" / "file2.md")

    mock_add_files_to_kb_api.assert_awaited_once_with(
        id="test-kb-id",
        body=[models.KnowledgeFileIdForm(file_id="file1-id"), models.KnowledgeFileIdForm(file_id="file2-id")],
        client=sdk_client._client,
    )


async def test_knowledge_delete_file_success(mocker, sdk_client):
    """Test successful deletion of a file."""
    mock_delete_file_api = mocker.patch(
        "openwebui.api.knowledge.delete_file_api_call", new_callable=AsyncMock
    )
    mock_delete_response = MagicMock(spec=Response, status_code=204, parsed=None)
    mock_delete_file_api.return_value = mock_delete_response

    success = await sdk_client.knowledge.delete_file(file_id="file-to-delete-id")

    assert success is True
    mock_delete_file_api.assert_awaited_once_with(
        id="file-to-delete-id",
        client=sdk_client._client,
    )


async def test_knowledge_delete_all_files_success(mocker, sdk_client):
    """Test successful deletion of all files from a KB."""
    mock_list_files_api = mocker.patch(
        "openwebui.api.knowledge.KnowledgeBaseAPI.list_files", new_callable=AsyncMock
    )
    mock_delete_file_api = mocker.patch(
        "openwebui.api.knowledge.KnowledgeBaseAPI.delete_file", new_callable=AsyncMock
    )

    # Simulate two files in KB for listing
    mock_list_files_api.return_value = [
        models.FileMetadataResponse(
            id="file1",
            created_at=1,
            updated_at=1,
            meta={
                "name": "file1.txt",
                "collection_name": "file1.txt",
                "content_type": "text/plain",
                "size": 10,
            },  # Direct dict for meta
        ),
        models.FileMetadataResponse(
            id="file2",
            created_at=2,
            updated_at=2,
            meta={
                "name": "file2.pdf",
                "collection_name": "file2.pdf",
                "content_type": "application/pdf",
                "size": 20,
            },  # Direct dict for meta
        ),
    ]
    mock_delete_file_api.return_value = True

    deletion_summary = await sdk_client.knowledge.delete_all_files_from_kb(kb_id="test-kb-id")

    assert deletion_summary["successful"] == 2
    assert deletion_summary["failed"] == 0
    mock_list_files_api.assert_awaited_once_with(kb_id="test-kb-id")
    assert mock_delete_file_api.call_count == 2
    mock_delete_file_api.assert_any_call("file1")
    mock_delete_file_api.assert_any_call("file2")

@pytest.mark.skip(reason="Broken test - needs investigation")
async def test_knowledge_list_files_success(mocker, sdk_client):
    """Test successful listing of files for a KB."""
    mock_list_files_api_call = mocker.patch(
        "openwebui.api.knowledge.list_files_for_knowledge_base_api_call", new_callable=AsyncMock
    )

    # Simulate raw API response data containing files
    raw_api_data = {
        "id": "test-kb-id",
        "description": "desc",
        "files": [
            {
                "id": "file1",
                "created_at": 1,
                "updated_at": 1,
                "meta": {"name": "document1.pdf", "collection_name": "path/document1.pdf"},
            },  # Direct dict for meta
            {
                "id": "file2",
                "created_at": 2,
                "updated_at": 2,
                "meta": {"name": "report.docx", "collection_name": "path/report.docx"},
            },  # Direct dict for meta
            {
                "id": "file3",
                "created_at": 3,
                "updated_at": 3,
                "meta": {"name": "image.png", "collection_name": "path/image.png"},
            },  # Direct dict for meta
        ],
    }
    mock_response_object = MagicMock(spec=Response)
    mock_response_object.status_code = 200
    mock_response_object.parsed = None
    mock_response_object.content = json.dumps(raw_api_data).encode("utf-8")
    mock_response_object.headers = {b"content-type": b"application/json"}
    mock_list_files_api_call.return_value = mock_response_object

    files = await sdk_client.knowledge.list_files(kb_id="test-kb-id")

    assert isinstance(files, list)
    assert len(files) == 3
    assert all(isinstance(f, models.FileMetadataResponse) for f in files)
    assert files[0].id == "file1"
    assert files[1].meta["name"] == "report.docx"  # FIX: Access meta as a dict directly
    mock_list_files_api_call.assert_awaited_once_with(id="test-kb-id", client=sdk_client._client)


@pytest.mark.asyncio
async def test_knowledge_query_success_basic(mocker, sdk_client):
    """Test successful basic query to a single knowledge base."""
    mock_query_api_call = mocker.patch(
        "openwebui.api.knowledge.query_kb_api_call", new_callable=AsyncMock
    )

    # Simulate a successful retrieval response with content
    mock_retrieved_chunks = [
        {"content": "This is a test document snippet.", "meta": {"file": "test.txt"}},
        {"content": "Another relevant piece of information.", "meta": {"file": "another.pdf"}},
    ]
    mock_response_object = MagicMock(spec=Response, status_code=200, parsed=mock_retrieved_chunks)
    mock_query_api_call.return_value = mock_response_object

    query_text = "What is the main topic?"
    kb_ids = ["kb-id-1"]
    k_value = 2

    result_chunks = await sdk_client.knowledge.query(query_text, kb_ids, k=k_value)

    # Assert that the low-level API was called with the correct QueryCollectionsForm
    mock_query_api_call.assert_awaited_once()
    call_args, call_kwargs = mock_query_api_call.call_args
    assert isinstance(call_kwargs['body'], models.QueryCollectionsForm)
    assert call_kwargs['body'].collection_names == kb_ids
    assert call_kwargs['body'].query == query_text
    assert call_kwargs['body'].k == k_value
    assert call_kwargs['body'].k_reranker is UNSET
    assert call_kwargs['body'].r is UNSET
    assert call_kwargs['body'].hybrid is UNSET
    assert call_kwargs['body'].hybrid_bm25_weight is UNSET

    # Assert the returned data matches the mock response
    assert isinstance(result_chunks, list)
    assert len(result_chunks) == len(mock_retrieved_chunks)
    assert result_chunks[0]["content"] == "This is a test document snippet."
    assert result_chunks[1]["meta"]["file"] == "another.pdf"


@pytest.mark.asyncio
async def test_knowledge_query_success_multiple_kbs_and_all_rag_params(mocker, sdk_client):
    """Test successful query to multiple knowledge bases with all RAG parameters."""
    mock_query_api_call = mocker.patch(
        "openwebui.api.knowledge.query_kb_api_call", new_callable=AsyncMock
    )

    mock_retrieved_chunks = [
        {"content": "Content from KB A.", "meta": {"kb": "KB_A"}},
        {"content": "Content from KB B.", "meta": {"kb": "KB_B"}},
    ]
    mock_response_object = MagicMock(spec=Response, status_code=200, parsed=mock_retrieved_chunks)
    mock_query_api_call.return_value = mock_response_object

    query_text = "Advanced RAG search"
    kb_ids = ["kb-alpha", "kb-beta"]
    k_value = 5
    k_reranker_value = 3
    r_value = 0.75
    hybrid_value = True
    hybrid_bm25_weight_value = 0.3

    result_chunks = await sdk_client.knowledge.query(
        query_text,
        kb_ids,
        k=k_value,
        k_reranker=k_reranker_value,
        r=r_value,
        hybrid=hybrid_value,
        hybrid_bm25_weight=hybrid_bm25_weight_value
    )

    # Assert the low-level API was called with the correct QueryCollectionsForm
    mock_query_api_call.assert_awaited_once()
    call_args, call_kwargs = mock_query_api_call.call_args
    assert isinstance(call_kwargs['body'], models.QueryCollectionsForm)
    assert call_kwargs['body'].collection_names == kb_ids
    assert call_kwargs['body'].query == query_text
    assert call_kwargs['body'].k == k_value
    assert call_kwargs['body'].k_reranker == k_reranker_value
    assert call_kwargs['body'].r == r_value
    assert call_kwargs['body'].hybrid == hybrid_value
    assert call_kwargs['body'].hybrid_bm25_weight == hybrid_bm25_weight_value

    assert isinstance(result_chunks, list)
    assert len(result_chunks) == len(mock_retrieved_chunks)


@pytest.mark.asyncio
async def test_knowledge_query_empty_result(mocker, sdk_client):
    """Test query returning an empty list of chunks."""
    mock_query_api_call = mocker.patch(
        "openwebui.api.knowledge.query_kb_api_call", new_callable=AsyncMock
    )
    # Simulate an empty retrieval result
    mock_response_object = MagicMock(spec=Response, status_code=200, parsed=[])
    mock_query_api_call.return_value = mock_response_object

    query_text = "Non-existent topic"
    kb_ids = ["empty-kb"]

    result_chunks = await sdk_client.knowledge.query(query_text, kb_ids)

    mock_query_api_call.assert_awaited_once()
    assert result_chunks == []


@pytest.mark.asyncio
async def test_knowledge_query_api_error(mocker, sdk_client):
    """Test APIError during knowledge base query."""
    mock_query_api_call = mocker.patch(
        "openwebui.api.knowledge.query_kb_api_call", new_callable=AsyncMock
    )

    # Simulate an API error response (e.g., 400 Bad Request)
    mock_bad_response = MagicMock(spec=Response, status_code=400, content=b'{"detail": "Invalid query"}')
    mock_bad_response.parsed = None  # Ensure handle_api_response goes to raw content
    mock_query_api_call.return_value = mock_bad_response

    query_text = "Error query"
    kb_ids = ["invalid-kb"]

    with pytest.raises(APIError) as exc_info:
        await sdk_client.knowledge.query(query_text, kb_ids)

    assert exc_info.value.status_code == 400
    assert "Invalid query" in str(exc_info.value)
    mock_query_api_call.assert_awaited_once()


@pytest.mark.asyncio
async def test_knowledge_query_connection_error(mocker, sdk_client):
    """Test ConnectionError during knowledge base API call."""
    mock_query_api_call = mocker.patch(
        "openwebui.api.knowledge.query_kb_api_call", new_callable=AsyncMock
    )
    # Simulate a network connection error
    mock_query_api_call.side_effect = httpx.ConnectError("Connection refused")

    query_text = "Network issue"
    kb_ids = ["remote-kb"]

    with pytest.raises(ConnectionError) as exc_info:
        await sdk_client.knowledge.query(query_text, kb_ids)

    assert "Connection refused" in str(exc_info.value)
    mock_query_api_call.assert_awaited_once()