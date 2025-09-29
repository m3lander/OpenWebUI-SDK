# Copilot Instructions for OpenWebUI-SDK

This repo is an async-first Python SDK and CLI for Open WebUI. The SDK wraps a generated OpenAPI client, adds opinionated flows (e.g., RAG in chats), and exposes a Click-based CLI.

## Architecture and data flow
- Entry SDK: `openwebui/client.py` defines `OpenWebUI` which:
  - Loads config via `openwebui/config.py` (env > ./.owui/config.yaml > ~/.owui/config.yaml), trims trailing slash.
  - Instantiates the generated `AuthenticatedClient` from `openwebui/open_web_ui_client/open_web_ui_client`.
  - Wires high-level groups: `FoldersAPI`, `ChatsAPI`, `KnowledgeBaseAPI` from `openwebui/api/*`.
- Generated client: in `openwebui/open_web_ui_client/open_web_ui_client/*` (httpx, typed models, UNSET sentinel).
- Response handling: Use `openwebui/utils/api_utils.py:handle_api_response()` everywhere. It:
  - Returns `response.parsed` when available; returns decoded JSON on parse gaps; maps 401→AuthenticationError, 404→NotFoundError; 204→True.
- RAG flow: `openwebui/api/chats.py` augments user prompt when `kb_ids` provided by calling `KnowledgeBaseAPI.query()`; only the LLM call uses the augmented prompt—the saved chat history keeps the original user prompt.

## Conventions you must follow
- Always import and call generated endpoints from `openwebui/open_web_ui_client/open_web_ui_client/api/...` and route all results through `handle_api_response`.
- Use generated models (`...models.*`) and `UNSET` for optional fields. For payloads with flexible schemas, set `additional_properties` (see `ChatsAPI.create`).
- Keep SDK methods async and catch `httpx.ConnectError`, re-raising `openwebui.exceptions.ConnectionError`.
- Knowledge APIs respect `.kbignore` via `utils/kbignore_parser.py`; skip uploading the `.kbignore` file itself.
- Known client schema gap: `KnowledgeBaseAPI.list_all()` works around parsing by instantiating `models.KnowledgeResponse` from raw JSON. Preserve this pattern until the OpenAPI/schema is fixed.

## CLI behaviors (Click)
- CLI entry: `openwebui/cli/main.py` (script name `owui`). Global flags: `--verbose`, `--debug`, `--output {text,json}`.
- Commands:
  - `folder`: create | list | list-chats | delete
  - `chat`: create | continue | list (messages) | rename | delete
  - `kb`: create | list-kbs | list-files | upload-file | upload-dir | update-file | delete-file | delete-all-files
- Text mode asks for confirmation on destructive ops; `--yes` skips for some commands. JSON mode prints structured data and avoids interactive prompts.

## Build, test, and lint workflows
- Python >= 3.11. Install for dev:
  - `uv pip install -e .[dev]` (recommended) or `pip install -e .[dev]`.
- Run tests (async, CLI, integration configured via `pyproject.toml`):
  - All: `uv run pytest`
  - SDK: `uv run pytest tests/sdk/`
  - CLI: `uv run pytest tests/cli/`
  - Integration (needs live server): `uv run pytest tests/integration/`
  - Integration config: pass `--server-url`, or set `TEST_SERVER_URL`/`OPENWEBUI_URL` and `OPENWEBUI_API_KEY`.
- Lint/format: `uv run ruff check .` and `uv run ruff format .`.
- End-to-end demo: `run_full_scenario.sh` (requires configured server + `owui`).

## Configuration and environment
- Precedence: `OPENWEBUI_URL`, `OPENWEBUI_API_KEY` env vars > `./.owui/config.yaml` > `~/.owui/config.yaml` (see `openwebui/config.py`).
- `OpenWebUI()` can be constructed with overrides: `base_url`, `api_key`, `timeout`.

## Adding or updating endpoints (pattern)
- Create a thin async wrapper in `openwebui/api/<area>.py`:
  - Import the generated function and `models`.
  - Build the form/model (use `UNSET` for optional params; set `additional_properties` for free-form fields).
  - Call `...asyncio_detailed(...)` with `client=self._client` and pass `body`/`id` as needed.
  - Return `handle_api_response(response, "descriptive name")`.
- Example references:
  - Folders: `openwebui/api/folders.py` (list, create, delete)
  - Chats: `openwebui/api/chats.py` (create + LLM call, continue, rename, list_by_folder)
  - Knowledge: `openwebui/api/knowledge.py` (create, list_all workaround, upload_file, upload_directory with async batches)

## Regenerating the low-level client
- Use `generate_client.sh` or run `openapi-python-client generate --url http://<url>/openapi.json --output-path openwebui/open_web_ui_client --overwrite --meta uv`.
- After regeneration, verify impacted wrappers and tests—especially knowledge listing and any endpoints that rely on `additional_properties`.

## Examples
- Building a flexible payload with additional_properties (chat create):
  - Use `models.GenerateChatCompletionOpenaiChatCompletionsPostFormData()` and set `additional_properties = {"model": model, "messages": [...], "stream": False}` before calling `...openai_chat_completions_post.asyncio_detailed(...)`.
  - Save to server using `models.ChatFormChat()` with `chat_data.additional_properties = {"models": [model], "messages": full_messages}`; wrap with `models.ChatForm(chat=chat_data, folder_id=folder_id or UNSET)`.
