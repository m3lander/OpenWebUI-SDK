import sys
import asyncio
import logging
import json
from pathlib import Path  # Added for path operations in upload_dir & update_file
from typing import Optional, Any, List

import click
import httpx

# Import the main SDK client
from openwebui.client import OpenWebUI
from openwebui.exceptions import OpenWebUIError, NotFoundError, AuthenticationError, APIError

# Configure the 'openwebui' root logger
log = logging.getLogger(__name__)
log.setLevel(logging.WARNING)  # Default level for SDK unless flags are used

# Add the StreamHandler to stderr early and once
if not log.handlers:
    handler = logging.StreamHandler(sys.stderr)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    log.addHandler(handler)

logging.basicConfig(level=logging.DEBUG)

# --- Output Formatting Helper ---
def format_output(data: Any, output_format: str):
    """
    Formats data for output based on the specified format.
    Args:
        data: The data to format (Python dict, list, str, etc.).
        output_format (str): 'text' or 'json'.
    """
    if output_format == "json":
        # Ensure data is JSON-serializable. For models, convert to dict.
        # This involves recursively converting models if they contain other models.
        # A quick way is to try to_dict() for models, or assume simple dicts/lists.
        def to_json_compatible(obj):
            if hasattr(obj, "to_dict") and callable(obj.to_dict):
                return obj.to_dict()
            if isinstance(obj, (list, tuple)):
                return [to_json_compatible(item) for item in obj]
            if isinstance(obj, dict):
                return {k: to_json_compatible(v) for k, v in obj.items()}
            # Handle instances of dataclasses or other custom objects
            # that might be returned by the SDK but are not Click models.
            # Using __dict__ for generic objects.
            if hasattr(obj, "__dict__"):
                return {k: to_json_compatible(v) for k, v in obj.__dict__.items()}
            return obj

        click.echo(json.dumps(to_json_compatible(data), indent=2))
    else:  # Default to text output
        click.echo(data)


# --- Click CLI Structure ---


@click.group()
@click.option("--verbose", "-v", is_flag=True, help="Enable INFO level logging.")
@click.option("--debug", is_flag=True, help="Enable DEBUG level logging (more verbose).")
@click.option(
    "--output",
    type=click.Choice(["text", "json"], case_sensitive=False),
    default="text",
    help="Output format.",
)
@click.pass_context
def cli(ctx, verbose: bool, debug: bool, output: str):
    """
    A CLI tool for interacting with Open WebUI chats, folders, and knowledge bases.

    Configuration is loaded from ~/.owui/config.yaml, ./.owui/config.yaml,
    or environment variables.
    """
    log_level = logging.WARNING
    if debug:
        log_level = logging.DEBUG
    elif verbose:
        log_level = logging.INFO

    log.setLevel(log_level)
    logging.basicConfig()
    # Store output format in context object for subcommands
    ctx.ensure_object(dict)
    ctx.obj["OUTPUT_FORMAT"] = output

    pass  # No direct os.getenv checks here anymore


# --- Chat Command Group ---
@cli.group()
def chat():
    """Commands for managing chats."""
    pass

# create_chat_command_wrapper function (add new options for RAG settings)
@chat.command("create")
@click.argument("prompt")
@click.option("--model", "-m", default="gemini-1.5-flash", help="The model name to use.")
@click.option("--folder-id", help="Optional ID of the folder to add this chat to.")
@click.option(
    "--kb-id", "kb_ids",
    multiple=True,
    help="ID of a knowledge base to use for RAG. Can be specified multiple times."
)
@click.option("--k", type=int, help="Number of top hits to retrieve from the KB.")
@click.option("--k-reranker", type=int, help="Number of re-ranked hits from the KB.")
@click.option("--r", type=float, help="Relevance score threshold for KB retrieval (0.0 to 1.0).")
@click.option("--hybrid/--no-hybrid", default=None, type=bool, help="Enable/disable hybrid search for KB retrieval.")
@click.option("--hybrid-bm25-weight", type=float, help="Weight for BM25 in hybrid search (0.0 to 1.0).")
@click.pass_context
def create_chat_command_wrapper(
    ctx,
    prompt: str,
    model: str,
    folder_id: Optional[str],
    kb_ids: tuple[str],
    k: Optional[int],
    k_reranker: Optional[int],
    r: Optional[float],
    hybrid: Optional[bool],
    hybrid_bm25_weight: Optional[float],
):
    """Creates a new chat, optionally using one or more knowledge bases with RAG."""
    kb_id_list = list(kb_ids) if kb_ids else None
    asyncio.run(
        _create_chat_async(
            ctx,
            prompt,
            model,
            folder_id,
            kb_id_list,
            k,
            k_reranker,
            r,
            hybrid,
            hybrid_bm25_weight,
        )
    )

