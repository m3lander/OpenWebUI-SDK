import pytest
from unittest.mock import MagicMock, AsyncMock

from openwebui.exceptions import NotFoundError
from openwebui.open_web_ui_client.open_web_ui_client import models
from openwebui.open_web_ui_client.open_web_ui_client.types import Response

# Mark all tests in this file as async
pytestmark = pytest.mark.asyncio


async def test_chats_list_success(mocker, sdk_client):
    """Tests successful listing of chat titles."""
    # Mock the low-level API function
    mock_api_func = mocker.patch(
        "openwebui.api.chats.get_session_user_chat_list_api_v1_chats_list_get.asyncio_detailed"
    )

    # Prepare the mock response data
    mock_chat_list = [
        models.ChatTitleIdResponse(id="chat1", title="Chat One", created_at=1, updated_at=1),
        models.ChatTitleIdResponse(id="chat2", title="Chat Two", created_at=2, updated_at=2),
    ]
    mock_response = MagicMock(spec=Response, status_code=200, parsed=mock_chat_list)
    mock_api_func.return_value = mock_response

    # Call the SDK method
    chats = await sdk_client.chats.list()

    # Assertions
    assert len(chats) == 2
    assert chats[0].title == "Chat One"
    mock_api_func.assert_awaited_once()


async def test_chats_get_success(mocker, sdk_client):
    """Tests successfully fetching a single chat's details."""
    mock_api_func = mocker.patch("openwebui.api.chats.get_chat_by_id_api_v1_chats_id_get.asyncio_detailed")

    mock_chat_details = models.ChatResponse(
        id="chat1", user_id="user1", title="Test Chat", chat={}, created_at=1, updated_at=1, archived=False
    )
    mock_response = MagicMock(spec=Response, status_code=200, parsed=mock_chat_details)
    mock_api_func.return_value = mock_response

    chat = await sdk_client.chats.get("chat1")

    assert chat.id == "chat1"
    assert chat.title == "Test Chat"
    mock_api_func.assert_awaited_once_with(id="chat1", client=sdk_client._client)


async def test_chats_get_not_found(mocker, sdk_client):
    """Tests fetching a chat that does not exist."""
    mock_api_func = mocker.patch("openwebui.api.chats.get_chat_by_id_api_v1_chats_id_get.asyncio_detailed")

    # FIX: Add the 'url' attribute to the mock response
    mock_response = MagicMock(
        spec=Response, status_code=404, url="http://test.com/api/v1/chats/non-existent-id"
    )
    mock_api_func.return_value = mock_response

    with pytest.raises(NotFoundError):
        await sdk_client.chats.get("non-existent-id")


async def test_chats_delete_success(mocker, sdk_client):
    """Tests successful chat deletion."""
    mock_api_func = mocker.patch(
        "openwebui.api.chats.delete_chat_by_id_api_v1_chats_id_delete.asyncio_detailed"
    )

    mock_response = MagicMock(spec=Response, status_code=200, parsed=True)
    mock_api_func.return_value = mock_response

    success = await sdk_client.chats.delete("chat-to-delete")

    assert success is True
    mock_api_func.assert_awaited_once_with(id="chat-to-delete", client=sdk_client._client)


