from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.export_config_api_v1_configs_export_get_response_export_config_api_v1_configs_export_get import (
    ExportConfigApiV1ConfigsExportGetResponseExportConfigApiV1ConfigsExportGet,
)
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/configs/export",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ExportConfigApiV1ConfigsExportGetResponseExportConfigApiV1ConfigsExportGet]:
    if response.status_code == 200:
        response_200 = ExportConfigApiV1ConfigsExportGetResponseExportConfigApiV1ConfigsExportGet.from_dict(
            response.json()
        )

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ExportConfigApiV1ConfigsExportGetResponseExportConfigApiV1ConfigsExportGet]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[ExportConfigApiV1ConfigsExportGetResponseExportConfigApiV1ConfigsExportGet]:
    """Export Config

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExportConfigApiV1ConfigsExportGetResponseExportConfigApiV1ConfigsExportGet]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Optional[ExportConfigApiV1ConfigsExportGetResponseExportConfigApiV1ConfigsExportGet]:
    """Export Config

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExportConfigApiV1ConfigsExportGetResponseExportConfigApiV1ConfigsExportGet
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[ExportConfigApiV1ConfigsExportGetResponseExportConfigApiV1ConfigsExportGet]:
    """Export Config

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExportConfigApiV1ConfigsExportGetResponseExportConfigApiV1ConfigsExportGet]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Optional[ExportConfigApiV1ConfigsExportGetResponseExportConfigApiV1ConfigsExportGet]:
    """Export Config

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExportConfigApiV1ConfigsExportGetResponseExportConfigApiV1ConfigsExportGet
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
