# OpenWebUI-SDK — Agent Handoff

This document primes coding agents to work productively on this repository. It condenses the architecture, conventions, workflows, and high‑leverage patterns used across the SDK and CLI.

## Mission and scope

- Provide a modern, async‑first Python SDK and CLI (script `owui`) to interact with an Open WebUI server.
- Hide low‑level OpenAPI complexity behind simple, opinionated high‑level abstractions (folders, chats, knowledge base, models, etc.).
- Prefer small, composable wrappers that call into the generated client and centralize response handling and errors.

## Quickstart

- Python >= 3.11
- Install for dev: `uv pip install -e .[dev]` (or `pip install -e .[dev]`)
- Configure server:
  - Env takes precedence: `OPENWEBUI_URL`, `OPENWEBUI_API_KEY`
  - Or `~/.owui/config.yaml` and/or `./.owui/config.yaml`
- Run CLI: `owui --help`
- Run tests: `uv run pytest` (see subsets below)
- Lint/format: `uv run ruff check .` and `uv run ruff format .`

## Architecture overview

- Entry point: `openwebui/client.py`
  - Loads config via `openwebui/config.py` (env > local `./.owui/config.yaml` > user `~/.owui/config.yaml`), rstrip `/` from URL.
  - Creates `AuthenticatedClient` from `openwebui/open_web_ui_client/open_web_ui_client`.
  - Exposes high‑level groups: `FoldersAPI`, `ChatsAPI`, `KnowledgeBaseAPI` (and future: `ModelsAPI`).
- Generated client: `openwebui/open_web_ui_client/open_web_ui_client/*`
  - Uses httpx; typed models with `UNSET` sentinel for optionals.
- Response handling: `openwebui/utils/api_utils.py:handle_api_response()`
  - Returns `response.parsed` when present, else decodes JSON on parse gaps; maps 401→AuthenticationError, 404→NotFoundError; treats 204 and empty 2xx as True.
- RAG flow: `openwebui/api/chats.py`
  - If `kb_ids`, augment the user prompt using `KnowledgeBaseAPI.query(...)` for the LLM call only; save original user prompt in history.
- Knowledge base quirks
  - Listing workaround in `KnowledgeBaseAPI.list_all()`: generated parser returns `None`; code converts raw JSON to `models.KnowledgeResponse`.
  - Directory uploads respect `.kbignore` via `utils/kbignore_parser.py` and skip uploading the `.kbignore` file itself.

## Conventions and patterns

- Always call endpoints from `openwebui/open_web_ui_client/open_web_ui_client/api/...` and route results through `handle_api_response`.
- Build payloads with generated `models.*`, use `UNSET` when optional args are not supplied (avoid sending `null`).
- Flexible schemas: set `.additional_properties` (e.g., chat message arrays, model params) before sending.
- SDK is async. Catch `httpx.ConnectError` in wrappers and re‑raise `openwebui.exceptions.ConnectionError`.
- CLI (`openwebui/cli/main.py`): Click, async `asyncio.run(...)`; text mode confirms destructive ops; JSON mode is non‑interactive and emits structured data via `format_output`.
- Tests: mock low‑level `...asyncio_detailed` and return `MagicMock(spec=Response, status_code=200, parsed=...)`; CLI tests patch `OpenWebUI` and assert awaited high‑level calls.

## Commands and workflows

- Tests
  - All: `uv run pytest`
  - SDK: `uv run pytest tests/sdk/`
  - CLI: `uv run pytest tests/cli/`
  - Integration: `uv run pytest tests/integration/` (needs live server and `OPENWEBUI_URL`+`OPENWEBUI_API_KEY` or `--server-url`)
- Lint/format: `uv run ruff check .` / `uv run ruff format .`
- End‑to‑end demo: `run_full_scenario.sh`
- Regenerate client: `generate_client.sh` (openapi-python-client with `--meta uv`)

## High‑leverage wrapper patterns

- Folder wrappers (reference): `openwebui/api/folders.py`
  - Thin async wrappers that construct forms, call `...asyncio_detailed`, and return `handle_api_response(...)`.
- Chat wrappers (reference): `openwebui/api/chats.py`
  - Two‑step create: LLM completion → save messages; preserve original user text when saving history; use `additional_properties` for `messages` and `models`.
- Knowledge wrappers (reference): `openwebui/api/knowledge.py`
  - RAG query builds `QueryCollectionsForm` with `UNSET` for missing optionals; list‑all workaround; directory upload with `.kbignore` honoring and async batch uploads.

