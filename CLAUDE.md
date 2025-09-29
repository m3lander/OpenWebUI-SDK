# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the OpenWebUI-SDK, an async-first Python SDK and CLI for interacting with Open WebUI instances. The project provides a high-level interface that wraps a generated OpenAPI client, offering opinionated workflows and a Click-based CLI tool.

## Common Development Commands

### Installation and Setup
```bash
# Install for development (recommended - uses uv)
uv pip install -e ".[dev]"

# Or using pip
pip install -e ".[dev]"
```

### Testing
```bash
# Run all tests (unit, CLI, integration)
uv run pytest

# Run specific test suites
uv run pytest tests/sdk/          # SDK unit tests
uv run pytest tests/cli/          # CLI tests
uv run pytest tests/integration/  # Integration tests (requires live server)

# Run single test file
uv run pytest tests/sdk/test_sdk_chats.py

# Run with live server configuration
uv run pytest tests/integration/ --server-url http://your-server:8080
```

### Code Quality
```bash
# Lint code
uv run ruff check .

# Format code
uv run ruff format .

# Type checking
uv run mypy openwebui/
```

### Client Regeneration
```bash
# Regenerate the OpenAPI client when the API changes
openapi-python-client generate \
    --url http://your-openwebui-instance:8080/openapi.json \
    --output-path openwebui/open_web_ui_client \
    --overwrite \
    --meta uv
```

## Architecture Overview

### Core Architecture
- **Entry Point**: `openwebui/client.py` - Main `OpenWebUI` class that manages authentication and API groups
- **Configuration**: `openwebui/config.py` - Hierarchical config loading (env vars > local .yaml > user .yaml)
- **Generated Client**: `openwebui/open_web_ui_client/` - Auto-generated OpenAPI client with typed models
- **High-level APIs**: `openwebui/api/` - Opinionated wrappers around generated endpoints
- **CLI**: `openwebui/cli/main.py` - Click-based CLI tool
- **Utilities**: `openwebui/utils/` - Helper functions for API responses and file handling

### Key Components
1. **OpenWebUI Client**: Main async client that provides access to API groups
2. **API Groups**:
   - `FoldersAPI` - Chat folder management
   - `ChatsAPI` - Chat creation, continuation, and management with RAG support
   - `KnowledgeBaseAPI` - Knowledge base and file management
3. **Generated Client**: Type-safe OpenAPI client with `UNSET` sentinel values
4. **Response Handler**: `utils/api_utils.py:handle_api_response()` - Standardized response processing

### Configuration Hierarchy
Configuration loads in this order (highest precedence first):
1. Environment variables (`OPENWEBUI_URL`, `OPENWEBUI_API_KEY`)
2. Local project config (`./.owui/config.yaml`)
3. User-level config (`~/.owui/config.yaml`)

### Testing Architecture
- **Unit Tests**: Mock HTTP calls, test SDK logic in isolation
- **CLI Tests**: Mock the entire SDK client, test CLI commands
- **Integration Tests**: Use live client against real OpenWebUI server
- **Fixtures**: `conftest.py` provides configured clients and test resources

## Development Patterns

### SDK Development
When adding new endpoints:
1. Import generated functions from `openwebui/open_web_ui_client/open_web_ui_client/api/`
2. Use generated models and `UNSET` for optional fields
3. Call `...asyncio_detailed()` with `client=self._client`
4. Return `handle_api_response(response, "descriptive name")`
5. Keep methods async and catch `httpx.ConnectError`

### Response Handling
Always use `handle_api_response()` from `utils/api_utils.py`:
- Returns `response.parsed` when available
- Falls back to decoded JSON on parse gaps
- Maps HTTP status codes to exceptions (401→AuthenticationError, 404→NotFoundError)
- Returns `True` for 204 responses

### CLI Development
- Entry point: `openwebui/cli/main.py` with script name `owui`
- Global flags: `--verbose`, `--debug`, `--output {text,json}`
- Commands: folder, chat, kb (knowledge base)
- Text mode confirms destructive operations; `--yes` skips confirmation
- JSON mode prints structured data, avoids interactive prompts

### Knowledge Base Operations
- Respect `.kbignore` files via `utils/kbignore_parser.py`
- Skip uploading the `.kbignore` file itself
- Use async batch processing for directory uploads
- Known issue: `list_all()` workaround for client schema gaps

## Key Technical Details

### Async Pattern
- All SDK methods are async-first
- Use `await` for all API calls
- Client implements async context manager pattern
- Integration tests manage client lifecycle with `pytest_asyncio`

### Type Safety
- Generated client provides type-safe models
- Use `UNSET` sentinel for optional fields in generated models
- For flexible schemas, set `additional_properties` parameter
- MyPy configured for type checking

### Error Handling
- Custom exceptions in `openwebui/exceptions.py`
- Connection errors wrapped from `httpx.ConnectError`
- Authentication errors for 401 responses
- Not found errors for 404 responses
- API errors for other HTTP error codes

### File Operations
- Directory uploads support `.kbignore` patterns
- Async batch processing for multiple files
- Progress tracking with `tqdm` for CLI operations
- Path validation and sanitization

## Testing Notes

### Integration Test Requirements
- Requires live OpenWebUI server
- Configure via `--server-url`, `TEST_SERVER_URL`, or `OPENWEBUI_URL`
- Requires `OPENWEBUI_API_KEY` environment variable
- Automatic cleanup of test resources (folders, knowledge bases)

### Test Configuration
- SDK unit tests use mocked HTTP client
- CLI tests use mocked SDK client
- Integration tests use live client with cleanup fixtures
- Pytest configured for async with `asyncio_mode = "auto"`

## Important Files

- `pyproject.toml` - Project configuration, dependencies, and tool settings
- `openwebui/client.py` - Main SDK client class
- `openwebui/config.py` - Configuration loading and management
- `openwebui/cli/main.py` - CLI entry point and command definitions
- `tests/conftest.py` - Test fixtures and configuration
- `openwebui/utils/api_utils.py` - Response handling utilities
- `openwebui/utils/kbignore_parser.py` - .kbignore file processing