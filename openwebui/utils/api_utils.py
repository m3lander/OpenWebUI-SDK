import logging
import json
from typing import Any

from httpx import Response

from ..exceptions import APIError, AuthenticationError, NotFoundError

log = logging.getLogger(__name__)


def handle_api_response(response: Response, resource_name: str = "resource") -> Any:
    """
    A centralized utility function to handle API responses, including error parsing and
    raising appropriate SDK-specific exceptions.

    Includes a temporary patch to return raw content if parsing fails but content is present.

    Args:
        response: The raw response object from the generated OpenAPI client.
        resource_name: A descriptive name for the resource being operated on,
                       used in error messages (e.g., "folder", "chat", "file", "knowledge base").

    Returns:
        The parsed data from the response, or raw content (str/dict) if parsing failed.

    Raises:
        AuthenticationError: If the API returns a 401 Unauthorized status.
        NotFoundError: If the API returns a 404 Not Found status.
        APIError: For other 4xx or 5xx status codes, or unparseable responses.
    """
    log.debug(f"Received API response for {resource_name}: Status {response.status_code}")

    if 200 <= response.status_code < 300:
        log.debug(f"Request for {resource_name} successful.")

        # Case 1: Officially No Content (204)
        if response.status_code == 204:
            return True

        # Case 2: Parsed content is valid
        if response.parsed is not None:
            return response.parsed

        # Case 3: Parsing failed (response.parsed is None) but content IS present (e.g., JSON)
        # This is the temporary patch for generated client parsing issues.
        if response.content is not None and len(response.content) > 0:
            log.info(
                f"API parsing for {resource_name} failed (response.parsed is None) "
                f"but raw content is present. Returning raw content."
            )
            try:
                # Attempt to decode as JSON if content-type suggests it
                if "application/json" in response.headers.get("content-type", ""):
                    return json.loads(response.content.decode("utf-8", errors="ignore"))
                return json.loads(response.content.decode("utf-8", errors="ignore"))  # Fallback to raw string
            except json.JSONDecodeError:
                log.warning(f"Could not JSON decode raw content for {resource_name}.")
                return response.content.decode("utf-8", errors="ignore")  # Fallback to raw string

        # Case 4: No parsed content and no raw content (or empty raw content for 2xx)
        if response.parsed is None and (response.content is None or len(response.content) == 0):
            # This could be acceptable for some 2xx (e.g., 200 OK after update that returns no body)
            # but might also indicate missing expected content.
            log.warning(
                f"No parsed content and no raw content for {resource_name}. Status {response.status_code}."
            )
            return True  # Assume success if no error code and no content.

    # --- Error Handling ---
    elif response.status_code == 401:
        log.error("Authentication failed. Check your API key.")
        raise AuthenticationError("Invalid or missing API key.")
    elif response.status_code == 404:
        log.warning("Resource not found.")
        raise NotFoundError("The requested resource was not found.")
    else:  # General 4xx or 5xx error
        error_message = response.content.decode("utf-8", errors="ignore")
        # Enhance error message for validation errors
        if response.status_code == 422:
            try:
                error_details = json.loads(error_message)
                if isinstance(error_details, dict) and "detail" in error_details:
                    details = error_details["detail"]
                    if isinstance(details, list):
                        detail_str = "; ".join([f"{d.get('loc', [])}: {d.get('msg')}" for d in details])
                        error_message = f"Validation Error (422): {detail_str}"
            except json.JSONDecodeError:
                pass  # Not a JSON error, use raw message for 422

        log.error(f"API Error {response.status_code}: {error_message}")
        raise APIError(
            message=f"Received unexpected status code: {response.status_code} for {resource_name}: {error_message}",
            status_code=response.status_code,
        )
