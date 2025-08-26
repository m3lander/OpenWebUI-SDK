from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.embeddings_api_v1_embeddings_post_form_data import EmbeddingsApiV1EmbeddingsPostFormData
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    *,
    body: EmbeddingsApiV1EmbeddingsPostFormData,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/embeddings",
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
    body: EmbeddingsApiV1EmbeddingsPostFormData,
) -> Response[Union[Any, HTTPValidationError]]:
    r"""Embeddings

     OpenAI-compatible embeddings endpoint.

    This handler:
      - Performs user/model checks and dispatches to the correct backend.
      - Supports OpenAI, Ollama, arena models, pipelines, and any compatible provider.

    Args:
        request (Request): Request context.
        form_data (dict): OpenAI-like payload (e.g., {\"model\": \"...\", \"input\": [...]})
        user (UserModel): Authenticated user.

    Returns:
        dict: OpenAI-compatible embeddings response.

    Args:
        body (EmbeddingsApiV1EmbeddingsPostFormData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: EmbeddingsApiV1EmbeddingsPostFormData,
) -> Optional[Union[Any, HTTPValidationError]]:
    r"""Embeddings

     OpenAI-compatible embeddings endpoint.

    This handler:
      - Performs user/model checks and dispatches to the correct backend.
      - Supports OpenAI, Ollama, arena models, pipelines, and any compatible provider.

    Args:
        request (Request): Request context.
        form_data (dict): OpenAI-like payload (e.g., {\"model\": \"...\", \"input\": [...]})
        user (UserModel): Authenticated user.

    Returns:
        dict: OpenAI-compatible embeddings response.

    Args:
        body (EmbeddingsApiV1EmbeddingsPostFormData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: EmbeddingsApiV1EmbeddingsPostFormData,
) -> Response[Union[Any, HTTPValidationError]]:
    r"""Embeddings

     OpenAI-compatible embeddings endpoint.

    This handler:
      - Performs user/model checks and dispatches to the correct backend.
      - Supports OpenAI, Ollama, arena models, pipelines, and any compatible provider.

    Args:
        request (Request): Request context.
        form_data (dict): OpenAI-like payload (e.g., {\"model\": \"...\", \"input\": [...]})
        user (UserModel): Authenticated user.

    Returns:
        dict: OpenAI-compatible embeddings response.

    Args:
        body (EmbeddingsApiV1EmbeddingsPostFormData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: EmbeddingsApiV1EmbeddingsPostFormData,
) -> Optional[Union[Any, HTTPValidationError]]:
    r"""Embeddings

     OpenAI-compatible embeddings endpoint.

    This handler:
      - Performs user/model checks and dispatches to the correct backend.
      - Supports OpenAI, Ollama, arena models, pipelines, and any compatible provider.

    Args:
        request (Request): Request context.
        form_data (dict): OpenAI-like payload (e.g., {\"model\": \"...\", \"input\": [...]})
        user (UserModel): Authenticated user.

    Returns:
        dict: OpenAI-compatible embeddings response.

    Args:
        body (EmbeddingsApiV1EmbeddingsPostFormData):

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
        )
    ).parsed
