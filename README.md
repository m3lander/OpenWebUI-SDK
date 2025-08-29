# OpenWebUI-SDK

A modern, asynchronous Python SDK and Command-Line Interface (`owui`) for interacting with your Open WebUI instance.

This project provides a unified, Pythonic interface to manage chats, folders, knowledgebases and interact with Large Language Models (LLMs) served by Open WebUI, following a structured, layered design. It is built to be both programmatically flexible for developers and easy to use from the terminal for end-users.

[//]: # ([![PyPI Version]&#40;https://img.shields.io/pypi/v/openwebui-sdk.svg?style=for-the-badge&#41;]&#40;https://pypi.org/project/openwebui-sdk/&#41;)

[//]: # ([![Python Versions]&#40;https://img.shields.io/pypi/pyversions/openwebui-sdk.svg?style=for-the-badge&#41;]&#40;https://pypi.org/project/openwebui-sdk/&#41;)

[![CI Tests](https://img.shields.io/github/actions/workflow/status/dubh3124/OpenWebUI-SDK/test.yml?branch=main&label=tests&style=for-the-badge)](https://github.com/dubh3124/OpenWebUI-SDK/actions/workflows/test.yaml)

[![Code Coverage](https://img.shields.io/codecov/c/github/dubh3124/OpenWebUI-SDK?style=for-the-badge)](https://codecov.io/gh/dubh3124/OpenWebUI-SDK)

[![Code style: ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json&style=for-the-badge)](https://github.com/astral-sh/ruff)

---

## 🚀 Features

*   **Asynchronous First SDK:** A clean, `asyncio`-native Python library (`openwebui`) for high-performance, concurrent interaction.
*   **Intuitive CLI:** A powerful command-line tool (`owui`) built with `click` for easy management of chats, folders, and Knowledge Bases directly from your terminal.
*   **Complex Workflow Abstraction:** Simplifies multi-step API interactions (e.g., creating a new chat with an initial LLM response, uploading a directory to a KB with `.kbignore` rules) into single, intuitive SDK methods.
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
    git clone https://github.com/dubh3124/OpenWebUI-SDK.git # Replace with your actual repo URL
    cd OpenWebUI-SDK
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

The CLI provides commands for managing folders, chats, and knowledge bases. You can explore all options using `--help`.

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

#### Knowledge Base Management Examples

*   **Create a new Knowledge Base:**
    ```bash
    owui kb create "My Project Docs" --description "Documentation for my new project."
    ```

*   **List all Knowledge Bases:**
    ```bash
    owui kb list-kbs
    ```

*   **Upload a single file to a KB:**
    ```bash
    owui kb upload-file ./my_document.txt --kb-id "your-knowledge-base-id-here"
    ```

*   **Upload a local directory to a KB:**
    ```bash
    # This command will upload all files from 'my_local_files/' to the specified KB.
    # It respects .kbignore files (e.g., my_local_files/.kbignore) for exclusions.
    owui kb upload-dir ./my_local_files/ --kb-id "your-knowledge-base-id-here"
    ```

*   **List files within a Knowledge Base:**
    ```bash
    owui kb list-files "your-knowledge-base-id-here" --search "report"
    ```

*   **Update content of an existing file in a KB:**
    ```bash
    owui kb update-file "your-file-id-here" ./updated_document.txt
    ```

*   **Delete a specific file from a KB:**
    ```bash
    owui kb delete-file "your-file-id-here"
    ```

*   **Delete all files from a Knowledge Base:**
    *(Requires confirmation, use `--yes` to skip)*
    ```bash
    owui kb delete-all-files "your-knowledge-base-id-here"
    ```
    
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

    # Run specific integration tests for Knowledge Base functionality
    uv run pytest tests/integration/test_kb_sdk_integration.py
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