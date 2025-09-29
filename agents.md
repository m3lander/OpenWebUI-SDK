# Coding Agent Environment Setup

This repository is configured for coding agents like Jules, GitHub Copilot Agent, and Claude Code.

## Quick Setup

Run the setup script to prepare your environment:

```bash
./.agents/setup.sh
```

This will:
- Install all Python dependencies 
- Set up configuration templates
- Validate the environment with tests
- Ensure CLI tools are working

## Validation

To quickly check if your environment is ready:

```bash
./.agents/validate.sh
```

## Documentation

See `.agents/README.md` for comprehensive documentation including:
- Project architecture and structure
- Development workflow
- Testing procedures
- Configuration management
- Agent-specific guidance

## Configuration

The project uses hierarchical configuration (environment variables take precedence):

1. Environment variables: `OPENWEBUI_URL`, `OPENWEBUI_API_KEY`
2. Local project config: `.owui/config.yaml` 
3. User config: `~/.owui/config.yaml`

See `.agents/config.example.yaml` for a template.

## Testing

Safe development without external dependencies:

```bash
# CLI tests (work without OpenWebUI server)
python3 -m pytest tests/cli/ -v

# Code quality checks
python3 -m ruff check .
```

This environment is designed to be coding-agent friendly with minimal external dependencies for development.