- Optional fields via UNSET:
  - When constructing `models.QueryCollectionsForm(...)`, pass `k=UNSET` (etc.) if not provided to avoid sending nulls (see `KnowledgeBaseAPI.query`).
- Centralized response parsing:
  - Always `return handle_api_response(response, "descriptive name")`. This returns `parsed`, or decodes JSON when parsing fails (used by `list_all()` workaround), and raises typed errors on 401/404/422.
- RAG prompt augmentation (pattern to preserve history):
  - If `kb_ids` present, fetch chunks via `KnowledgeBaseAPI.query(...)`, build `retrieved_context = "\n\n---\n\n".join(chunk["content"])`, and send this augmented prompt to the LLM.
  - When saving to chat history, store the original user prompt, not the augmented one.
- Knowledge base listing workaround:
  - Because the generated client returns `parsed=None` on list, use `handle_api_response(...)` to get raw JSON then instantiate `models.KnowledgeResponse(**kb_dict)` for each entry.
- CLI wiring pattern (Click):
  - Top-level `@click.group()` sets `--verbose/--debug` and `--output {text,json}`. Subcommands call `OpenWebUI()` and `asyncio.run(async_fn(...))`.
  - In text mode, confirm destructive ops; in JSON mode, output minimal structured data via `format_output`.
- Respecting .kbignore during directory uploads:
  - Use `KBIgnoreParser` loaded from the directory’s `.kbignore`; skip the `.kbignore` file itself and use POSIX-style paths for matching.
- Tests and mocking:
  - Unit tests mock low-level `...asyncio_detailed` calls and return `MagicMock(spec=Response, status_code=200, parsed=...)`.
  - CLI tests patch `openwebui.cli.main.OpenWebUI` and assert awaited calls with correct kwargs; integration tests use `--server-url` or env vars and a session-scoped async client.

### Pattern: New high-level wrapper — Models
- Goal: Add `ModelsAPI` with simple methods that compose the generated endpoints.
- Generated endpoints available under `...api.models.*` include:
  - `create_new_model_api_v1_models_create_post`
  - `get_models_api_v1_models_get`, `get_model_by_id_api_v1_models_model_get`, `get_base_models_api_v1_models_base_get`
  - `update_model_by_id_api_v1_models_model_update_post`, `delete_model_by_id_api_v1_models_model_delete_delete`
  - `toggle_model_by_id_api_v1_models_model_toggle_post`, `sync_models_api_v1_models_sync_post`, `export_models_api_v1_models_export_get`

- SDK wrapper skeleton (follow Folders/Chats patterns; always use `handle_api_response` and catch `httpx.ConnectError`):
  - File: `openwebui/api/models.py`
  - Methods to start with:
    - `create(id: str, name: str, params: dict, description: str | None = None, base_model_id: str | None = None, is_active: bool = True) -> models.ModelModel`
    - `list(id: str | None = None) -> Any` (use `handle_api_response` to tolerate schema gaps)
    - `get(model_id: str) -> models.ModelModel`
    - `toggle_active(model_id: str) -> models.ModelResponse | None`
    - `update(model_id: str, name: str | None = None, params: dict | None = None, description: str | None = None, is_active: bool | None = None) -> models.ModelModel`
    - `delete(model_id: str) -> bool`

- Model creation pattern (payload assembly):
  - Use `models.ModelForm(...)` with `meta=models.ModelMeta(description=description or UNSET)` and `params=models.ModelParams()` then set `params.additional_properties = {...your params...}`.
  - For nullable optionals, pass `UNSET` when not provided (e.g., `base_model_id=UNSET`).
  - Call:
    - `await create_new_model_api_v1_models_create_post.asyncio_detailed(client=self._client, body=form)`
    - Return `handle_api_response(response, "model creation")`.

- Listing pattern with parse gaps:
  - `get_models_api_v1_models_get.asyncio_detailed(client=self._client, id=id or UNSET)` then `handle_api_response(response, "models list")`.
  - If the generated parser returns `parsed=None`, `handle_api_response` will return decoded JSON; convert items to `models.ModelModel(**d)` as needed.

- Toggle and delete patterns:
  - Toggle: `toggle_model_by_id_api_v1_models_model_toggle_post.asyncio_detailed(id=model_id, client=self._client)` → `handle_api_response(response, "model toggle")`.
  - Delete: `delete_model_by_id_api_v1_models_model_delete_delete.asyncio_detailed(id=model_id, client=self._client)` → `handle_api_response(response, "model deletion")` (returns True on 204/empty 2xx).

- CLI wiring (Click):
  - Add a `@cli.group()` called `model` with subcommands `create | list | get | toggle | update | delete`.
  - Map flags to SDK wrapper. In JSON mode, emit minimal structured data; in text mode, show confirmations and summaries (mirrors folder/chat/kb patterns).

- Minimal test example outlines:
  - SDK unit test: patch `...api.models.create_new_model_api_v1_models_create_post.asyncio_detailed` to return `Response(status_code=200, parsed=models.ModelModel(...))`, then assert `ModelsAPI.create(...)` returns a `ModelModel` and the call was awaited with `body=ModelForm(...)`.
  - CLI unit test: patch `openwebui.cli.main.OpenWebUI` to return a mock with `models.create = AsyncMock(...)`, invoke `owui model create ...`, and assert awaited kwargs match the CLI options.
