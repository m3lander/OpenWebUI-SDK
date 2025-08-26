from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.load_tool_from_url_api_v1_tools_load_url_post_response_200_type_0 import (
    LoadToolFromUrlApiV1ToolsLoadUrlPostResponse200Type0,
)
from ...models.load_url_form import LoadUrlForm
from ...types import Response


def _get_kwargs(
    *,
    body: LoadUrlForm,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/tools/load/url",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, Union["LoadToolFromUrlApiV1ToolsLoadUrlPostResponse200Type0", None]]]:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> Union["LoadToolFromUrlApiV1ToolsLoadUrlPostResponse200Type0", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = LoadToolFromUrlApiV1ToolsLoadUrlPostResponse200Type0.from_dict(data)

                return response_200_type_0
            except:  # noqa: E722
                pass
            return cast(Union["LoadToolFromUrlApiV1ToolsLoadUrlPostResponse200Type0", None], data)

        response_200 = _parse_response_200(response.json())

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
) -> Response[Union[HTTPValidationError, Union["LoadToolFromUrlApiV1ToolsLoadUrlPostResponse200Type0", None]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: LoadUrlForm,
) -> Response[Union[HTTPValidationError, Union["LoadToolFromUrlApiV1ToolsLoadUrlPostResponse200Type0", None]]]:
    """Load Tool From Url

    Args:
        body (LoadUrlForm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, Union['LoadToolFromUrlApiV1ToolsLoadUrlPostResponse200Type0', None]]]
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
    body: LoadUrlForm,
) -> Optional[Union[HTTPValidationError, Union["LoadToolFromUrlApiV1ToolsLoadUrlPostResponse200Type0", None]]]:
    """Load Tool From Url

    Args:
        body (LoadUrlForm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, Union['LoadToolFromUrlApiV1ToolsLoadUrlPostResponse200Type0', None]]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: LoadUrlForm,
) -> Response[Union[HTTPValidationError, Union["LoadToolFromUrlApiV1ToolsLoadUrlPostResponse200Type0", None]]]:
    """Load Tool From Url

    Args:
        body (LoadUrlForm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, Union['LoadToolFromUrlApiV1ToolsLoadUrlPostResponse200Type0', None]]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: LoadUrlForm,
) -> Optional[Union[HTTPValidationError, Union["LoadToolFromUrlApiV1ToolsLoadUrlPostResponse200Type0", None]]]:
    """Load Tool From Url

    Args:
        body (LoadUrlForm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, Union['LoadToolFromUrlApiV1ToolsLoadUrlPostResponse200Type0', None]]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
