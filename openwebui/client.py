import logging
from typing import Optional
from .config import get_config, Config
from .exceptions import OpenWebUIError
from .api.folders import FoldersAPI
from .api.chats import ChatsAPI
from .api.knowledge import KnowledgeBaseAPI

# Import the necessary low-level client from the generated code
from .open_web_ui_client.open_web_ui_client import AuthenticatedClient

log = logging.getLogger(__name__)


class OpenWebUI:
    """
    The main async client for interacting with the Open WebUI API.
    It manages authentication and provides access to API resource groups.
    """

    folders: FoldersAPI
    chats: ChatsAPI
    knowledge: KnowledgeBaseAPI
    _client: AuthenticatedClient

    def __init__(
        self,
        config: Optional[Config] = None,
        base_url: Optional[str] = None,
        api_key: Optional[str] = None,
        timeout: int = 30,
    ):
        """Initializes the OpenWebUI client."""
        log.debug("Initializing OpenWebUI client.")
        if config is None:
            try:
                effective_config = get_config()
                base_url = base_url or effective_config.server_url
                api_key = api_key or effective_config.api_key
                log.debug("Loaded configuration from environment.")

            except ValueError as e:
                raise OpenWebUIError(f"Configuration failed: {e}") from e
        else:
            base_url = base_url or config.server_url
            api_key = api_key or config.api_key

        if not base_url or not api_key:
            raise OpenWebUIError("Client must be configured with base_url and api_key.")

        log.info(f"Client configured for server: {base_url}")

        self._client = AuthenticatedClient(
            base_url=base_url,
            token=api_key,
            timeout=timeout,
        )

        self.folders = FoldersAPI(self._client)
        self.chats = ChatsAPI(self._client)
        self.knowledge = KnowledgeBaseAPI(self._client)

    async def __aenter__(self):
        log.debug("Entering async context.")
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        log.debug("Exiting async context.")
        await self.aclose()

    async def aclose(self):
        """Cleanly close the underlying HTTPX client."""
        log.info("Closing client connection.")
        await self._client.get_async_httpx_client().aclose()
