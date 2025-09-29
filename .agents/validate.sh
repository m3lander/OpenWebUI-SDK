#!/bin/bash
# Quick validation script for OpenWebUI-SDK environment
# Run this to check if your development environment is ready

set -e

echo "🔍 OpenWebUI-SDK Environment Validation"
echo "======================================="

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

success() { echo -e "${GREEN}✅ $1${NC}"; }
error() { echo -e "${RED}❌ $1${NC}"; }
warning() { echo -e "${YELLOW}⚠️  $1${NC}"; }

# Check Python version
if python3 -c "import sys; exit(0 if sys.version_info >= (3, 11) else 1)" 2>/dev/null; then
    success "Python 3.11+ available: $(python3 --version)"
else
    error "Python 3.11+ required"
    exit 1
fi

# Check if package is installed
if python3 -c "import openwebui" 2>/dev/null; then
    success "OpenWebUI-SDK package installed"
else
    error "OpenWebUI-SDK package not found. Run: ./.agents/setup.sh"
    exit 1
fi

# Check CLI availability
if command -v owui >/dev/null 2>&1; then
    success "CLI tool 'owui' available"
else
    error "CLI tool 'owui' not found. Check PATH or run setup script"
    exit 1
fi

# Test CLI basic functionality
if owui --help >/dev/null 2>&1; then
    success "CLI help command works"
else
    error "CLI help command failed"
    exit 1
fi

# Check development tools
if python3 -c "import pytest" 2>/dev/null; then
    success "pytest available"
else
    warning "pytest not found (needed for testing)"
fi

if python3 -c "import ruff" 2>/dev/null; then
    success "ruff available"
else
    warning "ruff not found (needed for linting)"
fi

# Run quick tests
echo ""
echo "🧪 Running quick tests..."
if python3 -m pytest tests/cli/ -q --tb=no >/dev/null 2>&1; then
    success "CLI tests pass"
else
    error "CLI tests failed"
    exit 1
fi

# Check linting
if python3 -m ruff check . >/dev/null 2>&1; then
    success "Code linting passes"
else
    warning "Code has linting issues (run: python3 -m ruff check . --fix)"
fi

# Check configuration
if [ -f ~/.owui/config.yaml ] || [ -f .owui/config.yaml ]; then
    success "Configuration file found"
elif [ -n "$OPENWEBUI_URL" ] && [ -n "$OPENWEBUI_API_KEY" ]; then
    success "Environment variables configured"
else
    warning "No configuration found. See .agents/config.example.yaml"
fi

echo ""
success "Environment validation complete! 🚀"
echo ""
echo "📋 Summary:"
echo "  • Python and package installed"
echo "  • CLI tool working"
echo "  • Tests passing"
echo "  • Development tools available"
echo ""
echo "💡 Ready for development!"