# _create_chat_async function (update signature to receive new RAG settings)
async def _create_chat_async(
    ctx,
    prompt: str,
    model: str,
    folder_id: Optional[str],
    kb_ids: Optional[List[str]],
    k: Optional[int],
    k_reranker: Optional[int],
    r: Optional[float],
    hybrid: Optional[bool],
    hybrid_bm25_weight: Optional[float],
):
    log.info(f"CLI: Attempting to create chat with prompt: '{prompt[:50]}...'")
    if kb_ids:
        log.info(f"CLI: Using knowledge bases: {kb_ids}")

    try:
        sdk = OpenWebUI()
        result_chat = await sdk.chats.create(
            model=model,
            prompt=prompt,
            folder_id=folder_id,
            kb_ids=kb_ids,
            k=k,
            k_reranker=k_reranker,
            r=r,
            hybrid=hybrid,
            hybrid_bm25_weight=hybrid_bm25_weight,
        )

        if ctx.obj["OUTPUT_FORMAT"] == "json":
            format_output(result_chat, ctx.obj["OUTPUT_FORMAT"])
        else:
            click.secho(
                f"✅ Success! New chat created with ID: {result_chat.id}", fg="bright_green", bold=True
            )
            last_message_content = ""
            if hasattr(result_chat, 'chat') and hasattr(result_chat.chat, 'additional_properties'):
                messages = result_chat.chat.additional_properties.get("messages", [])
                if messages:
                    last_message_content = messages[-1].get("content", "")
            click.secho("Assistant Response:", fg="cyan", bold=True)
            click.echo(last_message_content)
        log.info("CLI: Chat creation command completed successfully.")

    except (AuthenticationError, NotFoundError, APIError, httpx.RequestError, OpenWebUIError) as e:
        click.secho(f"An error occurred during chat creation: {e}", fg="red", err=True)
        if isinstance(e, httpx.HTTPStatusError):
            click.secho(f"Response: {e.response.text}", fg="red", err=True)
        log.error("CLI: Chat creation command failed.")
        raise click.Abort()


# continue_chat_command_wrapper function (add new options for RAG settings)
@chat.command("continue")
@click.argument("chat_id")
@click.argument("prompt")
@click.option(
    "--kb-id", "kb_ids",
    multiple=True,
    help="ID of a knowledge base to use for RAG. Can be specified multiple times."
)
@click.option("--k", type=int, help="Number of top hits to retrieve from the KB.")
@click.option("--k-reranker", type=int, help="Number of re-ranked hits from the KB.")
@click.option("--r", type=float, help="Relevance score threshold for KB retrieval (0.0 to 1.0).")
@click.option("--hybrid/--no-hybrid", default=None, type=bool, help="Enable/disable hybrid search for KB retrieval.")
@click.option("--hybrid-bm25-weight", type=float, help="Weight for BM25 in hybrid search (0.0 to 1.0).")
@click.pass_context
def continue_chat_command_wrapper(
    ctx,
    chat_id: str,
    prompt: str,
    kb_ids: tuple[str],
    k: Optional[int],
    k_reranker: Optional[int],
    r: Optional[float],
    hybrid: Optional[bool],
    hybrid_bm25_weight: Optional[float],
):
    """Continues an existing chat thread by its ID, optionally using RAG."""
    kb_id_list = list(kb_ids) if kb_ids else None
    asyncio.run(
        _continue_chat_async(
            ctx,
            chat_id,
            prompt,
            kb_id_list,
            k,
            k_reranker,
            r,
            hybrid,
            hybrid_bm25_weight,
        )
    )

# _continue_chat_async function (update signature to receive new RAG settings)
async def _continue_chat_async(
    ctx,
    chat_id: str,
    prompt: str,
    kb_ids: Optional[List[str]],
    k: Optional[int],
    k_reranker: Optional[int],
    r: Optional[float],
    hybrid: Optional[bool],
    hybrid_bm25_weight: Optional[float],
):
    log.info(f"CLI: Attempting to continue chat '{chat_id}' with prompt: '{prompt}...'")
    if kb_ids:
        log.info(f"CLI: Using knowledge bases: {kb_ids}")

    try:
        sdk = OpenWebUI()
        updated_chat = await sdk.chats.continue_chat(
            chat_id=chat_id,
            prompt=prompt,
            kb_ids=kb_ids,
            k=k,
            k_reranker=k_reranker,
            r=r,
            hybrid=hybrid,
            hybrid_bm25_weight=hybrid_bm25_weight,
        )

        if ctx.obj["OUTPUT_FORMAT"] == "json":
            format_output(updated_chat, ctx.obj["OUTPUT_FORMAT"])
        else:
            click.secho(f"✅ Success! Chat {updated_chat.id} updated.", fg="bright_green", bold=True)
            last_message_content = ""
            if hasattr(updated_chat, 'chat') and hasattr(updated_chat.chat, 'additional_properties'):
                messages = updated_chat.chat.additional_properties.get("messages", [])
                if messages:
                    last_message_content = messages[-1].get("content", "")
            click.secho("Assistant Response:", fg="cyan", bold=True)
            click.echo(last_message_content)
        log.info("CLI: Chat continuation command completed successfully.")

    except (AuthenticationError, NotFoundError, APIError, httpx.RequestError, OpenWebUIError) as e:
        click.secho(f"An error occurred during chat continuation: {e}", fg="red", err=True)
        if isinstance(e, httpx.HTTPStatusError):
            click.secho(f"Response: {e.response.text}", fg="red", err=True)
        log.error("CLI: Chat continuation command failed.")
        raise click.Abort()