## Example: Adding a new high‑level Models API

- Generated endpoints available: `api/models/*` including create, list, get, update, delete, toggle, sync, export.
- Minimal SDK wrapper (file: `openwebui/api/models.py`):
  - `create(id, name, params: dict, description: str | None = None, base_model_id: str | None = None, is_active: bool = True) -> models.ModelModel`
    - Build `form = models.ModelForm(id=id, name=name, meta=models.ModelMeta(description=description or UNSET), params=models.ModelParams())`
    - `form.params.additional_properties = params`
    - Pass `base_model_id=UNSET` when `None`
    - Call `create_new_model_api_v1_models_create_post.asyncio_detailed(client=self._client, body=form)` → `handle_api_response(..., "model creation")`
  - `list(id: str | None = None) -> Any`
    - Call `get_models_api_v1_models_get.asyncio_detailed(client=self._client, id=id or UNSET)` → `handle_api_response(..., "models list")`
    - If JSON returned (parse gap), optionally coerce `[models.ModelModel.from_dict(d) for d in data]`
  - `get(model_id: str) -> models.ModelModel`
  - `toggle_active(model_id: str) -> models.ModelResponse | None`
  - `update(...) -> models.ModelModel` and `delete(model_id: str) -> bool`
- CLI wiring (in `openwebui/cli/main.py`):
  - `@cli.group() def model(): ...`
  - Subcommands: `create | list | get | toggle | update | delete`; follow folder/chat/kb patterns for prompts and JSON output.
- Tests
  - SDK: patch `...api.models.create_new_model_api_v1_models_create_post.asyncio_detailed` to return `Response(status_code=200, parsed=models.ModelModel(...))`; assert body is `ModelForm` and values were set.
  - CLI: patch `openwebui.cli.main.OpenWebUI` to return a mock with `models.create = AsyncMock(...)`; run `owui model create ...` and assert awaited kwargs.

## Examples: Payload assembly and response handling

- Flexible payloads with `additional_properties`
  - Chat create: use `GenerateChatCompletionOpenaiChatCompletionsPostFormData().additional_properties = {"model": model, "messages": [...], "stream": False}`
  - Persist chat: `ChatFormChat().additional_properties = {"models": [model], "messages": full_messages}` → wrap with `ChatForm(chat=..., folder_id=folder_id or UNSET)`
- Optional fields via `UNSET`
  - Build `QueryCollectionsForm(..., k=UNSET, k_reranker=UNSET, ...)` when optionals absent; avoids sending `null`
- Centralized response parsing
  - Use `handle_api_response` to normalize 2xx returns, raw JSON fallbacks, and to raise `AuthenticationError`, `NotFoundError`, or detailed 422 validation messages

## Gotchas and edge cases

- Generated client parse gaps: especially knowledge listing (`list_all`); always run through `handle_api_response`
- Preserve original user prompt in chat history; only the LLM call uses augmented RAG context
- For directory uploads, normalize paths to POSIX style for `.kbignore` matching and exclude the `.kbignore` file itself
- When adding new wrappers, always catch `httpx.ConnectError` and re‑raise `openwebui.exceptions.ConnectionError`

## File map (key references)

- SDK entry: `openwebui/client.py`
- Config: `openwebui/config.py`
- Exceptions: `openwebui/exceptions.py`
- Utils: `openwebui/utils/api_utils.py`, `openwebui/utils/kbignore_parser.py`
- APIs: `openwebui/api/folders.py`, `openwebui/api/chats.py`, `openwebui/api/knowledge.py` (add `models.py` for Models)
- CLI: `openwebui/cli/main.py`
- Generated client: `openwebui/open_web_ui_client/open_web_ui_client/*`
- Tests: `tests/sdk/*`, `tests/cli/*`, `tests/integration/*`

## Quality gates checklist

- Build: Python package compiles (no action required on docs-only changes)
- Lint/format: `uv run ruff check .` is clean; format diffs via `uv run ruff format .`
- Tests: Run relevant subsets; when adding public behavior, prefer adding/updating unit tests

## Maintainer preferences (implied by codebase)

- Async-first SDK (no sync wrappers)
- Thin, typed wrappers around generated client; no bespoke HTTP calls
- Centralized response/error handling via `handle_api_response`
- Click CLI with consistent UX across commands; avoid interactive prompts in JSON mode

---

If you’re adding a new high-level API group, mirror `folders.py` structure, use `handle_api_response`, and add CLI commands plus tests following the existing patterns.