@pytest.mark.asyncio
async def test_chats_create_success(mocker, sdk_client):
    """Tests the complex two-step chat creation workflow including optional RAG."""
    # 1. Mock the LLM completion API call
    mock_llm_api = mocker.patch(
        "openwebui.api.chats.generate_chat_completion_openai_chat_completions_post.asyncio_detailed"
    )
    llm_response_data = {"choices": [{"message": {"content": "The capital of France is Paris."}}]}
    mock_llm_response = MagicMock(spec=Response, status_code=200, parsed=llm_response_data)
    mock_llm_api.return_value = mock_llm_response

    # 2. Mock the chat creation API call
    mock_create_api = mocker.patch(
        "openwebui.api.chats.create_new_chat_api_v1_chats_new_post.asyncio_detailed"
    )
    final_chat_response = models.ChatResponse(
        id="new-chat-123",
        user_id="user1",
        title="New Chat",
        chat=models.ChatResponseChat(),  # Chat response often has empty chat on creation
        created_at=1,
        updated_at=1,
        archived=False,
    )
    mock_create_response = MagicMock(spec=Response, status_code=200, parsed=final_chat_response)
    mock_create_api.return_value = mock_create_response

    # --- RAG Specific Mocking ---
    # Mock the KnowledgeBaseAPI.query method that ChatsAPI uses
    mock_kb_query = mocker.patch(
        "openwebui.api.knowledge.KnowledgeBaseAPI.query", new_callable=AsyncMock
    )
    # Configure it to return a list of dictionaries, simulating chunks
    mock_kb_query.return_value = [
        {"content": "Relevant KB content about France."},
        {"content": "More details about European capitals."},
    ]

    # Test 1: Basic chat creation (no RAG)
    new_chat_no_rag = await sdk_client.chats.create(model="test-model", prompt="What is the capital of France?")
    assert new_chat_no_rag.id == "new-chat-123"
    mock_llm_api.assert_awaited_once()  # Should be called once for this test

    # Reset mocks for the next test
    mock_llm_api.reset_mock()
    mock_create_api.reset_mock()
    mock_kb_query.reset_mock()

    # Reconfigure mock_create_api for the next chat creation
    mock_create_api.return_value = MagicMock(spec=Response, status_code=200, parsed=final_chat_response)

    # Test 2: Chat creation WITH RAG parameters
    kb_ids_to_use = ["my-kb-id-1", "another-kb-id-2"]
    rag_k = 5
    rag_r = 0.7

    new_chat_with_rag = await sdk_client.chats.create(
        model="test-model",
        prompt="Tell me about AI",
        kb_ids=kb_ids_to_use,
        k=rag_k,
        r=rag_r,
        hybrid=True,
    )

    assert new_chat_with_rag.id == "new-chat-123"  # Still returns the same mocked chat

    # Verify KnowledgeBaseAPI.query was called correctly
    mock_kb_query.assert_awaited_once_with(
        "Tell me about AI",  # Original prompt passed to KB query
        kb_ids_to_use,
        k=rag_k,
        k_reranker=None,  # Not set in this call
        r=rag_r,
        hybrid=True,
        hybrid_bm25_weight=None,  # Not set in this call
    )

    # Verify LLM was called with the augmented prompt
    mock_llm_api.assert_awaited_once()
    llm_call_args = mock_llm_api.call_args[1]
    augmented_user_message = llm_call_args["body"]["messages"][0]["content"]
    assert "Please use the following context to answer the question." in augmented_user_message
    assert "Relevant KB content about France." in augmented_user_message  # Content from mock_kb_query
    assert "More details about European capitals." in augmented_user_message
    assert "Tell me about AI" in augmented_user_message  # Original prompt should be in augmented prompt

    # Verify original prompt (not augmented) was saved in chat history
    create_call_args = mock_create_api.call_args[1]
    sent_messages = create_call_args["body"].chat.additional_properties["messages"]
    assert sent_messages[0]["content"] == "Tell me about AI"  # Original prompt


