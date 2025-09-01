import logging
import mimetypes
import os
import tqdm
import asyncio
from pathlib import Path
from typing import List, Any, Optional, Dict

import httpx

from ..exceptions import APIError, ConnectionError, NotFoundError
from ..utils.kbignore_parser import KBIgnoreParser  # Assuming this is the correct path after copying
from ..utils.api_utils import handle_api_response  # NEW IMPORT for centralized handler


# --- DIRECT IMPORTS from the generated OpenWebUI API client ---
from ..open_web_ui_client.open_web_ui_client import AuthenticatedClient, models
from ..open_web_ui_client.open_web_ui_client.types import File as OpenAPIGeneratedFile, UNSET

# API function imports (extrapolated from kbmanager.api_interface and likely OpenWebUI structure)
from ..open_web_ui_client.open_web_ui_client.api.knowledge.create_new_knowledge_api_v1_knowledge_create_post import (
    asyncio_detailed as create_kb_api_call,
)
from ..open_web_ui_client.open_web_ui_client.api.knowledge.get_knowledge_list_api_v1_knowledge_list_get import (
    asyncio_detailed as list_kbs_api_call,
)
from ..open_web_ui_client.open_web_ui_client.api.files.upload_file_api_v1_files_post import (
    asyncio_detailed as upload_file_api_call,
)
from ..open_web_ui_client.open_web_ui_client.api.knowledge.add_files_to_knowledge_batch_api_v1_knowledge_id_files_batch_add_post import (
    asyncio_detailed as add_files_to_knowledge_batch_api_call,
)
from ..open_web_ui_client.open_web_ui_client.api.files.delete_file_by_id_api_v1_files_id_delete import (
    asyncio_detailed as delete_file_api_call,
)
from ..open_web_ui_client.open_web_ui_client.api.knowledge.get_knowledge_by_id_api_v1_knowledge_id_get import (
    asyncio_detailed as list_files_for_knowledge_base_api_call,
)
from ..open_web_ui_client.open_web_ui_client.api.knowledge.delete_knowledge_by_id_api_v1_knowledge_id_delete_delete import (
    asyncio_detailed as delete_kb_api_call,
)
from ..open_web_ui_client.open_web_ui_client.api.retrieval.query_collection_handler_api_v1_retrieval_query_collection_post import (
     asyncio_detailed as query_kb_api_call,
)


log = logging.getLogger(__name__)


