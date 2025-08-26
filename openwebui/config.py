import os
from typing import Optional, Dict, Any
from dataclasses import dataclass

# Import PyYAML
import yaml
from dotenv import load_dotenv  # Still used for loading env vars for highest precedence

# Paths for configuration files
DEFAULT_USER_CONFIG_PATH = os.path.expanduser("~/.owui/config.yaml")
LOCAL_PROJECT_CONFIG_PATH = ".owui/config.yaml"

# Load environment variables first (they have highest precedence)
load_dotenv()


@dataclass(frozen=True)
class Config:
    """
    Holds the configuration for the OpenWebUI client.

    This class provides a structured, read-only format for settings like
    server URL and API key.
    """

    server_url: str
    api_key: str


def _load_yaml_config() -> Dict[str, Any]:
    """
    Attempts to load configuration from YAML files in predefined locations.

    Loads from DEFAULT_USER_CONFIG_PATH first, then LOCAL_PROJECT_CONFIG_PATH,
    allowing the local project config to override user-level config.

    Returns:
        Dict[str, Any]: A dictionary containing loaded YAML configuration.

    Raises:
        ValueError: If a YAML file is found but cannot be parsed.
    """
    config_data = {}

    # Load from user's home directory
    if os.path.exists(DEFAULT_USER_CONFIG_PATH):
        try:
            with open(DEFAULT_USER_CONFIG_PATH, "r") as f:
                loaded_yaml = yaml.safe_load(f)
                if isinstance(loaded_yaml, dict):  # Ensure root is a dict
                    config_data.update(loaded_yaml)
        except yaml.YAMLError as e:
            raise ValueError(f"Error parsing YAML config file '{DEFAULT_USER_CONFIG_PATH}': {e}")
        except OSError as e:
            raise ValueError(f"Error reading YAML config file '{DEFAULT_USER_CONFIG_PATH}': {e}")

    # Load from local project directory (overrides user config)
    if os.path.exists(LOCAL_PROJECT_CONFIG_PATH):
        try:
            with open(LOCAL_PROJECT_CONFIG_PATH, "r") as f:
                loaded_yaml = yaml.safe_load(f)
                if isinstance(loaded_yaml, dict):  # Ensure root is a dict
                    config_data.update(loaded_yaml)
        except yaml.YAMLError as e:
            raise ValueError(f"Error parsing YAML config file '{LOCAL_PROJECT_CONFIG_PATH}': {e}")
        except OSError as e:
            raise ValueError(f"Error reading YAML config file '{LOCAL_PROJECT_CONFIG_PATH}': {e}")

    return config_data


def get_config() -> Config:
    """
    Loads and validates configuration from multiple sources with defined precedence.

    Precedence (highest to lowest):
    1. Environment variables (e.g., OPENWEBUI_URL, OPENWEBUI_API_KEY)
    2. Local project config file (`.owui/config.yaml`)
    3. User-level config file (`~/.owui/config.yaml`)

    Returns:
        Config: A validated configuration object.

    Raises:
        ValueError: If server URL or API key is not found in any source.
    """
    # 1. Load from YAML files
    yaml_config = _load_yaml_config()

    # 2. Get values from environment variables (highest precedence)
    server_url: Optional[str] = os.getenv("OPENWEBUI_URL")
    api_key: Optional[str] = os.getenv("OPENWEBUI_API_KEY")

    # 3. If not found in env, try YAML config
    if not server_url:
        server_url = yaml_config.get("server", {}).get("url")
    if not api_key:
        api_key = yaml_config.get("server", {}).get("api_key")

    # Basic validation
    if not server_url:
        raise ValueError(
            "Configuration error: Open WebUI server URL is not configured. "
            "Please set OPENWEBUI_URL environment variable or 'server.url' in ~/.owui/config.yaml or ./.owui/config.yaml."
        )

    if not api_key:
        raise ValueError(
            "Configuration error: Open WebUI API key is not configured. "
            "Please set OPENWEBUI_API_KEY environment variable or 'server.api_key' in ~/.owui/config.yaml or ./.owui/config.yaml."
        )

    # Ensure the URL doesn't have a trailing slash for consistency
    return Config(server_url=server_url.rstrip("/"), api_key=api_key)


# A default config instance that can be imported and used by the SDK.
# This raises an error on import if the config is not set, a "fail-fast" approach.
# However, the SDK OpenWebUI().__init__ will also call get_config,
# allowing for more granular error handling at runtime if desired.
try:
    default_config = get_config()
except ValueError:
    default_config = None  # Allows SDK to be imported even if config is absent initially