@chat.command("list")
@click.argument("chat_id")  # This lists messages OF a specific chat
@click.pass_context
def list_messages_command_wrapper(ctx, chat_id: str):
    """Lists all messages (threads) in a given chat."""
    asyncio.run(_list_messages_async(ctx, chat_id))


async def _list_messages_async(ctx, chat_id: str):
    log.info(f"CLI: Attempting to list messages for chat ID: {chat_id}")
    try:
        sdk = OpenWebUI()
        chat_details = await sdk.chats.get(chat_id)

        if ctx.obj["OUTPUT_FORMAT"] == "json":
            format_output(chat_details, ctx.obj["OUTPUT_FORMAT"])
        else:
            click.secho(f"Messages for Chat '{chat_details.title}'", bold=True)
            click.echo("---")
            if hasattr(chat_details, "chat") and hasattr(chat_details.chat, "additional_properties"):
                for message in chat_details.chat.additional_properties.get("messages", []):
                    role = message.get("role")
                    content = message.get("content")
                    color = "blue" if role == "user" else "cyan"
                    click.secho(f"{role.capitalize()}:", fg=color, bold=True)
                    click.echo(f"{content}\n")
        log.info("CLI: Message listing command completed successfully.")

    except (AuthenticationError, NotFoundError, APIError, httpx.RequestError, OpenWebUIError) as e:
        click.secho(f"An error occurred while listing messages: {e}", fg="red", err=True)
        if isinstance(e, httpx.HTTPStatusError):
            click.secho(f"Response: {e.response.text}", fg="red", err=True)
        log.error("CLI: Message listing command failed.")
        raise click.Abort()


@chat.command("rename")
@click.argument("chat_id")
@click.argument("new_title")
@click.pass_context
def rename_chat_command_wrapper(ctx, chat_id: str, new_title: str):
    """Renames (sets a new title for) a chat."""
    asyncio.run(_rename_chat_async(ctx, chat_id, new_title))


async def _rename_chat_async(ctx, chat_id: str, new_title: str):
    log.info(f"CLI: Attempting to rename chat '{chat_id}' to '{new_title}'.")
    try:
        sdk = OpenWebUI()
        updated_chat = await sdk.chats.rename(chat_id=chat_id, new_title=new_title)

        if ctx.obj["OUTPUT_FORMAT"] == "json":
            format_output(updated_chat, ctx.obj["OUTPUT_FORMAT"])
        else:
            # Assuming updated_chat has a 'title' attribute
            click.secho(f"✅ Chat '{chat_id}' renamed to '{updated_chat.title}'.", fg="green")
        log.info("CLI: Chat rename command completed successfully.")
    except (AuthenticationError, NotFoundError, APIError, httpx.RequestError, OpenWebUIError) as e:
        click.secho(f"An error occurred during chat renaming: {e}", fg="red", err=True)
        if isinstance(e, httpx.HTTPStatusError):
            click.secho(f"Response: {e.text}", fg="red", err=True)
        log.error("CLI: Chat rename command failed.")
        raise click.Abort()


@chat.command("delete")
@click.argument("chat_id")
@click.pass_context
def delete_chat_command_wrapper(ctx, chat_id: str):
    """Deletes a chat by its ID."""
    asyncio.run(_delete_chat_async(ctx, chat_id))


