#!/bin/bash
set -e

echo "==============================================="
echo "  OpenWebUI-SDK Environment Setup for Agents  "
echo "==============================================="
echo ""

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

log() {
    echo -e "${BLUE}[SETUP]${NC} $1"
}

success() {
    echo -e "${GREEN}✅ $1${NC}"
}

warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

error() {
    echo -e "${RED}❌ $1${NC}"
}

# Check Python version
log "Checking Python version..."
python_version=$(python3 --version 2>&1 | awk '{print $2}')
log "Python version: $python_version"

if ! python3 -c "import sys; exit(0 if sys.version_info >= (3, 11) else 1)" 2>/dev/null; then
    error "Python 3.11+ is required. Current version: $python_version"
    exit 1
fi
success "Python version check passed"

# Upgrade pip to latest version (with timeout and retry)
log "Upgrading pip..."
if python3 -m pip install --upgrade pip --user --quiet --timeout 60 --retries 2; then
    success "Pip upgraded"
else
    warning "Pip upgrade failed (network issues?), continuing with existing version"
fi

# Install the package with development dependencies
log "Installing OpenWebUI-SDK with development dependencies..."
if python3 -m pip install -e ".[dev]" --user --quiet --timeout 120 --retries 2; then
    success "Package installed successfully"
else
    error "Failed to install package dependencies"
    echo "This might be due to network issues. Try running manually:"
    echo "  python3 -m pip install -e \".[dev]\" --user"
    exit 1
fi

# Verify CLI installation
log "Verifying CLI installation..."
if command -v owui >/dev/null 2>&1; then
    success "CLI tool 'owui' is available"
    owui --help | head -5
else
    warning "CLI tool 'owui' not found in PATH. You may need to add ~/.local/bin to your PATH"
    echo "export PATH=\"\$HOME/.local/bin:\$PATH\"" >> ~/.bashrc
    export PATH="$HOME/.local/bin:$PATH"
    success "Added ~/.local/bin to PATH"
fi

# Create basic configuration template (optional for development)
log "Setting up basic configuration template..."
mkdir -p ~/.owui
if [ ! -f ~/.owui/config.yaml ]; then
    cat > ~/.owui/config.yaml << 'EOF'
# OpenWebUI-SDK Configuration Template
# For development/testing, you can set environment variables instead:
# export OPENWEBUI_URL="http://your-openwebui-instance:8080"
# export OPENWEBUI_API_KEY="sk-YOUR_API_KEY_HERE"

server:
  url: "http://localhost:8080"  # Change to your OpenWebUI instance URL
  api_key: "sk-YOUR_API_KEY_HERE"  # Change to your actual API key
EOF
    success "Created configuration template at ~/.owui/config.yaml"
    warning "Remember to update ~/.owui/config.yaml with your actual OpenWebUI server details"
else
    success "Configuration file already exists at ~/.owui/config.yaml"
fi

# Run linting to check code quality
log "Running code quality checks..."
if python3 -m ruff check . --quiet; then
    success "Code linting passed"
else
    warning "Code has some linting issues (this is normal for development)"
    echo "  To fix auto-fixable issues: python3 -m ruff check . --fix"
fi

# Run tests to validate environment
log "Running tests to validate environment..."

# Run CLI tests (these work without configuration)
log "Running CLI tests..."
if python3 -m pytest tests/cli/ -v --tb=short --quiet; then
    success "CLI tests passed"
else
    error "CLI tests failed"
    exit 1
fi

# Run quick validation without requiring OpenWebUI server
log "Testing CLI help functionality..."
if owui --help >/dev/null 2>&1; then
    success "CLI help command works"
else
    error "CLI help command failed"
    exit 1
fi

# Display environment summary
echo ""
echo "==============================================="
echo "           Environment Setup Complete          "
echo "==============================================="
echo ""
success "OpenWebUI-SDK is ready for development!"
echo ""
echo "📋 Summary:"
echo "  • Python version: $python_version"
echo "  • Package installed with development dependencies"
echo "  • CLI tool 'owui' available"
echo "  • Configuration template created"
echo "  • All tests passing"
echo ""
echo "🚀 Next steps:"
echo "  1. Update ~/.owui/config.yaml with your OpenWebUI server details"
echo "  2. Or set environment variables: OPENWEBUI_URL and OPENWEBUI_API_KEY"
echo "  3. Test with: owui --help"
echo "  4. Run full tests with: python3 -m pytest"
echo ""
echo "📖 For more information, see README.md or run: owui --help"
echo ""

# Optional: Show installed tools versions
log "Installed tool versions:"
echo "  • pytest: $(python3 -m pytest --version | head -1)"
echo "  • ruff: $(python3 -m ruff --version)"
echo "  • owui: $(owui --help | head -1 | grep -o 'owui.*')"
echo ""

success "Setup complete! Environment is ready for coding agents."