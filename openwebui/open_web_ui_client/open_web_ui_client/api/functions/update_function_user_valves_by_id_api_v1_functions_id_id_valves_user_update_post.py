from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.update_function_user_valves_by_id_api_v1_functions_id_id_valves_user_update_post_form_data import (
    UpdateFunctionUserValvesByIdApiV1FunctionsIdIdValvesUserUpdatePostFormData,
)
from ...models.update_function_user_valves_by_id_api_v1_functions_id_id_valves_user_update_post_response_200_type_0 import (
    UpdateFunctionUserValvesByIdApiV1FunctionsIdIdValvesUserUpdatePostResponse200Type0,
)
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: UpdateFunctionUserValvesByIdApiV1FunctionsIdIdValvesUserUpdatePostFormData,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/functions/id/{id}/valves/user/update",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        HTTPValidationError,
        Union["UpdateFunctionUserValvesByIdApiV1FunctionsIdIdValvesUserUpdatePostResponse200Type0", None],
    ]
]:
    if response.status_code == 200:

        def _parse_response_200(
            data: object,
        ) -> Union["UpdateFunctionUserValvesByIdApiV1FunctionsIdIdValvesUserUpdatePostResponse200Type0", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = (
                    UpdateFunctionUserValvesByIdApiV1FunctionsIdIdValvesUserUpdatePostResponse200Type0.from_dict(data)
                )

                return response_200_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union["UpdateFunctionUserValvesByIdApiV1FunctionsIdIdValvesUserUpdatePostResponse200Type0", None], data
            )

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
    Union[
        HTTPValidationError,
        Union["UpdateFunctionUserValvesByIdApiV1FunctionsIdIdValvesUserUpdatePostResponse200Type0", None],
    ]
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
    body: UpdateFunctionUserValvesByIdApiV1FunctionsIdIdValvesUserUpdatePostFormData,
) -> Response[
    Union[
        HTTPValidationError,
        Union["UpdateFunctionUserValvesByIdApiV1FunctionsIdIdValvesUserUpdatePostResponse200Type0", None],
    ]
]:
    """Update Function User Valves By Id

    Args:
        id (str):
        body (UpdateFunctionUserValvesByIdApiV1FunctionsIdIdValvesUserUpdatePostFormData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, Union['UpdateFunctionUserValvesByIdApiV1FunctionsIdIdValvesUserUpdatePostResponse200Type0', None]]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateFunctionUserValvesByIdApiV1FunctionsIdIdValvesUserUpdatePostFormData,
) -> Optional[
    Union[
        HTTPValidationError,
        Union["UpdateFunctionUserValvesByIdApiV1FunctionsIdIdValvesUserUpdatePostResponse200Type0", None],
    ]
]:
    """Update Function User Valves By Id

    Args:
        id (str):
        body (UpdateFunctionUserValvesByIdApiV1FunctionsIdIdValvesUserUpdatePostFormData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, Union['UpdateFunctionUserValvesByIdApiV1FunctionsIdIdValvesUserUpdatePostResponse200Type0', None]]
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateFunctionUserValvesByIdApiV1FunctionsIdIdValvesUserUpdatePostFormData,
) -> Response[
    Union[
        HTTPValidationError,
        Union["UpdateFunctionUserValvesByIdApiV1FunctionsIdIdValvesUserUpdatePostResponse200Type0", None],
    ]
]:
    """Update Function User Valves By Id

    Args:
        id (str):
        body (UpdateFunctionUserValvesByIdApiV1FunctionsIdIdValvesUserUpdatePostFormData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, Union['UpdateFunctionUserValvesByIdApiV1FunctionsIdIdValvesUserUpdatePostResponse200Type0', None]]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateFunctionUserValvesByIdApiV1FunctionsIdIdValvesUserUpdatePostFormData,
) -> Optional[
    Union[
        HTTPValidationError,
        Union["UpdateFunctionUserValvesByIdApiV1FunctionsIdIdValvesUserUpdatePostResponse200Type0", None],
    ]
]:
    """Update Function User Valves By Id

    Args:
        id (str):
        body (UpdateFunctionUserValvesByIdApiV1FunctionsIdIdValvesUserUpdatePostFormData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, Union['UpdateFunctionUserValvesByIdApiV1FunctionsIdIdValvesUserUpdatePostResponse200Type0', None]]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