@pytest.mark.asyncio
async def test_chats_continue_success(mocker, sdk_client):
    """Tests the complex workflow of continuing a chat, including optional RAG."""
    chat_id = "existing-chat-123"

    # Test 1: Continue chat without RAG
    # Define initial_chat_data specifically for this test case
    initial_chat_data_no_rag = models.ChatResponse(
        id=chat_id,
        user_id="user1",
        title="Initial Chat (No RAG)",
        chat=models.ChatResponseChat(),
        created_at=1,
        updated_at=1,
        archived=False,
    )
    initial_chat_data_no_rag.chat.additional_properties = {
        "models": ["test-model"],
        "messages": [{"role": "user", "content": "Hello"}],
    }

    mock_get_api = mocker.patch("openwebui.api.chats.get_chat_by_id_api_v1_chats_id_get.asyncio_detailed")
    mock_get_api.return_value = MagicMock(spec=Response, status_code=200, parsed=initial_chat_data_no_rag)

    mock_llm_api = mocker.patch(
        "openwebui.api.chats.generate_chat_completion_openai_chat_completions_post.asyncio_detailed")
    llm_response_data = {"choices": [{"message": {"content": "Hello back!"}}]}
    mock_llm_api.return_value = MagicMock(spec=Response, status_code=200, parsed=llm_response_data)

    mock_update_api = mocker.patch("openwebui.api.chats.update_chat_by_id_api_v1_chats_id_post.asyncio_detailed")
    mock_update_api.return_value = MagicMock(spec=Response, status_code=200, parsed=
    models.ChatResponse(
        id=chat_id, user_id="user1", title="Updated Chat (No RAG)", chat=models.ChatResponseChat(), created_at=1,
        updated_at=2, archived=False
    )
                                             )

    mock_kb_query = mocker.patch(  # Mock it even if not used, to control behavior
        "openwebui.api.knowledge.KnowledgeBaseAPI.query", new_callable=AsyncMock
    )
    mock_kb_query.return_value = []  # Ensure no RAG context for this test

    updated_chat_no_rag = await sdk_client.chats.continue_chat(chat_id=chat_id, prompt="How are you?")
    assert updated_chat_no_rag.title == "Updated Chat (No RAG)"
    mock_get_api.assert_awaited_once_with(id=chat_id, client=sdk_client._client)
    mock_llm_api.assert_awaited_once()  # Should be called
    mock_update_api.assert_awaited_once()  # Should be called
    mock_kb_query.assert_not_awaited()  # Should NOT be called

    # --- Test 2: Continue chat WITH RAG parameters ---
    # Reset and reconfigure mocks for this specific test block
    mock_get_api.reset_mock()
    mock_llm_api.reset_mock()
    mock_update_api.reset_mock()
    mock_kb_query.reset_mock()

    initial_chat_data_with_rag = models.ChatResponse(
        id=chat_id,
        user_id="user1",
        title="Initial Chat (With RAG)",
        chat=models.ChatResponseChat(),
        created_at=1,
        updated_at=1,
        archived=False,
    )
    initial_chat_data_with_rag.chat.additional_properties = {
        "models": ["test-model"],
        "messages": [{"role": "user", "content": "Previous history message from RAG test."}],
    }
    mock_get_api.return_value = MagicMock(spec=Response, status_code=200, parsed=initial_chat_data_with_rag)

    mock_llm_api.return_value = MagicMock(spec=Response, status_code=200,
                                          parsed=llm_response_data)  # Re-use generic LLM response

    mock_update_api.return_value = MagicMock(spec=Response, status_code=200, parsed=
    models.ChatResponse(
        id=chat_id, user_id="user1", title="Updated Chat (With RAG)", chat=models.ChatResponseChat(), created_at=1,
        updated_at=2, archived=False
    )
                                             )

    # Configure KB query to return content for RAG
    mock_kb_query.return_value = [
        {"content": "Relevant KB content for continuation."},
        {"content": "Additional facts for the project."},
    ]

    kb_ids_to_use = ["continuation-kb-1"]
    rag_k_reranker = 2
    rag_hybrid_bm25_weight = 0.5

    updated_chat_with_rag = await sdk_client.chats.continue_chat(
        chat_id=chat_id,
        prompt="Tell me more about the project.",
        kb_ids=kb_ids_to_use,
        k_reranker=rag_k_reranker,
        hybrid_bm25_weight=rag_hybrid_bm25_weight,
    )

    assert updated_chat_with_rag.title == "Updated Chat (With RAG)"  # Verify title updated

    # Verify KnowledgeBaseAPI.query was called correctly
    mock_kb_query.assert_awaited_once_with(
        "Tell me more about the project.",  # Original prompt passed to KB query
        kb_ids_to_use,
        k=None,  # Not set in this call
        k_reranker=rag_k_reranker,
        r=None,  # Not set in this call
        hybrid=None,  # Not set in this call
        hybrid_bm25_weight=rag_hybrid_bm25_weight,
    )

    # Verify LLM was called with the augmented prompt including history and new context
    mock_llm_api.assert_awaited_once()
    llm_call_args = mock_llm_api.call_args[1]

    # The list of messages passed to LLM should include previous history + the new augmented user message
    llm_messages = llm_call_args["body"]["messages"]
    assert len(llm_messages) == 2  # "Previous history message from RAG test." + new augmented prompt

    # Check the content of the previous message
    assert llm_messages[0]["content"] == "Previous history message from RAG test."

    # Check the content of the augmented user message
    augmented_user_message = llm_messages[1]["content"]
    assert "Please use the following context to answer the question." in augmented_user_message
    assert "Relevant KB content for continuation." in augmented_user_message
    assert "Additional facts for the project." in augmented_user_message
    assert "Tell me more about the project." in augmented_user_message

    # Verify the final update call saved the original prompt, not the augmented one
    mock_update_api.assert_awaited_once()
    update_call_args = mock_update_api.call_args[1]
    final_messages = update_call_args["body"].chat.additional_properties["messages"]
    assert len(final_messages) == 2  # Original chat and new message
    assert final_messages[0]["content"] == "Previous history message from RAG test."
    assert final_messages[1]["content"] == "Tell me more about the project."  # Should be original prompt