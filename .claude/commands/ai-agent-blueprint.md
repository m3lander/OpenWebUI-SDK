---
description: "Create an AI-first development environment blueprint from a repository or idea"
arguments:
  - name: "project_type"
    description: "Type of project (sdk, api, web, cli, tool, etc.)"
    required: false
  - name: "tech_stack"
    description: "Technology stack (python, node, typescript, etc.)"
    required: false
  - name: "focus_area"
    description: "Primary focus (performance, testing, documentation, etc.)"
    required: false
---

# AI-First Agent Development Environment Blueprint

## Template for Creating AI-First Development Environments

Based on the OpenWebUI-SDK documentation patterns, this blueprint helps you transform any repository or idea into an AI-first, coding agent native development environment.

## Quick Reference
- Use `$ARGUMENTS` to pass project type, tech stack, and focus areas
- Generates comprehensive documentation templates
- Creates agent-ready configuration files
- Sets up standardized development workflows

---

## 1. Project Overview Template

### Mission and Scope
- **Core Purpose**: [Describe the primary objective in one sentence]
- **Target Users**: [Who will use this - developers, end-users, etc.]
- **Key Differentiators**: [What makes this unique/valuable]

### Quickstart Commands
```bash
# Installation
[Install command for dev setup]

# Development
[Key development commands]

# Testing
[Test commands and suites]

# Quality Assurance
[Lint/format/check commands]
```

## 2. Architecture Overview Template

### Core Components
- **Entry Point**: `[Main module/file]`
  - `[Key functionality and responsibilities]`
- **Key Modules**:
  - `[Module 1]: [Primary responsibility]`
  - `[Module 2]: [Primary responsibility]`
  - `[Module 3]: [Primary responsibility]`

### Configuration System
- **Precedence**: Environment variables > local config > user config
- **Config Format**: [YAML/JSON/Environment]
- **Key Settings**: [Important configuration options]

## 3. Development Patterns Template

### Core Conventions
- **Code Style**: [Linting rules, formatting standards]
- **Error Handling**: [Exception patterns, error types]
- **Testing**: [Unit, integration, e2e approaches]
- **Documentation**: [Doc standards, API docs]

### Key Technical Details
- **Type Safety**: [Type system approach, validation]
- **Performance**: [Caching, async patterns, optimizations]
- **Security**: [Authentication, authorization, validation]
- **Deployment**: [Build, CI/CD, packaging]

## 4. Build and Test Workflows Template

### Standard Commands
```bash
# Development
[Dev server/start command]

# Building
[Build command(s)]

# Testing
[Unit tests]: [command]
[Integration tests]: [command]
[E2E tests]: [command]

# Quality
[Linting]: [command]
[Formatting]: [command]
[Type checking]: [command]
```

### Testing Architecture
- **Unit Tests**: [Scope and mocking approach]
- **Integration Tests**: [Live dependencies setup]
- **E2E Tests**: [Full system testing]
- **Fixtures**: [Test data setup]

## 5. Agent Handoff Template

### High-Leverage Patterns
- **Wrapper Pattern**: [How to abstract complexity]
- **Response Handling**: [Standardized processing]
- **Error Patterns**: [Exception hierarchy]
- **Configuration**: [Setup and precedence]

### Critical Gotchas
- **Known Issues**: [Common problems and workarounds]
- **Edge Cases**: [Special handling requirements]
- **Dependencies**: [Key external integrations]

## 6. Quality Gates Template

### Pre-Commit Checks
- [ ] Linting passes
- [ ] Formatting applied
- [ ] Type checking valid
- [ ] Unit tests pass
- [ ] Integration tests pass
- [ ] Documentation updated

### Code Review Focus
- **Architecture**: [Design principles adherence]
- **Performance**: [Efficiency considerations]
- **Security**: [Safety and validation]
- **Maintainability**: [Code clarity and structure]

## 7. Documentation Structure Template

### Essential Files
- **CLAUDE.md**: [Agent instructions and project overview]
- **AGENT_HANDOFF.md**: [Technical patterns and gotchas]
- **CONTRIBUTING.md**: [Developer onboarding]
- **README.md**: [User-facing documentation]

### API Documentation
- **Entry Points**: [Main interfaces]
- **Configuration**: [Setup and options]
- **Examples**: [Usage patterns]
- **Migration**: [Upgrade guides]

## 8. Operating Loop for AI Agents

### Development Cycle
1. **Understand**: Read existing documentation and code structure
2. **Plan**: Create task breakdown with dependencies
3. **Implement**: Follow established patterns and conventions
4. **Test**: Verify with existing test suite
5. **Refactor**: Apply quality standards and optimizations
6. **Document**: Update agent instructions and patterns

### Agent Capabilities
- **Code Generation**: Follows established patterns
- **Refactoring**: Maintains API compatibility
- **Testing**: Creates comprehensive test coverage
- **Documentation**: Updates agent instructions
- **Debugging**: Uses systematic troubleshooting

## 9. Domain-Specific Patterns

### For SDK Projects
- **Client Pattern**: Abstract low-level APIs
- **Response Handling**: Standardize error mapping
- **Configuration**: Hierarchical precedence
- **Testing**: Mock HTTP calls

### For Web Projects
- **Component Architecture**: Reusable, composable parts
- **State Management**: Centralized data flow
- **API Integration**: Type-safe endpoints
- **Styling**: Design system approach

### For CLI Tools
- **Command Structure**: Consistent subcommands
- **Output Formats**: Text and JSON modes
- **Configuration**: Global and local settings
- **Error Handling**: User-friendly messages

### For API Services
- **Endpoint Design**: RESTful patterns
- **Authentication**: Security first
- **Rate Limiting**: Protection and fairness
- **Documentation**: OpenAPI/Swagger

## 10. Implementation Steps

To create an AI-first environment:

1. **Analyze Current State**
   - Review existing code structure
   - Identify key patterns and conventions
   - Document technical decisions

2. **Create Documentation Templates**
   - Generate CLAUDE.md with project specifics
   - Create AGENT_HANDOFF.md with technical patterns
   - Set up CONTRIBUTING.md for onboarding

3. **Standardize Workflows**
   - Define build, test, and quality commands
   - Set up CI/CD integration
   - Create development scripts

4. **Configure Agent Support**
   - Add slash commands for common tasks
   - Set up testing and validation
   - Create code generation templates

5. **Iterate and Improve**
   - Gather feedback from agent usage
   - Refine patterns and documentation
   - Expand automation capabilities

## Generated for: $ARGUMENTS

---
*This blueprint was auto-generated based on AI-first development patterns. Customize the templates above for your specific project needs.*