async def _delete_chat_async(ctx, chat_id: str):
    if ctx.obj["OUTPUT_FORMAT"] == "text" and not click.confirm(
        f"Are you sure you want to delete chat '{chat_id}'? This action cannot be undone."
    ):
        click.echo("Aborted.")
        raise click.Abort()

    log.info(f"CLI: Attempting to delete chat ID: {chat_id}")
    try:
        sdk = OpenWebUI()
        success = await sdk.chats.delete(chat_id=chat_id)

        if ctx.obj["OUTPUT_FORMAT"] == "json":
            format_output({"id": chat_id, "deleted": success}, ctx.obj["OUTPUT_FORMAT"])
        else:
            if success:
                click.secho(f"✅ Chat '{chat_id}' deleted successfully.", fg="green")
            else:
                click.secho(f"❌ Failed to delete chat '{chat_id}'.", fg="red", err=True)

        if not success:  # Always abort if SDK reports non-success in text mode
            log.error("CLI: Chat deletion command failed (SDK reported not successful).")
            # For JSON output, we already outputted success: false, no need for another message
            if ctx.obj["OUTPUT_FORMAT"] == "text":
                raise click.Abort()
        log.info("CLI: Chat deletion command completed successfully.")

    except (AuthenticationError, NotFoundError, APIError, httpx.RequestError, OpenWebUIError) as e:
        click.secho(f"An error occurred during chat deletion: {e}", fg="red", err=True)
        if isinstance(e, httpx.HTTPStatusError):
            click.secho(f"Response: {e.text}", fg="red", err=True)
        log.error("CLI: Chat deletion command failed.")
        raise click.Abort()


# --- Folder Command Group ---
@cli.group()
def folder():
    """Commands for managing folders."""
    pass


@folder.command("create")
@click.argument("name")
@click.pass_context
def create_folder_command_wrapper(ctx, name: str):
    """Creates a new folder."""
    asyncio.run(_create_folder_async(ctx, name))


async def _create_folder_async(ctx, name: str):
    log.info(f"CLI: Attempting to create folder with name: '{name}'.")
    try:
        sdk = OpenWebUI()
        new_folder = await sdk.folders.create(name=name)

        if ctx.obj["OUTPUT_FORMAT"] == "json":
            format_output(new_folder, ctx.obj["OUTPUT_FORMAT"])
        else:
            # Assuming new_folder has an 'id' attribute or is dict-like
            folder_id_to_display = (
                new_folder.get("id")
                if isinstance(new_folder, dict)
                else getattr(new_folder, "id", "Unknown ID")
            )
            click.secho(f"✅ Folder '{name}' created with ID: {folder_id_to_display}", fg="green")
        log.info("CLI: Folder creation command completed successfully.")
    except (AuthenticationError, APIError, httpx.RequestError, OpenWebUIError) as e:
        click.secho(f"An error occurred during folder creation: {e}", fg="red", err=True)
        if isinstance(e, httpx.HTTPStatusError):
            click.secho(f"Response: {e.text}", fg="red", err=True)
        log.error("CLI: Folder creation command failed.")
        raise click.Abort()


@folder.command("list")
@click.pass_context
def list_all_folders_command_wrapper(ctx):
    """Lists all available folders."""
    asyncio.run(_list_all_folders_async(ctx))


async def _list_all_folders_async(ctx):
    log.info("CLI: Attempting to list all folders.")
    try:
        sdk = OpenWebUI()
        folders = await sdk.folders.list()

        if ctx.obj["OUTPUT_FORMAT"] == "json":
            format_output(folders, ctx.obj["OUTPUT_FORMAT"])
        else:
            if not folders:
                click.echo("No folders found on the server.")
                log.info("CLI: No folders found.")
                return

            click.secho("Available Folders:", bold=True)
            for folder_item in folders:
                # Accessing attributes directly assuming models.FolderModel
                folder_id = folder_item.id
                folder_name = folder_item.name or "Unnamed Folder"
                click.echo(f"  - ID: {folder_id}, Name: {folder_name}")
            log.info(f"CLI: Folder listing command completed successfully. Found {len(folders)} folders.")

    except (AuthenticationError, APIError, httpx.RequestError, OpenWebUIError) as e:
        click.secho(f"An error occurred while listing folders: {e}", fg="red", err=True)
        if isinstance(e, httpx.HTTPStatusError):
            click.secho(f"Response: {e.text}", fg="red", err=True)
        log.error("CLI: Folder listing command failed.")
        raise click.Abort()


@folder.command("list-chats")
@click.argument("folder_id")
@click.pass_context
def list_chats_in_folder_command_wrapper(ctx, folder_id: str):
    """Lists all chat IDs and titles within a specific folder."""
    asyncio.run(_list_chats_in_folder_async(ctx, folder_id))


