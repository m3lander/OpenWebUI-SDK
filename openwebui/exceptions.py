class OpenWebUIError(Exception):
    """
    Base exception class for all errors raised by the OpenWebUI SDK.

    This allows users to catch any error originating from this library
    with a single `except OpenWebUIError:` block.
    """

    pass


class APIError(OpenWebUIError):
    """
    Raised when the API returns an error response (e.g., status 4xx or 5xx).

    Attributes:
        status_code (int): The HTTP status code of the error response.
        message (str): The error message from the API response body.
    """

    def __init__(self, message: str, status_code: int):
        self.status_code = status_code
        super().__init__(f"API Error {status_code}: {message}")


class AuthenticationError(APIError):
    """
    A specific type of APIError raised for authentication failures (status 401).

    This indicates that the provided API key is invalid, missing, or has expired.
    """

    def __init__(self, message: str = "Invalid or missing API key."):
        super().__init__(message, status_code=401)


class NotFoundError(APIError):
    """
    A specific type of APIError raised when a requested resource is not found (status 404).
    """

    def __init__(self, resource: str):
        message = f"The requested resource '{resource}' was not found."
        super().__init__(message, status_code=404)


class ConnectionError(OpenWebUIError):
    """
    Raised for network-related issues, such as a failure to connect to the server.

    This typically wraps a lower-level exception from the HTTP client (e.g., httpx).
    """

    pass
