# OpenWebUI-SDK Agent Environment Guide

This guide is designed for coding agents (Jules, GitHub Copilot Agent, Claude Code, etc.) to quickly understand and work with the OpenWebUI-SDK repository.

## Quick Start

Run the setup script to prepare your environment:
```bash
./.agents/setup.sh
```

This will install dependencies, set up configuration templates, and validate the environment.

## Project Overview

**OpenWebUI-SDK** is a modern Python SDK and CLI tool for interacting with Open WebUI instances. It provides:

- 🐍 **Asynchronous Python SDK** (`openwebui` package)
- 🖥️ **Command-line tool** (`owui` command)
- 📁 **Management of chats, folders, and knowledge bases**
- 🤖 **LLM interaction capabilities**

## Architecture

```
openwebui/
├── api/                    # High-level SDK API classes
│   ├── chats.py           # Chat management
│   ├── folders.py         # Folder operations  
│   └── knowledge.py       # Knowledge base operations
├── cli/                   # Command-line interface
│   └── main.py           # CLI entry point
├── open_web_ui_client/   # Auto-generated low-level client
├── config.py             # Configuration management
└── client.py             # Main SDK client class

tests/
├── cli/                  # CLI tests (work without server)
├── sdk/                  # SDK unit tests (need config)
└── integration/          # Integration tests (need server)
```

## Configuration

The SDK uses a hierarchical configuration system:

1. **Environment variables** (highest precedence):
   ```bash
   export OPENWEBUI_URL="http://your-server:8080"
   export OPENWEBUI_API_KEY="sk-YOUR_KEY"
   ```

2. **Local project config**: `.owui/config.yaml`
3. **User config**: `~/.owui/config.yaml`

Sample config:
```yaml
server:
  url: "http://localhost:8080"
  api_key: "sk-YOUR_API_KEY_HERE"
```

## Development Workflow

### Running Tests

```bash
# All tests (requires configuration for integration tests)
python3 -m pytest

# CLI tests only (work without server configuration)
python3 -m pytest tests/cli/ -v

# SDK unit tests (mock-based, work without server)
python3 -m pytest tests/sdk/ -v

# Integration tests (require live OpenWebUI server)
python3 -m pytest tests/integration/ -v
```

### Code Quality

```bash
# Check linting
python3 -m ruff check .

# Auto-fix issues
python3 -m ruff check . --fix

# Format code
python3 -m ruff format .
```

### CLI Usage Examples

```bash
# Show help
owui --help

# List folders (requires configuration)
owui folder list

# Create a chat (requires configuration)
owui chat create -m "gpt-4" "Hello, world!"

# Test without configuration (shows help)
owui --help
```

## Key Files for Development

### Core SDK Files
- `openwebui/client.py` - Main SDK client class
- `openwebui/config.py` - Configuration management
- `openwebui/api/` - High-level API classes

### CLI Files
- `openwebui/cli/main.py` - CLI entry point and commands

### Configuration Files
- `pyproject.toml` - Project metadata and dependencies
- `.gitignore` - Git ignore patterns

### Testing
- `tests/cli/` - CLI tests (best for development without server)
- `tests/sdk/` - SDK unit tests
- `conftest.py` - Pytest configuration

## Common Development Tasks

### Adding New CLI Commands
1. Add command to `openwebui/cli/main.py`
2. Add corresponding SDK method to appropriate API class
3. Write CLI tests in `tests/cli/`
4. Write SDK tests in `tests/sdk/`

### Adding New SDK Features
1. Add method to appropriate API class in `openwebui/api/`
2. Add tests in `tests/sdk/`
3. Consider adding CLI command for the feature

### Fixing Bugs
1. Write failing test first
2. Fix the bug
3. Ensure all tests pass
4. Check code quality with ruff

## Environment Validation

After setup, validate your environment:

```bash
# Check Python version (3.11+ required)
python3 --version

# Check if CLI is installed
owui --help

# Run safe tests (no configuration needed)
python3 -m pytest tests/cli/ -v

# Check code quality
python3 -m ruff check .
```

## Working Without OpenWebUI Server

You can develop most features without a running OpenWebUI server:

- **CLI tests**: Use mocking to test CLI commands
- **SDK tests**: Use mocking to test SDK methods
- **Code quality**: Linting and formatting work offline
- **Development**: Add features and write tests

For testing with a real server, you'll need:
1. Running OpenWebUI instance
2. Valid API key
3. Proper configuration

## Troubleshooting

### CLI not found
```bash
export PATH="$HOME/.local/bin:$PATH"
```

### Configuration errors
- Set environment variables: `OPENWEBUI_URL` and `OPENWEBUI_API_KEY`
- Or create config file with proper server details

### Test failures
- CLI tests should always pass
- SDK/integration tests need proper configuration
- Check if you have the right Python version (3.11+)

### Import errors
```bash
python3 -m pip install -e ".[dev]" --user
```

## Agent-Specific Notes

### For Jules
- Use the setup script in your environment configuration
- The project supports both `pip` and `uv` (Jules VMs have both)
- All necessary tools are included in development dependencies

### For GitHub Copilot Agent
- Setup script handles PATH configuration automatically
- Use CLI tests for safe development without external dependencies
- Code quality checks are integrated

### For Claude Code
- Project structure is well-documented in this file
- Tests provide good examples of usage patterns
- Configuration is flexible (env vars or YAML files)

## Resources

- **README.md**: Main project documentation
- **pyproject.toml**: Dependencies and project metadata
- **tests/**: Example usage patterns
- **openwebui/**: Source code with docstrings

This environment is designed to be coding-agent friendly with comprehensive testing, clear structure, and minimal external dependencies for development.