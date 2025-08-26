from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.user_list_response import UserListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    query: Union[None, Unset, str] = UNSET,
    order_by: Union[None, Unset, str] = UNSET,
    direction: Union[None, Unset, str] = UNSET,
    page: Union[None, Unset, int] = 1,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_query: Union[None, Unset, str]
    if isinstance(query, Unset):
        json_query = UNSET
    else:
        json_query = query
    params["query"] = json_query

    json_order_by: Union[None, Unset, str]
    if isinstance(order_by, Unset):
        json_order_by = UNSET
    else:
        json_order_by = order_by
    params["order_by"] = json_order_by

    json_direction: Union[None, Unset, str]
    if isinstance(direction, Unset):
        json_direction = UNSET
    else:
        json_direction = direction
    params["direction"] = json_direction

    json_page: Union[None, Unset, int]
    if isinstance(page, Unset):
        json_page = UNSET
    else:
        json_page = page
    params["page"] = json_page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/users/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, UserListResponse]]:
    if response.status_code == 200:
        response_200 = UserListResponse.from_dict(response.json())

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
) -> Response[Union[HTTPValidationError, UserListResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    query: Union[None, Unset, str] = UNSET,
    order_by: Union[None, Unset, str] = UNSET,
    direction: Union[None, Unset, str] = UNSET,
    page: Union[None, Unset, int] = 1,
) -> Response[Union[HTTPValidationError, UserListResponse]]:
    """Get Users

    Args:
        query (Union[None, Unset, str]):
        order_by (Union[None, Unset, str]):
        direction (Union[None, Unset, str]):
        page (Union[None, Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, UserListResponse]]
    """

    kwargs = _get_kwargs(
        query=query,
        order_by=order_by,
        direction=direction,
        page=page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    query: Union[None, Unset, str] = UNSET,
    order_by: Union[None, Unset, str] = UNSET,
    direction: Union[None, Unset, str] = UNSET,
    page: Union[None, Unset, int] = 1,
) -> Optional[Union[HTTPValidationError, UserListResponse]]:
    """Get Users

    Args:
        query (Union[None, Unset, str]):
        order_by (Union[None, Unset, str]):
        direction (Union[None, Unset, str]):
        page (Union[None, Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, UserListResponse]
    """

    return sync_detailed(
        client=client,
        query=query,
        order_by=order_by,
        direction=direction,
        page=page,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    query: Union[None, Unset, str] = UNSET,
    order_by: Union[None, Unset, str] = UNSET,
    direction: Union[None, Unset, str] = UNSET,
    page: Union[None, Unset, int] = 1,
) -> Response[Union[HTTPValidationError, UserListResponse]]:
    """Get Users

    Args:
        query (Union[None, Unset, str]):
        order_by (Union[None, Unset, str]):
        direction (Union[None, Unset, str]):
        page (Union[None, Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, UserListResponse]]
    """

    kwargs = _get_kwargs(
        query=query,
        order_by=order_by,
        direction=direction,
        page=page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    query: Union[None, Unset, str] = UNSET,
    order_by: Union[None, Unset, str] = UNSET,
    direction: Union[None, Unset, str] = UNSET,
    page: Union[None, Unset, int] = 1,
) -> Optional[Union[HTTPValidationError, UserListResponse]]:
    """Get Users

    Args:
        query (Union[None, Unset, str]):
        order_by (Union[None, Unset, str]):
        direction (Union[None, Unset, str]):
        page (Union[None, Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, UserListResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            query=query,
            order_by=order_by,
            direction=direction,
            page=page,
        )
    ).parsed
