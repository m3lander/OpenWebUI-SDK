from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_upload_file_api_v1_files_post import BodyUploadFileApiV1FilesPost
from ...models.file_model_response import FileModelResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: BodyUploadFileApiV1FilesPost,
    process: Union[Unset, bool] = True,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["process"] = process

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/files/",
        "params": params,
    }

    _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[FileModelResponse, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = FileModelResponse.from_dict(response.json())

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
) -> Response[Union[FileModelResponse, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: BodyUploadFileApiV1FilesPost,
    process: Union[Unset, bool] = True,
) -> Response[Union[FileModelResponse, HTTPValidationError]]:
    """Upload File

    Args:
        process (Union[Unset, bool]):  Default: True.
        body (BodyUploadFileApiV1FilesPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[FileModelResponse, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        body=body,
        process=process,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: BodyUploadFileApiV1FilesPost,
    process: Union[Unset, bool] = True,
) -> Optional[Union[FileModelResponse, HTTPValidationError]]:
    """Upload File

    Args:
        process (Union[Unset, bool]):  Default: True.
        body (BodyUploadFileApiV1FilesPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[FileModelResponse, HTTPValidationError]
    """

    return sync_detailed(
        client=client,
        body=body,
        process=process,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BodyUploadFileApiV1FilesPost,
    process: Union[Unset, bool] = True,
) -> Response[Union[FileModelResponse, HTTPValidationError]]:
    """Upload File

    Args:
        process (Union[Unset, bool]):  Default: True.
        body (BodyUploadFileApiV1FilesPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[FileModelResponse, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        body=body,
        process=process,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: BodyUploadFileApiV1FilesPost,
    process: Union[Unset, bool] = True,
) -> Optional[Union[FileModelResponse, HTTPValidationError]]:
    """Upload File

    Args:
        process (Union[Unset, bool]):  Default: True.
        body (BodyUploadFileApiV1FilesPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[FileModelResponse, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            process=process,
        )
    ).parsed
