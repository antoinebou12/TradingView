from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.locale import Locale
from ...models.place_order_data import PlaceOrderData
from ...models.post_order_response import PostOrderResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: str,
    *,
    client: AuthenticatedClient,
    form_data: PlaceOrderData,
    locale: Locale,
    request_id: Union[Unset, None, str] = UNSET,
    confirm_id: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/accounts/{accountId}/orders".format(client.base_url, accountId=account_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_locale = locale.value

    params["locale"] = json_locale

    params["requestId"] = request_id

    params["confirmId"] = confirm_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "post",
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
) -> Optional[Union["ErrorResponse", "PostOrderResponse"]]:
    if response.status_code == HTTPStatus.OK:

        def _parse_response_200(data: object) -> Union["ErrorResponse", "PostOrderResponse"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = PostOrderResponse.from_dict(data)

                return response_200_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = ErrorResponse.from_dict(data)

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union["ErrorResponse", "PostOrderResponse"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient,
    form_data: PlaceOrderData,
    locale: Locale,
    request_id: Union[Unset, None, str] = UNSET,
    confirm_id: Union[Unset, None, str] = UNSET,
) -> Response[Union["ErrorResponse", "PostOrderResponse"]]:
    """Place Order

     Place a new order. Custom `Order dialog` fields defined in the [/accounts](#operation/getAccounts)
    are sent along with the standard fields in the order object.

    Args:
        account_id (str):
        locale (Locale): Locale (language) id. This parameter is required for trading integration
            only.
        request_id (Union[Unset, None, str]):
        confirm_id (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['ErrorResponse', 'PostOrderResponse']]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        client=client,
        form_data=form_data,
        locale=locale,
        request_id=request_id,
        confirm_id=confirm_id,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: str,
    *,
    client: AuthenticatedClient,
    form_data: PlaceOrderData,
    locale: Locale,
    request_id: Union[Unset, None, str] = UNSET,
    confirm_id: Union[Unset, None, str] = UNSET,
) -> Optional[Union["ErrorResponse", "PostOrderResponse"]]:
    """Place Order

     Place a new order. Custom `Order dialog` fields defined in the [/accounts](#operation/getAccounts)
    are sent along with the standard fields in the order object.

    Args:
        account_id (str):
        locale (Locale): Locale (language) id. This parameter is required for trading integration
            only.
        request_id (Union[Unset, None, str]):
        confirm_id (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['ErrorResponse', 'PostOrderResponse']
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
        form_data=form_data,
        locale=locale,
        request_id=request_id,
        confirm_id=confirm_id,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient,
    form_data: PlaceOrderData,
    locale: Locale,
    request_id: Union[Unset, None, str] = UNSET,
    confirm_id: Union[Unset, None, str] = UNSET,
) -> Response[Union["ErrorResponse", "PostOrderResponse"]]:
    """Place Order

     Place a new order. Custom `Order dialog` fields defined in the [/accounts](#operation/getAccounts)
    are sent along with the standard fields in the order object.

    Args:
        account_id (str):
        locale (Locale): Locale (language) id. This parameter is required for trading integration
            only.
        request_id (Union[Unset, None, str]):
        confirm_id (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['ErrorResponse', 'PostOrderResponse']]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        client=client,
        form_data=form_data,
        locale=locale,
        request_id=request_id,
        confirm_id=confirm_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    *,
    client: AuthenticatedClient,
    form_data: PlaceOrderData,
    locale: Locale,
    request_id: Union[Unset, None, str] = UNSET,
    confirm_id: Union[Unset, None, str] = UNSET,
) -> Optional[Union["ErrorResponse", "PostOrderResponse"]]:
    """Place Order

     Place a new order. Custom `Order dialog` fields defined in the [/accounts](#operation/getAccounts)
    are sent along with the standard fields in the order object.

    Args:
        account_id (str):
        locale (Locale): Locale (language) id. This parameter is required for trading integration
            only.
        request_id (Union[Unset, None, str]):
        confirm_id (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['ErrorResponse', 'PostOrderResponse']
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            form_data=form_data,
            locale=locale,
            request_id=request_id,
            confirm_id=confirm_id,
        )
    ).parsed