async def _list_chats_in_folder_async(ctx, folder_id: str):
    log.info(f"CLI: Attempting to list chats in folder ID: {folder_id}")
    try:
        sdk = OpenWebUI()
        chats_in_folder = await sdk.chats.list_by_folder(folder_id=folder_id)

        if ctx.obj["OUTPUT_FORMAT"] == "json":
            format_output(chats_in_folder, ctx.obj["OUTPUT_FORMAT"])
        else:
            if not chats_in_folder:
                click.echo(f"No chats found in folder '{folder_id}'.")
                log.info(f"CLI: No chats found in folder '{folder_id}'.")
                return

            click.secho(f"Chats in folder '{folder_id}':", bold=True)
            for chat_item in chats_in_folder:
                # Accessing attributes directly assuming models.ChatTitleIdResponse
                click.echo(f"  - ID: {chat_item.id}, Title: {chat_item.title}")
            log.info(
                f"CLI: Listing chats in folder command completed successfully. Found {len(chats_in_folder)} chats."
            )

    except (AuthenticationError, NotFoundError, APIError, httpx.RequestError, OpenWebUIError) as e:
        click.secho(f"An error occurred while listing chats in folder: {e}", fg="red", err=True)
        if isinstance(e, httpx.HTTPStatusError):
            click.secho(f"Response: {e.text}", fg=True, err=True)
        log.error("CLI: Listing chats in folder command failed.")
        raise click.Abort()


@folder.command("delete")
@click.argument("folder_id")
@click.pass_context
def delete_folder_command_wrapper(ctx, folder_id: str):
    """Deletes a folder by its ID."""
    asyncio.run(_delete_folder_async(ctx, folder_id))


async def _delete_folder_async(ctx, folder_id: str):
    if ctx.obj["OUTPUT_FORMAT"] == "text" and not click.confirm(
        f"Are you sure you want to delete folder '{folder_id}'?"
    ):
        click.echo("Aborted.")
        raise click.Abort()

    log.info(f"CLI: Attempting to delete folder ID: {folder_id}")
    try:
        sdk = OpenWebUI()
        success = await sdk.folders.delete(folder_id=folder_id)

        if ctx.obj["OUTPUT_FORMAT"] == "json":
            format_output({"id": folder_id, "deleted": success}, ctx.obj["OUTPUT_FORMAT"])
        else:
            if success:
                click.secho(f"✅ Folder '{folder_id}' deleted successfully.", fg="green")
            else:
                click.secho(f"❌ Failed to delete folder '{folder_id}'.", fg="red", err=True)

        if not success:  # Always abort if SDK reports non-success in text mode
            log.error("CLI: Folder deletion command failed (SDK reported not successful).")
            if ctx.obj["OUTPUT_FORMAT"] == "text":
                raise click.Abort()
        log.info("CLI: Folder deletion command completed successfully.")

    except (AuthenticationError, NotFoundError, APIError, httpx.RequestError, OpenWebUIError) as e:
        click.secho(f"An error occurred during folder deletion: {e}", fg="red", err=True)
        if isinstance(e, httpx.HTTPStatusError):
            click.secho(f"Response: {e.text}", fg="red", err=True)
        log.error("CLI: Folder deletion command failed.")
        raise click.Abort()


# --- NEW: Knowledge Base Command Group ---
@cli.group()
def kb():
    """Commands for managing knowledge bases and files."""
    pass


@kb.command("create")
@click.argument("name")
@click.option("--description", help="Description for the new knowledge base.")
@click.pass_context
def create_kb_command_wrapper(ctx, name: str, description: Optional[str]):
    """
    Creates a new knowledge base.
    """
    asyncio.run(_create_kb_async(ctx, name, description))


async def _create_kb_async(ctx, name: str, description: Optional[str]):
    log.info(f"CLI: Creating Knowledge Base: {name}")
    try:
        sdk = OpenWebUI()
        # Assuming sdk.knowledge.create returns a model with .id, .name, .description
        kb_info = await sdk.knowledge.create(name, description)

        if ctx.obj["OUTPUT_FORMAT"] == "json":
            # Convert the KB info object to a dictionary for JSON output
            kb_dict = {
                "id": kb_info.id,
                "name": kb_info.name,
                "description": getattr(kb_info, "description", None),  # Safely get description
            }
            format_output(kb_dict, ctx.obj["OUTPUT_FORMAT"])
        else:
            click.secho("✅ Successfully created Knowledge Base:", fg="green")
            click.echo(f"  Name: {kb_info.name}")
            click.echo(f"  ID:   {kb_info.id}")
            if hasattr(kb_info, "description") and kb_info.description:
                click.echo(f"  Desc: {kb_info.description}")
        log.info("CLI: Knowledge Base creation command completed successfully.")
    except (AuthenticationError, APIError, httpx.RequestError, OpenWebUIError) as e:
        click.secho(f"Error creating Knowledge Base: {e}", fg="red", err=True)
        if isinstance(e, httpx.HTTPStatusError):
            click.secho(f"Response: {e.response.text}", fg="red", err=True)
        log.error("CLI: Knowledge Base creation command failed.")
        raise click.Abort()  # Abort the CLI execution on error


@kb.command("list-kbs")
@click.pass_context
def list_kbs_command_wrapper(ctx):
    """
    Lists all available knowledge bases.
    """
    asyncio.run(_list_kbs_async(ctx))


