from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_tools_user_valves_by_id_api_v1_tools_id_id_valves_user_get_response_200_type_0 import (
    GetToolsUserValvesByIdApiV1ToolsIdIdValvesUserGetResponse200Type0,
)
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/tools/id/{id}/valves/user",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[HTTPValidationError, Union["GetToolsUserValvesByIdApiV1ToolsIdIdValvesUserGetResponse200Type0", None]]
]:
    if response.status_code == 200:

        def _parse_response_200(
            data: object,
        ) -> Union["GetToolsUserValvesByIdApiV1ToolsIdIdValvesUserGetResponse200Type0", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = GetToolsUserValvesByIdApiV1ToolsIdIdValvesUserGetResponse200Type0.from_dict(data)

                return response_200_type_0
            except:  # noqa: E722
                pass
            return cast(Union["GetToolsUserValvesByIdApiV1ToolsIdIdValvesUserGetResponse200Type0", None], data)

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
) -> Response[
    Union[HTTPValidationError, Union["GetToolsUserValvesByIdApiV1ToolsIdIdValvesUserGetResponse200Type0", None]]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    Union[HTTPValidationError, Union["GetToolsUserValvesByIdApiV1ToolsIdIdValvesUserGetResponse200Type0", None]]
]:
    """Get Tools User Valves By Id

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, Union['GetToolsUserValvesByIdApiV1ToolsIdIdValvesUserGetResponse200Type0', None]]]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[
    Union[HTTPValidationError, Union["GetToolsUserValvesByIdApiV1ToolsIdIdValvesUserGetResponse200Type0", None]]
]:
    """Get Tools User Valves By Id

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, Union['GetToolsUserValvesByIdApiV1ToolsIdIdValvesUserGetResponse200Type0', None]]
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    Union[HTTPValidationError, Union["GetToolsUserValvesByIdApiV1ToolsIdIdValvesUserGetResponse200Type0", None]]
]:
    """Get Tools User Valves By Id

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, Union['GetToolsUserValvesByIdApiV1ToolsIdIdValvesUserGetResponse200Type0', None]]]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[
    Union[HTTPValidationError, Union["GetToolsUserValvesByIdApiV1ToolsIdIdValvesUserGetResponse200Type0", None]]
]:
    """Get Tools User Valves By Id

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, Union['GetToolsUserValvesByIdApiV1ToolsIdIdValvesUserGetResponse200Type0', None]]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