class KnowledgeBaseAPI:
    """
    Provides high-level asynchronous methods for interacting with the OpenWebUI
    Knowledge Base and File Management APIs.
    """

    def __init__(self, client: AuthenticatedClient):
        """
        Initializes the KnowledgeBaseAPI with an authenticated OpenWebUI client.

        Args:
            client: An instance of the AuthenticatedClient from the generated OpenAPI client.
        """
        self._client = client

    async def create(self, name: str, description: Optional[str] = None) -> models.KnowledgeResponse:
        """
        Creates a new knowledge base in OpenWebUI.

        Args:
            name: The name of the new knowledge base.
            description: An optional description for the knowledge base.

        Returns:
            A KnowledgeBase model object representing the newly created knowledge base.

        Raises:
            ConnectionError: If a network-related issue occurs.
            AuthenticationError: If authentication fails.
            APIError: For other API-related errors.
        """
        log.info(f"Creating knowledge base: '{name}'")
        try:
            kb_form = models.KnowledgeForm(name=name, description=description)
            response = await create_kb_api_call(body=kb_form, client=self._client)
            return handle_api_response(response, "knowledge base")
        except httpx.ConnectError as e:
            raise ConnectionError(f"A network error occurred while creating knowledge base: {e}") from e

    async def delete(self, kb_id: str) -> bool:
        """
        Deletes a knowledge base by its ID.

        Args:
            kb_id: The ID of the knowledge base to delete.

        Returns:
            True if the deletion was successful.

        Raises:
            ConnectionError: If a network-related issue occurs.
            AuthenticationError: If authentication fails.
            NotFoundError: If the knowledge base with kb_id is not found.
            APIError: For other API-related errors.
        """
        log.info(f"Deleting knowledge base with ID: '{kb_id}'.")
        try:
            # Assuming 'delete_kb_api_call' is the imported generated function for this
            response = await delete_kb_api_call(id=kb_id, client=self._client)
            return handle_api_response(response, f"knowledge base deletion for ID {kb_id}")
        except httpx.ConnectError as e:
            raise ConnectionError(f"A network error occurred while deleting knowledge base: {e}") from e

    async def query(
            self,
            query_text: str,
            kb_ids: List[str],
            k: Optional[int] = None,
            k_reranker: Optional[int] = None,
            r: Optional[float] = None,
            hybrid: Optional[bool] = None,
            hybrid_bm25_weight: Optional[float] = None,
    ) -> List[Dict[str, Any]]:  # This return type is still correct conceptually for the final output
        """
        Queries one or more knowledge bases and returns the most relevant text chunks.

        Args:
            query_text: The user's query to search for.
            kb_ids: A list of knowledge base IDs to query.
            k: The number of results to return (top-k).
            k_reranker: The number of results to re-rank (if reranking is used).
            r: The relevance score threshold (0.0 to 1.0).
            hybrid: Whether to use hybrid search (vector + keyword).
            hybrid_bm25_weight: The weight for BM25 in hybrid search (0.0 to 1.0).

        Returns:
            A list of dictionary objects, each representing a retrieved document chunk.
            Each dictionary will typically contain 'content' and 'meta' fields.
        """
        log.info(f"Querying KBs: {kb_ids} with text: '{query_text[:50]}...'")
        try:
            # Construct QueryCollectionsForm dynamically based on provided parameters
            query_form_data = {
                "collection_names": kb_ids,
                "query": query_text,
            }
            if k is not None:
                query_form_data["k"] = k
            if k_reranker is not None:
                query_form_data["k_reranker"] = k_reranker
            if r is not None:
                query_form_data["r"] = r
            if hybrid is not None:
                query_form_data["hybrid"] = hybrid
            if hybrid_bm25_weight is not None:
                query_form_data["hybrid_bm25_weight"] = hybrid_bm25_weight

            query_form = models.QueryCollectionsForm(
                collection_names=query_form_data["collection_names"],
                query=query_form_data["query"],
                k=query_form_data.get("k", UNSET),
                k_reranker=query_form_data.get("k_reranker", UNSET),
                r=query_form_data.get("r", UNSET),
                hybrid=query_form_data.get("hybrid", UNSET),
                hybrid_bm25_weight=query_form_data.get("hybrid_bm25_weight", UNSET),
            )

            response = await query_kb_api_call(client=self._client, body=query_form)
            retrieved_response_dict = handle_api_response(response, f"query on KBs {kb_ids}")

            # --- FIX STARTS HERE ---
            if not isinstance(retrieved_response_dict, dict):
                log.error(
                    f"Expected dict from retrieval API, but received: {type(retrieved_response_dict)}. Raw: {retrieved_response_dict}")
                raise APIError(f"Unexpected retrieval API response type: {type(retrieved_response_dict)}",
                               response.status_code)

            # The actual chunks are in the 'documents' field, and 'metadatas' often stores the corresponding meta
            # Assuming 'documents' is a list of lists, and we want to flatten it and pair with metadata.
            # The structure from your error message: {'distances': [...], 'documents': [[...]], 'metadatas': [[...]]}

            extracted_documents_lists = retrieved_response_dict.get('documents', [])
            extracted_metadatas_lists = retrieved_response_dict.get('metadatas', [])

            # Flatten the lists and pair documents with their metadata
            # Assuming a 1:1 mapping between documents in inner list and their metadatas
            retrieved_chunks = []
            for doc_list, meta_list in zip(extracted_documents_lists, extracted_metadatas_lists):
                for doc_content, meta_data in zip(doc_list, meta_list):
                    retrieved_chunks.append({
                        "content": doc_content,
                        "meta": meta_data  # This could be any relevant metadata
                    })
            # --- FIX ENDS HERE ---

            log.info(f"Retrieved {len(retrieved_chunks)} chunks from KBs: {kb_ids}.")
            log.debug(f"Retrieved chunks: {retrieved_chunks}")
            return retrieved_chunks  # Now returning a List[Dict] as expected by ChatsAPI

        except httpx.ConnectError as e:
            raise ConnectionError(f"A network error occurred while querying KBs '{kb_ids}': {e}") from e

    async def list_all(self) -> List[models.KnowledgeResponse]:
        """
        Lists all available knowledge bases in OpenWebUI.

        Returns:
            A list of KnowledgeBase model objects.

        Raises:
            ConnectionError: If a network-related issue occurs.
            AuthenticationError: If authentication fails.
            APIError: For other API-related errors.
        """
        log.info("Listing all knowledge bases.")
        try:
            response = await list_kbs_api_call(client=self._client)
            raw_kbs_data = handle_api_response(response, "knowledge bases")

            # TODO: #1: API Client Bug/Schema Mismatch
            # get_knowledge_list_api_v1_knowledge_list_get.py response.parsed is always None. Have to return raw json content.
            # handle_api_response will return a List[Dict] (JSON content).
            # This part manually converts those dictionaries to models.KnowledgeResponse objects.
            # This temporary workaround should be removed once the generated client correctly
            # parses the OpenAPI schema for this endpoint to models.KnowledgeResponse.

            if not isinstance(raw_kbs_data, list):
                log.error(
                    f"Expected list of KBs, but received: {type(raw_kbs_data)}. Raw data: {raw_kbs_data}"
                )
                # Re-raise as APIError if the raw data itself is not a list.
                # If raw_kbs_data is a string (e.g. malformed or unexpected content type)
                raise APIError(
                    f"Unexpected API response type for knowledge base list: {type(raw_kbs_data)}",
                    response.status_code,
                )

            kbs: List[models.KnowledgeResponse] = []
            for kb_data in raw_kbs_data:
                # Assuming models.KnowledgeResponse can be instantiated from a dictionary
                # directly matching its attribute names (id, name, description).
                # Adjust if your generated model requires different initialization.
                if isinstance(kb_data, dict):
                    try:
                        # Filter out any unexpected keys that are not part of KnowledgeResponse
                        # See TODO #1 above for context
                        kb_data = {k: v for k, v in kb_data.items() if k in models.KnowledgeResponse.__dict__.keys()}
                        kbs.append(models.KnowledgeResponse(**kb_data))
                    except TypeError as e:
                        log.error(f"Failed to instantiate models.KnowledgeResponse from dict {kb_data}: {e}")
                        raise APIError(
                            f"Malformed KB data received from API for {kb_data.get('id', 'unknown_id')}.",
                            response.status_code,
                        )
                else:
                    log.warning(f"Expected dict for KB entry, but got {type(kb_data)}. Skipping: {kb_data}")
            return kbs
        except httpx.ConnectError as e:
            raise ConnectionError(f"A network error occurred while listing knowledge bases: {e}") from e

    async def upload_file(self, file_path: Path, kb_id: str) -> models.FileModelResponse:
        """
        Uploads a single file to OpenWebUI and associates it with a knowledge base.

        Args:
            file_path: The path to the file to upload.
            kb_id: The ID of the knowledge base to associate the file with.

        Returns:
            A FileModelResponse object representing the uploaded file.

        Raises:
            FileNotFoundError: If the specified file does not exist.
            ConnectionError: If a network-related issue occurs.
            AuthenticationError: If authentication fails.
            APIError: For other API-related errors.
        """
        if not file_path.is_file():
            log.error(f"File not found: {file_path}")
            raise FileNotFoundError(f"File not found: {file_path}")

        log.info(f"Uploading file '{file_path.name}' to knowledge base '{kb_id}'.")
        try:
            # Read file content
            file_content_bytes = file_path.read_bytes()

            # Guess MIME type
            mime_type, _ = mimetypes.guess_type(str(file_path))
            if mime_type is None:
                mime_type = "application/octet-stream"  # Default MIME type

            # Create the OpenAPI generated file object
            # Assumed model name is `models.File` from `open_web_ui_client.models`
            generated_file_object = OpenAPIGeneratedFile(
                file_name=file_path.name, payload=file_content_bytes, mime_type=mime_type
            )

            # --- FIX: Removed 'process' and 'internal' from constructor ---
            # They are likely direct arguments to the api call, not part of the body model
            upload_request_body = models.BodyUploadFileApiV1FilesPost(
                file=generated_file_object,
            )

            response = await upload_file_api_call(
                client=self._client,
                body=upload_request_body,
            )
            # handle_api_response will return `response.parsed` which should be models.FileModelResponse
            uploaded_file = handle_api_response(response, "file upload")

            # After successful upload, associate the file with the KB (batch add for simplicity)
            # Assumed models: `models.KnowledgeFileIdForm`
            log.info(f"Associating uploaded file '{uploaded_file.id}' with KB '{kb_id}'.")
            batch_add_payload = [models.KnowledgeFileIdForm(file_id=uploaded_file.id)]
            batch_response = await add_files_to_knowledge_batch_api_call(
                id=kb_id,  # Assumed 'id' parameter for KB ID
                body=batch_add_payload,
                client=self._client,
            )
            handle_api_response(
                batch_response, "file association with KB"
            )  # Just check for success, no return needed

            log.info(
                f"Successfully uploaded and associated '{file_path.name}' (ID: {uploaded_file.id}) with KB '{kb_id}'."
            )
            return uploaded_file
        except httpx.ConnectError as e:
            raise ConnectionError(f"A network error occurred during file upload: {e}") from e

    async def upload_directory(
        self, directory_path: Path, kb_id: str, kbignore_file_path: Optional[Path] = None
    ) -> List[models.FileModelResponse]:
        """
        Uploads all files from a directory to a knowledge base, respecting .kbignore rules.

        Args:
            directory_path: The path to the directory to upload.
            kb_id: The ID of the knowledge base to upload files to.
            kbignore_file_path: Optional path to a custom .kbignore file. If None,
                                 it looks for .kbignore in the directory_path.

        Returns:
            A list of FileModelResponse objects for successfully uploaded files.

        Raises:
            NotADirectoryError: If directory_path is not a valid directory.
            ConnectionError: If a network-related issue occurs.
            AuthenticationError: If authentication fails.
            APIError: For other API-related errors.
        """
        if not directory_path.is_dir():
            log.error(f"Directory not found: {directory_path}")
            raise NotADirectoryError(f"Directory not found: {directory_path}")

        log.info(f"Scanning directory '{directory_path}' for upload to KB '{kb_id}'.")
        kbignore_parser = KBIgnoreParser()
        effective_kbignore_path = None

        if kbignore_file_path and kbignore_file_path.is_file():
            effective_kbignore_path = kbignore_file_path
        else:
            default_kbignore = directory_path / ".kbignore"
            if default_kbignore.is_file():
                effective_kbignore_path = default_kbignore

        if effective_kbignore_path:
            kbignore_parser.load_patterns(effective_kbignore_path)
            log.info(f"Loaded .kbignore patterns from '{effective_kbignore_path}'.")
        else:
            log.debug("No .kbignore file found or specified; proceeding without ignore rules.")

        files_to_upload: List[Path] = []
        for root, _, files_in_dir in os.walk(directory_path):
            current_dir_path = Path(root)
            for file_name in files_in_dir:
                full_file_path = current_dir_path / file_name
                relative_file_path = full_file_path.relative_to(directory_path)

                # FIX: Exclude .kbignore file itself from being uploaded
                if full_file_path == effective_kbignore_path:
                    log.debug(f"Skipping .kbignore file itself: '{full_file_path}'")
                    continue

                # Use posixpath for consistency with gitignore-style matching
                if not kbignore_parser.is_ignored(f"{relative_file_path}".replace(os.sep, "/")):
                    files_to_upload.append(full_file_path)
                else:
                    log.debug(f"Skipping ignored file: '{relative_file_path}'")

        if not files_to_upload:
            log.info(f"No files found in '{directory_path}' after applying ignore rules. Nothing to upload.")
            return []

        log.info(f"Identified {len(files_to_upload)} files for upload from '{directory_path}'.")

        uploaded_files: List[models.FileModelResponse] = []
        uploaded_file_ids: List[str] = []
        failed_uploads_count = 0

        with tqdm.tqdm(
            total=len(files_to_upload), desc="Overall Upload Progress", unit="file", ncols=100
        ) as pbar:
            tasks = [self._upload_single_file_for_batch(file_path) for file_path in files_to_upload]
            for future in asyncio.as_completed(tasks):
                try:
                    uploaded_file = await future
                    uploaded_files.append(uploaded_file)
                    uploaded_file_ids.append(uploaded_file.id)
                    log.debug(f"Successfully uploaded: '{uploaded_file.filename}' (ID: {uploaded_file.id})")
                except Exception as e:
                    failed_uploads_count += 1
                    # Log the error, but try to continue with other files
                    log.error(f"Failed to upload a file in batch: {e}")
                finally:
                    pbar.update(1)

        if not uploaded_files:
            log.warning("No files were successfully uploaded from the directory.")
            if failed_uploads_count > 0:
                raise APIError(
                    f"All files failed to upload. {failed_uploads_count} errors occurred during batch upload.",
                    0,
                )
            return []

        log.info(f"Successfully uploaded {len(uploaded_files)} files. Linking to KB '{kb_id}'.")

        try:
            batch_add_payload = [models.KnowledgeFileIdForm(file_id=file_id) for file_id in uploaded_file_ids]
            batch_response = await add_files_to_knowledge_batch_api_call(
                id=kb_id, body=batch_add_payload, client=self._client
            )
            handle_api_response(batch_response, f"{len(uploaded_file_ids)} files batch association with KB")
            log.info(f"Successfully linked {len(uploaded_file_ids)} files to KB '{kb_id}'.")
        except httpx.ConnectError as e:
            raise ConnectionError(f"A network error occurred while linking files to KB: {e}") from e
        except Exception as e:
            log.error(f"Failed to link all successfully uploaded files to KB '{kb_id}': {e}")
            raise APIError(
                f"Failed to link uploaded files to KB '{kb_id}': {e}", 0
            )  # Use 0 or appropriate unknown code

        return uploaded_files

    async def _upload_single_file_for_batch(self, file_path: Path) -> models.FileModelResponse:
        """
        Helper method to upload a single file, used internally for batch uploads.
        Does not associate with KB, that is handled by the caller.
        """
        log.debug(f"Initiating single file upload for '{file_path.name}'.")
        try:
            file_content_bytes = file_path.read_bytes()
            mime_type, _ = mimetypes.guess_type(str(file_path))
            if mime_type is None:
                mime_type = "application/octet-stream"

            generated_file_object = OpenAPIGeneratedFile(
                file_name=file_path.name, payload=file_content_bytes, mime_type=mime_type
            )

            upload_request_body = models.BodyUploadFileApiV1FilesPost(
                file=generated_file_object,
            )

            response = await upload_file_api_call(
                client=self._client,
                body=upload_request_body,
            )
            uploaded_file = handle_api_response(response, f"single file upload: {file_path.name}")
            log.debug(f"Completed single file upload for '{file_path.name}'.")
            return uploaded_file
        except httpx.ConnectError as e:
            raise ConnectionError(f"Network error on upload of '{file_path.name}': {e}") from e
        except Exception as e:
            log.error(f"Unexpected error during single file upload of '{file_path.name}': {e}")
            raise APIError(f"Single file upload failed for '{file_path.name}': {e}", 0)

    async def delete_file(self, file_id: str) -> bool:
        """
        Deletes a single file from OpenWebUI by its file ID.

        Args:
            file_id: The ID of the file to delete.

        Returns:
            True if the deletion was successful.

        Raises:
            ConnectionError: If a network-related issue occurs.
            AuthenticationError: If authentication fails.
            NotFoundError: If the file with file_id is not found.
            APIError: For other API-related errors.
        """
        log.info(f"Deleting file with ID: '{file_id}'.")
        try:
            response = await delete_file_api_call(id=file_id, client=self._client)
            # handle_api_response will return True for successful deletes
            handle_api_response(response, f"file deletion for ID {file_id}")
            return True
        except httpx.ConnectError as e:
            raise ConnectionError(f"A network error occurred while deleting file: {e}") from e

    async def delete_all_files_from_kb(self, kb_id: str) -> Dict[str, Any]:
        """
        Deletes all files associated with a specific knowledge base ID.
        This operation lists all files in the KB and then deletes them individually.

        Args:
            kb_id: The ID of the knowledge base from which to delete all files.

        Returns:
            A dictionary containing counts of successful and failed deletions.

        Raises:
            ConnectionError: If a network-related issue occurs.
            AuthenticationError: If authentication fails.
            NotFoundError: If the knowledge base is not found.
            APIError: For other API-related errors.
        """
        log.info(f"Initiating deletion of all files from Knowledge Base ID: '{kb_id}'.")
        try:
            files_to_delete = await self.list_files(kb_id=kb_id)
        except NotFoundError:  # Catch case where KB doesn't exist
            raise NotFoundError(f"Knowledge Base with ID '{kb_id}' not found.")
        except Exception as e:  # Catch other errors during listing
            log.error(f"Failed to list files for KB '{kb_id}' prior to mass deletion: {e}")
            raise APIError(f"Failed to prepare file list for deletion in KB '{kb_id}': {e}", 0)

        if not files_to_delete:
            log.info(f"No files found in Knowledge Base '{kb_id}'. Nothing to delete.")
            return {"successful": 0, "failed": 0}

        log.info(f"Found {len(files_to_delete)} files to delete from KB '{kb_id}'.")
        delete_tasks = [self.delete_file(file.id) for file in files_to_delete]

        successful_deletes = 0
        failed_deletes = 0

        import tqdm  # Assuming tqdm is installed via dependencies
        import asyncio  # Assuming asyncio is available

        with tqdm.tqdm(total=len(delete_tasks), desc="Deleting Files", unit="file", ncols=100) as pbar:
            for future in asyncio.as_completed(delete_tasks):
                try:
                    await future
                    successful_deletes += 1
                except Exception as e:
                    # Log individual file deletion failures but continue processing others
                    log.warning(f"Failed to delete a file during batch operation: {e}")
                    failed_deletes += 1
                finally:
                    pbar.update(1)

        log.info(
            f"Completed batch deletion for KB '{kb_id}'. Successful: {successful_deletes}, Failed: {failed_deletes}."
        )
        return {"successful": successful_deletes, "failed": failed_deletes}

    async def list_files(self, kb_id: str) -> List[models.FileMetadataResponse]:
        """
        Lists files for a specific knowledge base, with optional client-side filtering.

        Args:
            kb_id: The ID of the knowledge base to list files from.

        Returns:
            A list of FileMetadataResponse objects within the specified knowledge base.

        Raises:
            ConnectionError: If a network-related issue occurs.
            AuthenticationError: If authentication fails.
            NotFoundError: If the knowledge base is not found.
            APIError: For other API-related errors.
        """
        log.info(f"Listing files for KB ID: '{kb_id}'.")
        try:
            response = await list_files_for_knowledge_base_api_call(id=kb_id, client=self._client)
            parsed_response = handle_api_response(response, f"files for KB {kb_id}")

            if hasattr(parsed_response, "files") and isinstance(parsed_response.files, list):
                files = [
                    f_item
                    if isinstance(f_item, models.FileMetadataResponse)
                    else models.FileMetadataResponse(**f_item)
                    if isinstance(f_item, dict)
                    else f_item  # Should ideally not hit this 'else'
                    for f_item in parsed_response.files
                ]
            else:
                log.warning(
                    f"Unexpected structure in KnowledgeFilesResponse for KB '{kb_id}'. Expected 'files' list. Value: {parsed_response}. Assuming empty list."
                )
                files = []

            return files
        except httpx.ConnectError as e:
            raise ConnectionError(
                f"A network error occurred while listing files for KB '{kb_id}': {e}"
            ) from e
