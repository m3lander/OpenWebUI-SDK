import sys
import asyncio
import logging
import json
from typing import Optional, Any

import click
import httpx
# from dotenv import load_dotenv # REMOVED: No longer load dotenv here, get_config() handles it

# Import the main SDK client
from openwebui.client import OpenWebUI
from openwebui.exceptions import OpenWebUIError, NotFoundError, AuthenticationError, APIError

# Configure the 'openwebui' root logger
log = logging.getLogger("openwebui")
log.setLevel(logging.WARNING)  # Default level for SDK unless flags are used

# Add the StreamHandler to stderr early and once
if not log.handlers:
    handler = logging.StreamHandler(sys.stderr)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    log.addHandler(handler)


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
            # Handle instances of dataclasses that are not from generated client
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
    A CLI tool for interacting with Open WebUI chats and folders.

    Configuration is loaded from ~/.owui/config.yaml, ./.owui/config.yaml,
    or environment variables.
    """
    log_level = logging.WARNING
    if debug:
        log_level = logging.DEBUG
    elif verbose:
        log_level = logging.INFO

    log.setLevel(log_level)

    # Store output format in context object for subcommands
    ctx.ensure_object(dict)
    ctx.obj["OUTPUT_FORMAT"] = output

    # Pre-flight check (will now be handled by OpenWebUI() directly)
    # The SDK will raise ValueError if config is missing, which will
    # be caught by the command's try/except block.
    pass  # No direct os.getenv checks here anymore


# --- Chat Command Group ---
@cli.group()
def chat():
    """Commands for managing chats."""
    pass


@chat.command("create")
@click.argument("prompt")
@click.option("--model", "-m", default="gemini-1.5-flash", help="The model name to use.")
@click.option("--folder-id", help="Optional ID of the folder to add this chat to.")
@click.pass_context
def create_chat(ctx, prompt: str, model: str, folder_id: Optional[str]):
    """Creates a new chat, gets a response, and saves it to Open WebUI."""
    log.info(f"CLI: Attempting to create chat with prompt: '{prompt[:50]}...'")
    try:
        sdk = OpenWebUI()
        result_chat = asyncio.run(sdk.chats.create(model=model, prompt=prompt, folder_id=folder_id))

        if ctx.obj["OUTPUT_FORMAT"] == "json":
            format_output(result_chat, ctx.obj["OUTPUT_FORMAT"])
        else:
            click.secho(
                f"✅ Success! New chat created with ID: {result_chat.id}", fg="bright_green", bold=True
            )
            last_message_content = result_chat.chat.additional_properties.get("messages", [])[-1].get(
                "content", ""
            )
            click.secho("Assistant Response:", fg="cyan", bold=True)
            click.echo(last_message_content)
        log.info("CLI: Chat creation command completed successfully.")

    except (AuthenticationError, NotFoundError, APIError, httpx.RequestError, OpenWebUIError) as e:
        click.secho(f"An error occurred during chat creation: {e}", fg="red", err=True)
        if isinstance(e, httpx.HTTPStatusError):
            click.secho(f"Response: {e.response.text}", fg="red", err=True)
        log.error("CLI: Chat creation command failed.")
        raise click.Abort()


@chat.command("continue")
@click.argument("chat_id")
@click.argument("prompt")
@click.pass_context
def continue_chat(ctx, chat_id: str, prompt: str):
    """Continues an existing chat thread by its ID."""
    log.info(f"CLI: Attempting to continue chat '{chat_id}' with prompt: '{prompt[:50]}...'")
    try:
        sdk = OpenWebUI()
        updated_chat = asyncio.run(sdk.chats.continue_chat(chat_id=chat_id, prompt=prompt))

        if ctx.obj["OUTPUT_FORMAT"] == "json":
            format_output(updated_chat, ctx.obj["OUTPUT_FORMAT"])
        else:
            click.secho(f"✅ Success! Chat {updated_chat.id} updated.", fg="bright_green", bold=True)
            last_message_content = updated_chat.chat.additional_properties.get("messages", [])[-1].get(
                "content", ""
            )
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
def list_messages(ctx, chat_id: str):
    """Lists all messages (threads) in a given chat."""
    log.info(f"CLI: Attempting to list messages for chat ID: {chat_id}")
    try:
        sdk = OpenWebUI()
        chat_details = asyncio.run(sdk.chats.get(chat_id))

        if ctx.obj["OUTPUT_FORMAT"] == "json":
            format_output(chat_details, ctx.obj["OUTPUT_FORMAT"])
        else:
            click.secho(f"Messages for Chat '{chat_details.title}'", bold=True)
            click.echo("---")
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
def rename_chat(ctx, chat_id: str, new_title: str):
    """Renames (sets a new title for) a chat."""
    log.info(f"CLI: Attempting to rename chat '{chat_id}' to '{new_title}'.")
    try:
        sdk = OpenWebUI()
        updated_chat = asyncio.run(sdk.chats.rename(chat_id=chat_id, new_title=new_title))

        if ctx.obj["OUTPUT_FORMAT"] == "json":
            format_output(updated_chat, ctx.obj["OUTPUT_FORMAT"])
        else:
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
def delete_chat(ctx, chat_id: str):
    """Deletes a chat by its ID."""
    if ctx.obj["OUTPUT_FORMAT"] == "text" and not click.confirm(
        f"Are you sure you want to delete chat '{chat_id}'? This action cannot be undone."
    ):
        click.echo("Aborted.")
        raise click.Abort()

    log.info(f"CLI: Attempting to delete chat ID: {chat_id}")
    try:
        sdk = OpenWebUI()
        success = asyncio.run(sdk.chats.delete(chat_id=chat_id))

        if ctx.obj["OUTPUT_FORMAT"] == "json":
            format_output({"id": chat_id, "deleted": success}, ctx.obj["OUTPUT_FORMAT"])
        else:
            if success:
                click.secho(f"✅ Chat '{chat_id}' deleted successfully.", fg="green")
            else:
                click.secho(f"❌ Failed to delete chat '{chat_id}'.", fg="red", err=True)

        if not success:  # Always abort if SDK reports non-success
            log.error("CLI: Chat deletion command failed (SDK reported not successful).")
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
def create_folder(ctx, name: str):
    """Creates a new folder."""
    log.info(f"CLI: Attempting to create folder with name: '{name}'.")
    try:
        sdk = OpenWebUI()
        new_folder = asyncio.run(sdk.folders.create(name=name))

        if ctx.obj["OUTPUT_FORMAT"] == "json":
            format_output(new_folder, ctx.obj["OUTPUT_FORMAT"])
        else:
            click.secho(f"✅ Folder '{name}' created with ID: {new_folder.get('id')}", fg="green")
        log.info("CLI: Folder creation command completed successfully.")
    except (AuthenticationError, APIError, httpx.RequestError, OpenWebUIError) as e:
        click.secho(f"An error occurred during folder creation: {e}", fg="red", err=True)
        if isinstance(e, httpx.HTTPStatusError):
            click.secho(f"Response: {e.text}", fg="red", err=True)
        log.error("CLI: Folder creation command failed.")
        raise click.Abort()


@folder.command("list")
@click.pass_context
def list_all_folders(ctx):
    """Lists all available folders."""
    log.info("CLI: Attempting to list all folders.")
    try:
        sdk = OpenWebUI()
        folders = asyncio.run(sdk.folders.list())

        if ctx.obj["OUTPUT_FORMAT"] == "json":
            format_output(folders, ctx.obj["OUTPUT_FORMAT"])
        else:
            if not folders:
                click.echo("No folders found on the server.")
                log.info("CLI: No folders found.")
                return

            click.secho("Available Folders:", bold=True)
            for folder_item in folders:
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
def list_chats_in_folder(ctx, folder_id: str):
    """Lists all chat IDs and titles within a specific folder."""
    log.info(f"CLI: Attempting to list chats in folder ID: {folder_id}")
    try:
        sdk = OpenWebUI()
        chats_in_folder = asyncio.run(sdk.chats.list_by_folder(folder_id=folder_id))

        if ctx.obj["OUTPUT_FORMAT"] == "json":
            format_output(chats_in_folder, ctx.obj["OUTPUT_FORMAT"])
        else:
            if not chats_in_folder:
                click.echo(f"No chats found in folder '{folder_id}'.")
                log.info(f"CLI: No chats found in folder '{folder_id}'.")
                return

            click.secho(f"Chats in folder '{folder_id}':", bold=True)
            for chat_item in chats_in_folder:
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
def delete_folder(ctx, folder_id: str):
    """Deletes a folder by its ID."""
    if ctx.obj["OUTPUT_FORMAT"] == "text" and not click.confirm(
        f"Are you sure you want to delete folder '{folder_id}'?"
    ):
        click.echo("Aborted.")
        raise click.Abort()

    log.info(f"CLI: Attempting to delete folder ID: {folder_id}")
    try:
        sdk = OpenWebUI()
        success = asyncio.run(sdk.folders.delete(folder_id=folder_id))

        if ctx.obj["OUTPUT_FORMAT"] == "json":
            format_output({"id": folder_id, "deleted": success}, ctx.obj["OUTPUT_FORMAT"])
        else:
            if success:
                click.secho(f"✅ Folder '{folder_id}' deleted successfully.", fg="green")
            else:
                click.secho(f"❌ Failed to delete folder '{folder_id}'.", fg="red", err=True)

        if not success:  # Always abort if SDK reports non-success
            log.error("CLI: Folder deletion command failed (SDK reported not successful).")
            raise click.Abort()
        log.info("CLI: Folder deletion command completed successfully.")

    except (AuthenticationError, NotFoundError, APIError, httpx.RequestError, OpenWebUIError) as e:
        click.secho(f"An error occurred during folder deletion: {e}", fg="red", err=True)
        if isinstance(e, httpx.HTTPStatusError):
            click.secho(f"Response: {e.text}", fg="red", err=True)
        log.error("CLI: Folder deletion command failed.")
        raise click.Abort()


if __name__ == "__main__":
    cli()
