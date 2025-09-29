# OpenWebUI-SDK Context

## Project Overview

OpenWebUI-SDK is a modern, asynchronous Python SDK and Command-Line Interface (`owui`) for interacting with Open WebUI instances. The project provides a unified, Pythonic interface to manage chats, folders, knowledge bases, and interact with Large Language Models (LLMs) served by Open WebUI. It follows a structured, layered design and is built to be both programmatically flexible for developers and easy to use from the terminal for end-users.

### Key Features

1. **Asynchronous First SDK**: A clean, `asyncio`-native Python library for high-performance, concurrent interaction
2. **Intuitive CLI**: A powerful command-line tool built with `click` for easy management of chats, folders, and Knowledge Bases directly from the terminal
3. **Complex Workflow Abstraction**: Simplifies multi-step API interactions into single, intuitive SDK methods
4. **Hierarchical YAML Configuration**: Loads configuration from `~/.owui/config.yaml` or a local `.owui/config.yaml`, with environment variables for overrides
5. **Robust Error Handling**: Provides custom exceptions like `AuthenticationError` and `NotFoundError`
6. **Integrated Logging**: Detailed logging controllable via CLI flags (`--verbose`, `--debug`)
7. **Type-Safe API Interaction**: Uses an auto-generated low-level client from the OpenWebUI OpenAPI schema
8. **Comprehensive Test Suite**: Includes unit tests, integration tests, and CLI tests

## Architecture

The SDK is organized into several key modules:

- `client.py`: Main async client class that coordinates access to different API resource groups
- `api/`: Contains specialized API modules for different functionality:
  - `folders.py`: Folder management functionality
  - `chats.py`: Chat management and interaction functionality
  - `knowledge.py`: Knowledge base management functionality
- `config.py`: Configuration loading with precedence (env vars > local config > user config)
- `exceptions.py`: Custom exception hierarchy for error handling
- `cli/main.py`: Command-line interface implementation using Click
- `open_web_ui_client/`: Auto-generated low-level OpenAPI client

## Configuration System

The SDK uses a hierarchical configuration system with the following precedence (highest to lowest):
1. Environment variables (`OPENWEBUI_URL`, `OPENWEBUI_API_KEY`)
2. Local project config file (`.owui/config.yaml`)
3. User-level config file (`~/.owui/config.yaml`)

Configuration format:
```yaml
# ~/.owui/config.yaml
server:
  url: "http://your-openwebui-instance:8080"
  api_key: "sk-YOUR_API_KEY_HERE"
```

## Building and Running

### Installation
```bash
# Clone the repository
git clone https://github.com/dubh3124/OpenWebUI-SDK.git
cd OpenWebUI-SDK

# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate

# Install the package in editable mode with development dependencies
uv pip install -e ".[dev]"  # Or using pip if uv is not available
```

### Running Tests
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

### Code Style
This project uses `ruff` for linting and formatting:
```bash
# Check for linting errors
uv run ruff check .

# Auto-format code
uv run ruff format .
```

### Regenerating the OpenAPI Client
If the OpenWebUI API changes, you can regenerate the low-level client:
```bash
openapi-python-client generate \
    --url http://your-openwebui-instance:8080/openapi.json \
    --output-path openwebui/open_web_ui_client
```

## Development Conventions

- **Python version**: Requires Python >= 3.11
- **Async-first**: The SDK is designed to be asynchronous-first for better performance
- **Error Handling**: All API errors are wrapped in custom exception classes inheriting from `OpenWebUIError`
- **Logging**: Uses Python's standard logging module with configurable levels
- **Configuration**: Uses YAML for configuration files with environment variable overrides

## CLI Commands

### Folder Management
- `owui folder create "Folder Name"` - Create a new folder
- `owui folder list` - List all available folders
- `owui folder list-chats "folder_id"` - List chats within a specific folder
- `owui folder delete "folder_id"` - Delete a folder

### Chat Management
- `owui chat create -m gemini-1.5-flash "Prompt text"` - Create a new chat
- `owui chat continue "chat_id" "Prompt text"` - Continue an existing chat
- `owui chat list "chat_id"` - List all messages in a chat
- `owui chat rename "chat_id" "New Title"` - Rename a chat
- `owui chat delete "chat_id"` - Delete a chat

### Knowledge Base Management
- `owui kb create "KB Name" --description "Description"` - Create a new knowledge base
- `owui kb list-kbs` - List all knowledge bases
- `owui kb upload-file ./file.txt --kb-id "kb_id"` - Upload a single file
- `owui kb upload-dir ./directory/ --kb-id "kb_id"` - Upload a directory
- `owui kb list-files "kb_id"` - List files in a knowledge base
- `owui kb update-file "file_id" ./updated_file.txt` - Update a file
- `owui kb delete-file "file_id"` - Delete a file
- `owui kb delete-all-files "kb_id"` - Delete all files in a KB

### Global Options
- `--verbose, -v`: Enable INFO level logging
- `--debug`: Enable DEBUG level logging
- `--output [text|json]`: Output format

## Key Dependencies

- `httpx`: HTTP client for async API requests
- `click`: CLI framework
- `PyYAML`: YAML configuration parsing
- `python-dotenv`: Environment variable loading
- `attrs`: Classes with minimal boilerplate
- `python-dateutil`: Date/time utilities
- `tqdm`: Progress bars
- `pathspec`: Pattern matching for file paths

## Testing

The project includes comprehensive tests covering:
- Unit tests for SDK functionality
- Integration tests for API interactions (requires a live OpenWebUI server)
- CLI tests for command-line interface functionality
- Code coverage reporting

## Project Structure

- `openwebui/`: Main SDK package with client, config, exceptions, and API modules
- `tests/`: Test suite with unit, integration, and CLI tests
- `pyproject.toml`: Project configuration and dependencies
- `README.md`: User documentation
- `generate_client.sh`: Script for regenerating OpenAPI client
- `run_full_scenario.sh`: Shell script demonstrating full SDK/CLI workflow