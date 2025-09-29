---
description: "Initialize a new AI-first development environment for a project"
arguments:
  - name: "project_name"
    description: "Name of the project"
    required: true
  - name: "project_type"
    description: "Type of project (sdk, api, web, cli, tool, library)"
    required: true
  - name: "tech_stack"
    description: "Primary technology stack (python, node, typescript, go, rust)"
    required: true
  - name: "description"
    description: "Brief project description"
    required: false
---

# AI-First Development Environment Initialization

This command will initialize a comprehensive AI-first development environment for your project.

## Project Configuration
- **Name**: $1
- **Type**: $2
- **Tech Stack**: $3
- **Description**: $4

The following files will be created based on AI-first development patterns:

1. **CLAUDE.md** - Agent instructions and project overview
2. **AGENT_HANDOFF.md** - Technical patterns and gotchas
3. **CONTRIBUTING.md** - Developer onboarding guide
4. **.claude/commands/** - Custom slash commands
5. **Quality gate scripts** - Automated checks and validation

Continue with initialization? [y/N]