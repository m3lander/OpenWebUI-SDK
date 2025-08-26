from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.update_pipeline_valves_api_v1_pipelines_pipeline_id_valves_update_post_form_data import (
    UpdatePipelineValvesApiV1PipelinesPipelineIdValvesUpdatePostFormData,
)
from ...types import UNSET, Response


def _get_kwargs(
    pipeline_id: str,
    *,
    body: UpdatePipelineValvesApiV1PipelinesPipelineIdValvesUpdatePostFormData,
    url_idx: Union[None, int],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_url_idx: Union[None, int]
    json_url_idx = url_idx
    params["urlIdx"] = json_url_idx

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/pipelines/{pipeline_id}/valves/update",
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
    pipeline_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdatePipelineValvesApiV1PipelinesPipelineIdValvesUpdatePostFormData,
    url_idx: Union[None, int],
) -> Response[Union[Any, HTTPValidationError]]:
    """Update Pipeline Valves

    Args:
        pipeline_id (str):
        url_idx (Union[None, int]):
        body (UpdatePipelineValvesApiV1PipelinesPipelineIdValvesUpdatePostFormData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        pipeline_id=pipeline_id,
        body=body,
        url_idx=url_idx,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    pipeline_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdatePipelineValvesApiV1PipelinesPipelineIdValvesUpdatePostFormData,
    url_idx: Union[None, int],
) -> Optional[Union[Any, HTTPValidationError]]:
    """Update Pipeline Valves

    Args:
        pipeline_id (str):
        url_idx (Union[None, int]):
        body (UpdatePipelineValvesApiV1PipelinesPipelineIdValvesUpdatePostFormData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return sync_detailed(
        pipeline_id=pipeline_id,
        client=client,
        body=body,
        url_idx=url_idx,
    ).parsed


async def asyncio_detailed(
    pipeline_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdatePipelineValvesApiV1PipelinesPipelineIdValvesUpdatePostFormData,
    url_idx: Union[None, int],
) -> Response[Union[Any, HTTPValidationError]]:
    """Update Pipeline Valves

    Args:
        pipeline_id (str):
        url_idx (Union[None, int]):
        body (UpdatePipelineValvesApiV1PipelinesPipelineIdValvesUpdatePostFormData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        pipeline_id=pipeline_id,
        body=body,
        url_idx=url_idx,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pipeline_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdatePipelineValvesApiV1PipelinesPipelineIdValvesUpdatePostFormData,
    url_idx: Union[None, int],
) -> Optional[Union[Any, HTTPValidationError]]:
    """Update Pipeline Valves

    Args:
        pipeline_id (str):
        url_idx (Union[None, int]):
        body (UpdatePipelineValvesApiV1PipelinesPipelineIdValvesUpdatePostFormData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            pipeline_id=pipeline_id,
            client=client,
            body=body,
            url_idx=url_idx,
        )
    ).parsed
