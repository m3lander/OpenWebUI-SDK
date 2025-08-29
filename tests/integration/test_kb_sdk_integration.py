import pytest
import asyncio  # Import asyncio for sleep

from openwebui.exceptions import NotFoundError

# Import generated models for type hinting and up

# Mark all tests in this file as async
pytestmark = pytest.mark.asyncio


# Using the sdk_live_client fixture from conftest.py


@pytest.mark.xfail(reason="Known asyncio loop closed error during httpx client teardown", strict=False)
@pytest.mark.skip(reason="Needs a live server with LLMs configured")
async def test_full_knowledge_base_workflow(sdk_live_client, test_kb_id, tmp_path):
    """
    Tests the full lifecycle of knowledge base management:
    Create KB (via fixture), Upload files, List files, Update file, Delete files.
    """
    kb_id = test_kb_id

    # Create dummy files for testing throughout the workflow
    dummy_file_1 = tmp_path / "document_for_kb_1.txt"
    dummy_file_1.write_text("This is an initial test document.\nIt has a second line.")

    dummy_file_2_from_dir = tmp_path / "another_file_for_dir.pdf"  # Used in directory upload
    dummy_file_2_from_dir.write_text("PDF content placeholder for directory upload.")

    updated_dummy_file_1_content = tmp_path / "document_for_kb_1_updated_content.txt"
    updated_dummy_file_1_content.write_text("This test document is updated now with new info.")

    uploaded_file_ids_in_test = []  # Track IDs uploaded within this test for precise cleanup

    try:
        print(f"\n--- Testing workflow for Knowledge Base ID: {kb_id} ---")

        # 1. Upload a single file
        print(f"Uploading file: {dummy_file_1.name} to KB '{kb_id}'...")
        uploaded_file_1 = await sdk_live_client.knowledge.upload_file(dummy_file_1, kb_id)
        assert uploaded_file_1 is not None
        # Handle the raw dict fallback if necessary for initial check
        uploaded_file_1_id = (
            uploaded_file_1.id if hasattr(uploaded_file_1, "id") else uploaded_file_1.get("id")
        )
        uploaded_file_1_filename = (
            uploaded_file_1.filename
            if hasattr(uploaded_file_1, "filename")
            else uploaded_file_1.get("filename")
        )

        assert uploaded_file_1_id is not None
        assert uploaded_file_1_filename == dummy_file_1.name
        uploaded_file_ids_in_test.append(uploaded_file_1_id)
        print(f"Uploaded {dummy_file_1.name} (ID: {uploaded_file_1_id})")
        await asyncio.sleep(7)  # Added delay after single file upload

        # 2. Upload a directory
        print(f"Uploading directory: {tmp_path.name} to KB '{kb_id}'...")

        # Create a subdirectory within tmp_path for the directory upload test
        sub_dir = tmp_path / "test_subdir"
        sub_dir.mkdir(exist_ok=True)  # Ensure it exists for Path operations
        sub_file_1 = sub_dir / "sub_doc.txt"
        sub_file_1.write_text("Content in sub_doc.")

        # Move dummy_file_2_from_dir into tmp_path to ensure it's picked up by upload_directory
        dummy_file_2_from_dir.rename(tmp_path / dummy_file_2_from_dir.name)

        # Create a temporary .kbignore file for the test
        _kbignore_file = tmp_path / ".kbignore"
        _kbignore_file.write_text("*.pdf\n")  # Ignore pdfs for this test, so dummy_file_2_from_dir is ignored

        uploaded_files_from_dir = await sdk_live_client.knowledge.upload_directory(
            tmp_path, kb_id, _kbignore_file
        )

        assert uploaded_files_from_dir is not None

        # Find sub_doc.txt in the uploaded files
        uploaded_sub_doc = next(
            (
                f
                for f in uploaded_files_from_dir
                if (hasattr(f, "filename") and f.filename == sub_file_1.name)
                or (isinstance(f, dict) and f.get("filename") == sub_file_1.name)
            ),
            None,
        )
        assert uploaded_sub_doc is not None
        uploaded_sub_doc_id = (
            uploaded_sub_doc.id if hasattr(uploaded_sub_doc, "id") else uploaded_sub_doc.get("id")
        )
        uploaded_file_ids_in_test.append(uploaded_sub_doc_id)
        print(f"Uploaded {sub_file_1.name} (ID: {uploaded_sub_doc_id}) from directory.")
        await asyncio.sleep(7)  # Added delay after directory upload

        # 3. List files in the KB to confirm uploads + optional search
        print(f"Listing files in KB '{kb_id}'...")
        all_files_in_kb = await sdk_live_client.knowledge.list_files(kb_id)

        print(f"Found {len(all_files_in_kb)} files in KB:")
        for f in all_files_in_kb:
            # Accessing properties safely for printing, accounting for potential dict vs model
            file_id = f.id if hasattr(f, "id") else f.get("id", "N/A_ID")
            filename = (
                f.meta.get("name", "N/A")
                if isinstance(f.meta, dict)
                else (f.meta.name if hasattr(f.meta, "name") else "N/A_Filename")
            )
            print(f"  - ID: {file_id}, Filename: {filename}")

        # More verbose assertion for debugging
        print(f"\n--- Verifying uploaded file 1 ID: {uploaded_file_1_id} ---")
        found_file_1 = False
        for f in all_files_in_kb:
            current_file_id = f.id if hasattr(f, "id") else f.get("id")
            if current_file_id == uploaded_file_1_id:
                found_file_1 = True
                print(f"DEBUG: Found {uploaded_file_1_id} in {current_file_id}")
                break

        print(f"--- Verifying uploaded sub_doc ID: {uploaded_sub_doc_id} ---")
        found_sub_doc = False
        for f in all_files_in_kb:
            current_file_id = f.id if hasattr(f, "id") else f.get("id")
            if current_file_id == uploaded_sub_doc_id:
                found_sub_doc = True
                print(f"DEBUG: Found {uploaded_sub_doc_id} in {current_file_id}")
                break

        assert found_file_1, f"File {uploaded_file_1_id} not found in KB list."
        assert found_sub_doc, f"File {uploaded_sub_doc_id} not found in KB list."
        assert len(all_files_in_kb) >= 2, f"Expected at least 2 files, found {len(all_files_in_kb)}"

        # # Test listing with search
        # searched_files = await sdk_live_client.knowledge.list_files(kb_id, search_query="document")
        # # Assert that the directly uploaded document is found by search
        # assert any(f.id == uploaded_file_1_id for f in searched_files if hasattr(f, 'id')) or any(
        #     f.get('id') == uploaded_file_1_id for f in searched_files if isinstance(f, dict)), \
        #     f"Searched document {uploaded_file_1_id} not found in search results."
        # # Assert that all files in search results contain "document" in their name (case-insensitive)
        # assert all((f.meta.get("name", "").lower().find("document") != -1) if isinstance(f.meta, dict) else (
        #     f.meta.name.lower().find("document") != -1 if hasattr(f.meta, 'name') else False) for f in searched_files), \
        #     "Not all files in search results contain 'document'."

        # # 4. Update a file's content
        # print(f"Updating file '{uploaded_file_1_id}' content...")
        # updated_file_1 = await sdk_live_client.knowledge.update_file(uploaded_file_1_id, updated_dummy_file_1_content)
        # assert updated_file_1 is not None
        # assert (updated_file_1.id if hasattr(updated_file_1, 'id') else updated_file_1.get('id')) == uploaded_file_1_id
        # assert (updated_file_1.filename if hasattr(updated_file_1, 'filename') else updated_file_1.get(
        #     'filename')) == updated_dummy_file_1_content.name
        # print(f"File {uploaded_file_1_id} updated with new content.")
        # await asyncio.sleep(7)  # Added delay after update

    except Exception as e:
        pytest.fail(f"Knowledge Base workflow failed: {e}")
    finally:
        # 5. Delete specific uploaded files that were tracked by this test
        for file_id in uploaded_file_ids_in_test:
            if file_id:
                print(f"Deleting test-specific uploaded file: {file_id}...")
                try:
                    delete_success = await sdk_live_client.knowledge.delete_file(file_id)
                    assert delete_success is True
                    print(f"File {file_id} deleted successfully.")
                except NotFoundError:
                    print(f"File {file_id} already deleted (or not found) during cleanup.")
                except Exception as e:
                    print(f"Warning: Could not delete file {file_id} during specific cleanup: {e}")

        # Remaining general cleanup (delete all files in KB and then the KB) is handled by the test_kb_id fixture.
        print(f"Fixture will now delete any remaining files and KB: {kb_id}")