async def _list_kbs_async(ctx):
    log.info("CLI: Attempting to list all knowledge bases.")
    try:
        sdk = OpenWebUI()
        # Assuming sdk.knowledge.list_all returns a list of models.KnowledgeBase
        kbs = await sdk.knowledge.list_all()

        if ctx.obj["OUTPUT_FORMAT"] == "json":
            kbs_list_dicts = []
            for kb_found in kbs:
                kb_data = {
                    "id": kb_found.id,
                    "name": kb_found.name,
                    "description": getattr(kb_found, "description", None),
                }
                kbs_list_dicts.append(kb_data)
            format_output(kbs_list_dicts, ctx.obj["OUTPUT_FORMAT"])
        else:
            if not kbs:
                click.echo("No knowledge bases found on the server.")
                log.info("CLI: No knowledge bases found.")
                return

            click.secho("Found Knowledge Bases:", bold=True)
            for kb_item in kbs:
                click.echo(f"  - Name: {kb_item.name}")
                click.echo(f"  ID:   {kb_item.id}")
                if hasattr(kb_item, "description") and kb_item.description:
                    click.echo(f"  Desc: {kb_item.description}")
                click.echo("-" * 20)  # Separator for readability
        log.info("CLI: Knowledge base listing command completed successfully.")
    except (AuthenticationError, NotFoundError, APIError, httpx.RequestError, OpenWebUIError) as e:
        click.secho(f"An error occurred while listing knowledge bases: {e}", fg="red", err=True)
        if isinstance(e, httpx.HTTPStatusError):
            click.secho(f"Response: {e.response.text}", fg="red", err=True)
        log.error("CLI: Knowledge base listing command failed.")
        raise click.Abort()


@kb.command("list-files")
@click.argument("kb_id")
@click.pass_context
def list_kb_files_command_wrapper(ctx, kb_id: str):
    """
    Lists files for a specific knowledge base.
    """
    asyncio.run(_list_kb_files_async(ctx, kb_id))


async def _list_kb_files_async(ctx, kb_id: str):
    log.info(f"CLI: Listing files for KB '{kb_id}'...")
    try:
        sdk = OpenWebUI()
        # Assuming sdk.knowledge.list_files returns a list of models.FileMetadataResponse
        files = await sdk.knowledge.list_files(kb_id)

        if ctx.obj["OUTPUT_FORMAT"] == "json":
            files_list_dicts = []
            for f in files:
                # Accessing additional_properties safely. Assumes it's a dict.
                additional_meta = getattr(getattr(f, "meta", None), "additional_properties", {})
                file_dict = {
                    "id": f.id,
                    "filename": additional_meta.get("name", "[Filename Missing]"),
                    "filepath": additional_meta.get("collection_name", "[Filepath Missing]"),
                    "mime_type": additional_meta.get("content_type", "[MIME Type Missing]"),
                    "size": additional_meta.get("size", 0),  # Default size to 0
                    "meta_raw": additional_meta,
                }
                files_list_dicts.append(file_dict)
            format_output(files_list_dicts, ctx.obj["OUTPUT_FORMAT"])
        else:
            if not files:
                click.echo(f"No files found for Knowledge Base '{kb_id}'")
                return

            click.secho(f"Found {len(files)} Files for KB '{kb_id}':", bold=True)
            for f in files:
                # Accessing additional_properties safely
                additional_meta = getattr(getattr(f, "meta", None), "additional_properties", {})

                filename = additional_meta.get("name", "[Filename Missing]")
                filepath = additional_meta.get("collection_name", "[Filepath Missing]")

                click.echo(f"  - Filename: {filename}")
                click.echo(f"    ID:       {f.id}")
                click.echo(f"    Path:     {filepath}")
                click.echo("-" * 20)
        log.info("CLI: Knowledge Base file listing command completed successfully.")
    except (AuthenticationError, NotFoundError, APIError, httpx.RequestError, OpenWebUIError) as e:
        click.secho(f"Error listing files for KB '{kb_id}': {e}", fg="red", err=True)
        if isinstance(e, httpx.HTTPStatusError):
            click.secho(f"Response: {e.response.text}", fg="red", err=True)
        log.error("CLI: Knowledge Base file listing command failed.")
        raise click.Abort()


@kb.command("upload-file")
@click.argument("file_path", type=click.Path(exists=True, dir_okay=False, resolve_path=True))
@click.option("--kb-id", required=True, help="ID of the knowledge base to add the file to.")
@click.pass_context
def upload_file_command_wrapper(ctx, file_path: str, kb_id: str):
    """
    Uploads a single file to a specified knowledge base.
    """
    asyncio.run(_upload_file_async(ctx, file_path, kb_id))


