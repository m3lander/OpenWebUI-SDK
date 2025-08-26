# OpenWebUI-SDK

A modern, asynchronous Python SDK and Command-Line Interface (`owui`) for interacting with your Open WebUI instance.

This project provides a unified, Pythonic interface to manage chats, folders, and interact with Large Language Models (LLMs) served by Open WebUI, following a structured, layered design. It is built to be both programmatically flexible for developers and easy to use from the terminal for end-users.

[//]: # ([![PyPI Version]&#40;https://img.shields.io/pypi/v/openwebui-sdk.svg?style=for-the-badge&#41;]&#40;https://pypi.org/project/openwebui-sdk/&#41;)

[//]: # ([![Python Versions]&#40;https://img.shields.io/pypi/pyversions/openwebui-sdk.svg?style=for-the-badge&#41;]&#40;https://pypi.org/project/openwebui-sdk/&#41;)

[//]: # ([![License]&#40;https://img.shields.io/pypi/l/openwebui-sdk.svg?style=for-the-badge&#41;]&#40;https://github.com/HermanHaggerty/OpenWebUI-LLM-CLI/blob/main/LICENSE&#41;)

[//]: # ([![CI Tests]&#40;https://img.shields.io/github/actions/workflow/status/HermanHaggerty/OpenWebUI-LLM-CLI/test.yml?branch=main&label=tests&style=for-the-badge&#41;]&#40;https://github.com/HermanHaggerty/OpenWebUI-LLM-CLI/actions/workflows/test.yml&#41;)

[//]: # ([![Code Coverage]&#40;https://img.shields.io/codecov/c/github/HermanHaggerty/OpenWebUI-LLM-CLI?style=for-the-badge&#41;]&#40;https://codecov.io/gh/HermanHaggerty/OpenWebUI-LLM-CLI&#41;)

[//]: # ([![Code style: ruff]&#40;https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json&style=for-the-badge&#41;]&#40;https://github.com/astral-sh/ruff&#41;)

---

## 🚀 Features

*   **Asynchronous First SDK:** A clean, `asyncio`-native Python library (`openwebui`) for high-performance, concurrent interaction.
*   **Intuitive CLI:** A powerful command-line tool (`owui`) built with `click` for easy management of chats and folders directly from your terminal.
*   **Complex Workflow Abstraction:** Simplifies multi-step API interactions (e.g., creating a new chat with an initial LLM response) into single, intuitive SDK methods.
*   **Hierarchical YAML Configuration:** Loads configuration from `~/.owui/config.yaml` or a local `.owui/config.yaml`, with environment variables for overrides.
*   **Robust Error Handling:** Provides custom exceptions like `AuthenticationError` and `NotFoundError` for predictable error handling in your applications.
*   **Integrated Logging:** Detailed logging controllable via CLI flags (`--verbose`, `--debug`) for easy debugging and visibility.
*   **Type-Safe API Interaction:** Uses an auto-generated low-level client from the OpenWebUI OpenAPI schema to ensure type safety and maintainability.
*   **Comprehensive Test Suite:** Includes unit tests, integration tests, and CLI tests to ensure reliability.

---

## 📦 Installation

It is recommended to install `openwebui-sdk` in a virtual environment.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/HermanHaggerty/OpenWebUI-LLM-CLI.git # Replace with your actual repo URL
    cd OpenWebUI-LLM-CLI
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install the package in editable mode with development dependencies:**
    This allows you to run the `owui` CLI directly and makes development easier. This project uses `uv` for package management, but `pip` will also work.

    ```bash
    # Using uv (recommended)
    uv pip install -e ".[dev]"
    
    # Or using pip
    pip install -e ".[dev]"
    ```
---

## ⚙️ Configuration

The SDK and CLI load configuration from YAML files with environment variables taking highest precedence.

**1. Create the configuration directory:**
```bash
mkdir -p ~/.owui
```

**2. Create a `config.yaml` file:**
Create `~/.owui/config.yaml` and add your server details.

```yaml
# ~/.owui/config.yaml

server:
  url: "http://your-openwebui-instance:8080"
  api_key: "sk-YOUR_API_KEY_HERE"
```

*   **`url`**: The full URL to your Open WebUI instance. **Important:** Ensure the scheme (`http://` or `https://`) matches your server's setup to avoid SSL errors.
*   **`api_key`**: Your API key obtained from your Open WebUI settings (`Settings` -> `Account`).

**Precedence Order:**
1.  Environment Variables (`OPENWEBUI_URL`, `OPENWEBUI_API_KEY`)
2.  Local Project Config (`./.owui/config.yaml`)
3.  User-level Config (`~/.owui/config.yaml`)

---

## 💡 Usage

### Command-Line Interface (`owui`)

The CLI provides commands for managing folders and chats. You can explore all options using `--help`.

```bash
owui --help
```

You can control verbosity with logging flags and output format with the `--output` option.
`owui --verbose folder list`
`owui --output json folder list`

#### Folder Management Examples

*   **Create a new folder:**
    ```bash
    owui folder create "My New Project Ideas"
    ```

*   **List all existing folders:**
    ```bash
    owui folder list
    ```

*   **List chats within a specific folder:**
    (Requires the folder ID obtained from `folder list`)
    ```bash
    owui folder list-chats "your-folder-id-here"
    ```

*   **Delete a folder:**
    ```bash
    owui folder delete "your-folder-id-here"
    ```

#### Chat Interaction Examples

*   **Create a new chat and get an LLM response:**
    ```bash
    owui chat create -m gemini-1.5-flash "What is the capital of France?"
    ```
    *(Use `-m` or `--model` to specify the model)*

*   **Continue an existing chat thread:**
    ```bash
    owui chat continue "your-chat-id-here" "Can you tell me more about its history?"
    ```

*   **View all messages in a specific chat:**
    ```bash
    owui chat list "your-chat-id-here"
    ```

*   **Rename a chat:**
    ```bash
    owui chat rename "your-chat-id-here" "French History Discussion"
    ```

*   **Delete a chat:**
    ```bash
    owui chat delete "your-chat-id-here"
    ```

### Python SDK Usage

You can also use the `openwebui` Python package directly in your scripts and applications for programmatic control.

```python
import asyncio
from openwebui import OpenWebUI, AuthenticationError, NotFoundError

async def main():
    try:
        # Client takes config from YAML/env by default, or you can pass directly:
        # client = OpenWebUI(base_url="http://localhost:8080", api_key="sk-YOUR_KEY")
        async with OpenWebUI() as client:
            # --- Folders API ---
            print("\n--- Listing Folders ---")
            folders = await client.folders.list()
            if folders:
                for folder in folders:
                    print(f"Folder: {folder.name} (ID: {folder.id})")
            else:
                print("No folders found.")
            
            # --- Chats API ---
            print("\n--- Creating a new chat ---")
            new_chat = await client.chats.create(model="gemini-1.5-flash", prompt="Tell me a fun fact about Python.")
            chat_id = new_chat.id
            print(f"Created chat: '{new_chat.title}' (ID: {chat_id})")
            print(f"Assistant's first response: {new_chat.chat.additional_properties['messages'][-1]['content']}")

            print("\n--- Continuing the chat ---")
            await client.chats.continue_chat(chat_id, "And why is it useful for web development?")

            print("\n--- Listing messages in the chat ---")
            chat_details = await client.chats.get(chat_id)
            for msg in chat_details.chat.additional_properties['messages']:
                print(f"[{msg['role'].capitalize()}]: {msg['content']}")

            print("\n--- Deleting the new chat ---")
            if await client.chats.delete(chat_id):
                print(f"Chat {chat_id} deleted successfully.")

    except AuthenticationError:
        print("Authentication failed. Please check your configuration.")
    except NotFoundError as e:
        print(f"Resource not found: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(main())
```

---

## 🛠️ Development

For those looking to contribute to the project:

1.  **Setup:** Ensure you have installed the project with development dependencies: `uv pip install -e ".[dev]"`
2.  **Running Tests:**
    ```bash
    # Run all tests (unit, CLI, integration)
    uv run pytest

    # Run only SDK unit tests
    uv run pytest tests/sdk/

    # Run only CLI tests
    uv run pytest tests/cli/

    # Run only integration tests (requires live server and configuration)
    uv run pytest tests/integration/
    ```
3.  **Code Style:** This project uses `ruff` for linting and formatting.
    ```bash
    # Check for linting errors
    uv run ruff check .

    # Auto-format code
    uv run ruff format .
    ```
4.  **Regenerating the OpenAPI Client:** If the OpenWebUI API changes, you can regenerate the low-level client with:
    ```bash
    openapi-python-client generate \
        --url http://your-openwebui-instance:8080/openapi.json \
        --output-path openwebui/open_web_ui_client
    ```


## 🤝 Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.