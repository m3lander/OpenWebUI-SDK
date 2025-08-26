from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.chat_title_id_response import ChatTitleIdResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: Union[None, Unset, int] = UNSET,
    query: Union[None, Unset, str] = UNSET,
    order_by: Union[None, Unset, str] = UNSET,
    direction: Union[None, Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_page: Union[None, Unset, int]
    if isinstance(page, Unset):
        json_page = UNSET
    else:
        json_page = page
    params["page"] = json_page

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

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/chats/archived",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, list["ChatTitleIdResponse"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ChatTitleIdResponse.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[Union[HTTPValidationError, list["ChatTitleIdResponse"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    page: Union[None, Unset, int] = UNSET,
    query: Union[None, Unset, str] = UNSET,
    order_by: Union[None, Unset, str] = UNSET,
    direction: Union[None, Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, list["ChatTitleIdResponse"]]]:
    """Get Archived Session User Chat List

    Args:
        page (Union[None, Unset, int]):
        query (Union[None, Unset, str]):
        order_by (Union[None, Unset, str]):
        direction (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, list['ChatTitleIdResponse']]]
    """

    kwargs = _get_kwargs(
        page=page,
        query=query,
        order_by=order_by,
        direction=direction,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    page: Union[None, Unset, int] = UNSET,
    query: Union[None, Unset, str] = UNSET,
    order_by: Union[None, Unset, str] = UNSET,
    direction: Union[None, Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, list["ChatTitleIdResponse"]]]:
    """Get Archived Session User Chat List

    Args:
        page (Union[None, Unset, int]):
        query (Union[None, Unset, str]):
        order_by (Union[None, Unset, str]):
        direction (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, list['ChatTitleIdResponse']]
    """

    return sync_detailed(
        client=client,
        page=page,
        query=query,
        order_by=order_by,
        direction=direction,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    page: Union[None, Unset, int] = UNSET,
    query: Union[None, Unset, str] = UNSET,
    order_by: Union[None, Unset, str] = UNSET,
    direction: Union[None, Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, list["ChatTitleIdResponse"]]]:
    """Get Archived Session User Chat List

    Args:
        page (Union[None, Unset, int]):
        query (Union[None, Unset, str]):
        order_by (Union[None, Unset, str]):
        direction (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, list['ChatTitleIdResponse']]]
    """

    kwargs = _get_kwargs(
        page=page,
        query=query,
        order_by=order_by,
        direction=direction,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    page: Union[None, Unset, int] = UNSET,
    query: Union[None, Unset, str] = UNSET,
    order_by: Union[None, Unset, str] = UNSET,
    direction: Union[None, Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, list["ChatTitleIdResponse"]]]:
    """Get Archived Session User Chat List

    Args:
        page (Union[None, Unset, int]):
        query (Union[None, Unset, str]):
        order_by (Union[None, Unset, str]):
        direction (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, list['ChatTitleIdResponse']]
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            query=query,
            order_by=order_by,
            direction=direction,
        )
    ).parsed