async def _upload_file_async(ctx, file_path_str: str, kb_id: str):
    file_path = Path(file_path_str)
    log.info(f"CLI: Uploading file: {file_path.name} to KB '{kb_id}'")
    try:
        sdk = OpenWebUI()
        # Assuming sdk.knowledge.upload_file returns FileModelResponse
        uploaded_file = await sdk.knowledge.upload_file(file_path, kb_id)

        if ctx.obj["OUTPUT_FORMAT"] == "json":
            # Convert uploaded_file (model) to dict for JSON output
            format_output(
                {"id": uploaded_file.id, "filename": uploaded_file.filename}, ctx.obj["OUTPUT_FORMAT"]
            )
        else:
            click.secho(
                f"✅ Successfully uploaded '{uploaded_file.filename}' (ID: {uploaded_file.id}) to KB '{kb_id}'.",
                fg="green",
            )
        log.info("CLI: File upload command completed successfully.")
    except (
        AuthenticationError,
        NotFoundError,
        APIError,
        httpx.RequestError,
        OpenWebUIError,
        FileNotFoundError,
    ) as e:
        click.secho(f"Error uploading file: {e}", fg="red", err=True)
        if isinstance(e, httpx.HTTPStatusError):
            click.secho(f"Response: {e.response.text}", fg="red", err=True)
        log.error("CLI: File upload command failed.")
        raise click.Abort()


@kb.command("upload-dir")
@click.argument("directory_path", type=click.Path(exists=True, file_okay=False, resolve_path=True))
@click.option("--kb-id", required=True, help="ID of the knowledge base to add the files to.")
@click.option(
    "--ignore-file",
    type=click.Path(exists=True, dir_okay=False, resolve_path=True),
    help="Path to a .kbignore file. Defaults to .kbignore in the directory_path if not specified.",
)
@click.pass_context
def upload_dir_command_wrapper(ctx, directory_path: str, kb_id: str, ignore_file: Optional[str]):
    """
    Uploads files from a directory to a specified knowledge base, respecting .kbignore.
    """
    asyncio.run(_upload_dir_async(ctx, directory_path, kb_id, ignore_file))


async def _upload_dir_async(ctx, directory_path_str: str, kb_id: str, ignore_file_str: Optional[str]):
    directory_path = Path(directory_path_str)
    ignore_file_path = Path(ignore_file_str) if ignore_file_str else None

    # Path to os.path for walk logic. This imports should be at the top of file
    log.info(f"CLI: Uploading directory: {directory_path.name} to KB '{kb_id}'")
    try:
        sdk = OpenWebUI()
        # Assuming sdk.knowledge.upload_directory returns List[FileModelResponse]
        uploaded_files = await sdk.knowledge.upload_directory(directory_path, kb_id, ignore_file_path)

        if ctx.obj["OUTPUT_FORMAT"] == "json":
            files_list_dicts = [{"id": f.id, "filename": f.filename} for f in uploaded_files]
            format_output(files_list_dicts, ctx.obj["OUTPUT_FORMAT"])
        else:
            click.secho(
                f"✅ Successfully uploaded {len(uploaded_files)} files from '{directory_path.name}' to KB '{kb_id}'.",
                fg="green",
            )
        log.info("CLI: Directory upload command completed successfully.")
    except (
        AuthenticationError,
        NotFoundError,
        APIError,
        httpx.RequestError,
        OpenWebUIError,
        NotADirectoryError,
    ) as e:
        click.secho(f"Error uploading directory: {e}", fg="red", err=True)
        if isinstance(e, httpx.HTTPStatusError):
            click.secho(f"Response: {e.response.text}", fg="red", err=True)
        log.error("CLI: Directory upload command failed.")
        raise click.Abort()


@kb.command("update-file")
@click.argument("file_id")
@click.argument("new_file_path", type=click.Path(exists=True, dir_okay=False, resolve_path=True))
@click.pass_context
def update_file_command_wrapper(ctx, file_id: str, new_file_path: str):
    """
    Updates the content of an existing file by its OpenWebUI ID.
    """
    asyncio.run(_update_file_async(ctx, file_id, new_file_path))


async def _update_file_async(ctx, file_id: str, new_file_path_str: str):
    new_file_path = Path(new_file_path_str)
    log.info(f"CLI: Updating file ID: {file_id} with content from {new_file_path.name}")
    try:
        sdk = OpenWebUI()
        # Assuming sdk.knowledge.update_file returns FileModelResponse
        updated_file = await sdk.knowledge.update_file(file_id, new_file_path)

        if ctx.obj["OUTPUT_FORMAT"] == "json":
            format_output(
                {"id": updated_file.id, "filename": updated_file.filename}, ctx.obj["OUTPUT_FORMAT"]
            )
        else:
            click.secho(
                f"✅ Successfully updated content for '{updated_file.filename}' (ID: {updated_file.id}).",
                fg="green",
            )
        log.info("CLI: File update command completed successfully.")
    except (
        AuthenticationError,
        NotFoundError,
        APIError,
        httpx.RequestError,
        OpenWebUIError,
        FileNotFoundError,
    ) as e:
        click.secho(f"Error updating file content: {e}", fg="red", err=True)
        if isinstance(e, httpx.HTTPStatusError):
            click.secho(f"Response: {e.response.text}", fg="red", err=True)
        log.error("CLI: File update command failed.")
        raise click.Abort()


