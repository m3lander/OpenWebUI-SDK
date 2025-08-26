import logging

from .client import OpenWebUI
from .exceptions import APIError, AuthenticationError, ConnectionError, NotFoundError, OpenWebUIError

# Set up a null handler for the library's root logger
# This prevents "No handler found" warnings and allows applications
# using this SDK to configure logging how they see fit.
log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())

# Define what gets imported when a user writes `from openwebui import *`
__all__ = [
    "OpenWebUI",
    "APIError",
    "AuthenticationError",
    "ConnectionError",
    "NotFoundError",
    "OpenWebUIError",
]
