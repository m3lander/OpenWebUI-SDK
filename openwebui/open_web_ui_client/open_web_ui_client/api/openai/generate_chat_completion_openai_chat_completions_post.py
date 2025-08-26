from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.generate_chat_completion_openai_chat_completions_post_form_data import (
    GenerateChatCompletionOpenaiChatCompletionsPostFormData,
)
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: GenerateChatCompletionOpenaiChatCompletionsPostFormData,
    bypass_filter: Union[None, Unset, bool] = False,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_bypass_filter: Union[None, Unset, bool]
    if isinstance(bypass_filter, Unset):
        json_bypass_filter = UNSET
    else:
        json_bypass_filter = bypass_filter
    params["bypass_filter"] = json_bypass_filter

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/openai/chat/completions",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = response.json()
        return response_200
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: GenerateChatCompletionOpenaiChatCompletionsPostFormData,
    bypass_filter: Union[None, Unset, bool] = False,
) -> Response[Union[Any, HTTPValidationError]]:
    """Generate Chat Completion

    Args:
        bypass_filter (Union[None, Unset, bool]):  Default: False.
        body (GenerateChatCompletionOpenaiChatCompletionsPostFormData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        body=body,
        bypass_filter=bypass_filter,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: GenerateChatCompletionOpenaiChatCompletionsPostFormData,
    bypass_filter: Union[None, Unset, bool] = False,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Generate Chat Completion

    Args:
        bypass_filter (Union[None, Unset, bool]):  Default: False.
        body (GenerateChatCompletionOpenaiChatCompletionsPostFormData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return sync_detailed(
        client=client,
        body=body,
        bypass_filter=bypass_filter,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: GenerateChatCompletionOpenaiChatCompletionsPostFormData,
    bypass_filter: Union[None, Unset, bool] = False,
) -> Response[Union[Any, HTTPValidationError]]:
    """Generate Chat Completion

    Args:
        bypass_filter (Union[None, Unset, bool]):  Default: False.
        body (GenerateChatCompletionOpenaiChatCompletionsPostFormData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        body=body,
        bypass_filter=bypass_filter,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: GenerateChatCompletionOpenaiChatCompletionsPostFormData,
    bypass_filter: Union[None, Unset, bool] = False,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Generate Chat Completion

    Args:
        bypass_filter (Union[None, Unset, bool]):  Default: False.
        body (GenerateChatCompletionOpenaiChatCompletionsPostFormData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            bypass_filter=bypass_filter,
        )
    ).parsed