@kb.command("delete-file")
@click.argument("file_id")
@click.pass_context
def delete_file_command_wrapper(ctx, file_id: str):
    """
    Deletes a file by its OpenWebUI ID.
    """
    asyncio.run(_delete_file_async(ctx, file_id))


async def _delete_file_async(ctx, file_id: str):
    if ctx.obj["OUTPUT_FORMAT"] == "text" and not click.confirm(
        f"Are you sure you want to delete file '{file_id}'?"
    ):
        click.echo("Aborted.")
        raise click.Abort()

    log.info(f"CLI: Deleting file ID: {file_id}")
    try:
        sdk = OpenWebUI()
        success = await sdk.knowledge.delete_file(file_id)

        if ctx.obj["OUTPUT_FORMAT"] == "json":
            format_output({"id": file_id, "deleted": success}, ctx.obj["OUTPUT_FORMAT"])
        else:
            if success:
                click.secho(f"✅ Successfully deleted file with ID: {file_id}.", fg="green")
            else:
                click.secho(f"❌ Failed to delete file with ID: {file_id}.", fg="red", err=True)

        if not success:  # Always abort if SDK reports non-success in text mode
            log.error("CLI: File deletion command failed (SDK reported not successful).")
            if ctx.obj["OUTPUT_FORMAT"] == "text":
                raise click.Abort()
        log.info("CLI: File deletion command completed successfully.")
    except (AuthenticationError, NotFoundError, APIError, httpx.RequestError, OpenWebUIError) as e:
        click.secho(f"Error deleting file: {e}", fg="red", err=True)
        if isinstance(e, httpx.HTTPStatusError):
            click.secho(f"Response: {e.response.text}", fg="red", err=True)
        log.error("CLI: File deletion command failed.")
        raise click.Abort()


@kb.command("delete-all-files")
@click.argument("kb_id")
@click.option("--yes", is_flag=True, help="Skip confirmation prompt.")
@click.pass_context
def delete_all_files_command_wrapper(ctx, kb_id: str, yes: bool):
    """
    Deletes ALL files belonging to a specified knowledge base.
    This action is irreversible.
    """
    asyncio.run(_delete_all_files_async(ctx, kb_id, yes))


async def _delete_all_files_async(ctx, kb_id: str, yes: bool):
    log.info(f"CLI: Attempting to delete all files from Knowledge Base ID: {kb_id}")

    if ctx.obj["OUTPUT_FORMAT"] == "text" and not yes:
        click.secho(
            click.style(
                f"WARNING: This will delete ALL files from Knowledge Base '{kb_id}'. This action is irreversible!",
                fg="red",
                bold=True,
            )
        )
        if not click.confirm("Are you sure you want to proceed?"):
            click.echo("Operation cancelled.")
            raise click.Abort()

    try:
        sdk = OpenWebUI()
        deletion_summary = await sdk.knowledge.delete_all_files_from_kb(kb_id)

        if ctx.obj["OUTPUT_FORMAT"] == "json":
            format_output(deletion_summary, ctx.obj["OUTPUT_FORMAT"])
        else:
            click.secho(f"\nDeletion summary for Knowledge Base '{kb_id}':", bold=True)
            click.echo(f"  - Successfully deleted: {deletion_summary.get('successful', 0)}")
            if deletion_summary.get("failed", 0) > 0:
                click.secho(f"  - Failed to delete: {deletion_summary.get('failed', 0)}", fg="red")
                click.secho(
                    f"❌ Completed with {deletion_summary.get('failed', 0)} errors during deletion.",
                    fg="red",
                    err=True,
                )
                raise click.Abort()  # Abort CLI on partial failure for batch delete
            else:
                click.secho("✅ All files deleted successfully.", fg="green")
        log.info("CLI: All files deletion command completed successfully.")
    except (AuthenticationError, NotFoundError, APIError, httpx.RequestError, OpenWebUIError) as e:
        click.secho(f"Error deleting all files from KB '{kb_id}': {e}", fg="red", err=True)
        if isinstance(e, httpx.HTTPStatusError):
            click.secho(f"Response: {e.response.text}", fg="red", err=True)
        log.error("CLI: All files deletion command failed.")
        raise click.Abort()


if __name__ == "__main__":
    cli()
