from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.locale import Locale
from ...models.place_modify_preview_order_common import PlaceModifyPreviewOrderCommon
from ...models.success_response import SuccessResponse
from ...models.success_response_with_transaction_id import SuccessResponseWithTransactionId
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: str,
    order_id: str,
    *,
    client: AuthenticatedClient,
    form_data: PlaceModifyPreviewOrderCommon,
    locale: Locale,
    confirm_id: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/accounts/{accountId}/orders/{orderId}".format(client.base_url, accountId=account_id, orderId=order_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_locale = locale.value

    params["locale"] = json_locale

    params["confirmId"] = confirm_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "data": form_data.to_dict(),
        "params": params,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union["ErrorResponse", "SuccessResponse", "SuccessResponseWithTransactionId"]]:
    if response.status_code == HTTPStatus.OK:

        def _parse_response_200(
            data: object,
        ) -> Union["ErrorResponse", "SuccessResponse", "SuccessResponseWithTransactionId"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = SuccessResponse.from_dict(data)

                return response_200_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_1 = SuccessResponseWithTransactionId.from_dict(data)

                return response_200_type_1
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_2 = ErrorResponse.from_dict(data)

            return response_200_type_2

        response_200 = _parse_response_200(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union["ErrorResponse", "SuccessResponse", "SuccessResponseWithTransactionId"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_id: str,
    order_id: str,
    *,
    client: AuthenticatedClient,
    form_data: PlaceModifyPreviewOrderCommon,
    locale: Locale,
    confirm_id: Union[Unset, None, str] = UNSET,
) -> Response[Union["ErrorResponse", "SuccessResponse", "SuccessResponseWithTransactionId"]]:
    """Modify Order

     Modify an existing order. Custom `Order dialog` fields defined in the
    [/accounts](#operation/getAccounts) are sent along with the standard fields in the order object.

    Args:
        account_id (str):
        order_id (str):
        locale (Locale): Locale (language) id. This parameter is required for trading integration
            only.
        confirm_id (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['ErrorResponse', 'SuccessResponse', 'SuccessResponseWithTransactionId']]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        order_id=order_id,
        client=client,
        form_data=form_data,
        locale=locale,
        confirm_id=confirm_id,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: str,
    order_id: str,
    *,
    client: AuthenticatedClient,
    form_data: PlaceModifyPreviewOrderCommon,
    locale: Locale,
    confirm_id: Union[Unset, None, str] = UNSET,
) -> Optional[Union["ErrorResponse", "SuccessResponse", "SuccessResponseWithTransactionId"]]:
    """Modify Order

     Modify an existing order. Custom `Order dialog` fields defined in the
    [/accounts](#operation/getAccounts) are sent along with the standard fields in the order object.

    Args:
        account_id (str):
        order_id (str):
        locale (Locale): Locale (language) id. This parameter is required for trading integration
            only.
        confirm_id (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['ErrorResponse', 'SuccessResponse', 'SuccessResponseWithTransactionId']
    """

    return sync_detailed(
        account_id=account_id,
        order_id=order_id,
        client=client,
        form_data=form_data,
        locale=locale,
        confirm_id=confirm_id,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    order_id: str,
    *,
    client: AuthenticatedClient,
    form_data: PlaceModifyPreviewOrderCommon,
    locale: Locale,
    confirm_id: Union[Unset, None, str] = UNSET,
) -> Response[Union["ErrorResponse", "SuccessResponse", "SuccessResponseWithTransactionId"]]:
    """Modify Order

     Modify an existing order. Custom `Order dialog` fields defined in the
    [/accounts](#operation/getAccounts) are sent along with the standard fields in the order object.

    Args:
        account_id (str):
        order_id (str):
        locale (Locale): Locale (language) id. This parameter is required for trading integration
            only.
        confirm_id (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['ErrorResponse', 'SuccessResponse', 'SuccessResponseWithTransactionId']]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        order_id=order_id,
        client=client,
        form_data=form_data,
        locale=locale,
        confirm_id=confirm_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    order_id: str,
    *,
    client: AuthenticatedClient,
    form_data: PlaceModifyPreviewOrderCommon,
    locale: Locale,
    confirm_id: Union[Unset, None, str] = UNSET,
) -> Optional[Union["ErrorResponse", "SuccessResponse", "SuccessResponseWithTransactionId"]]:
    """Modify Order

     Modify an existing order. Custom `Order dialog` fields defined in the
    [/accounts](#operation/getAccounts) are sent along with the standard fields in the order object.

    Args:
        account_id (str):
        order_id (str):
        locale (Locale): Locale (language) id. This parameter is required for trading integration
            only.
        confirm_id (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['ErrorResponse', 'SuccessResponse', 'SuccessResponseWithTransactionId']
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            order_id=order_id,
            client=client,
            form_data=form_data,
            locale=locale,
            confirm_id=confirm_id,
        )
    ).parsed
