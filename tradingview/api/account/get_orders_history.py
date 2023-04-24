from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.locale import Locale
from ...models.orders_history_response import OrdersHistoryResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: str,
    *,
    client: AuthenticatedClient,
    locale: Locale,
    max_count: Union[Unset, None, float] = UNSET,
) -> Dict[str, Any]:
    url = "{}/accounts/{accountId}/ordersHistory".format(client.base_url, accountId=account_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_locale = locale.value

    params["locale"] = json_locale

    params["maxCount"] = max_count

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "params": params,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union["ErrorResponse", "OrdersHistoryResponse"]]:
    if response.status_code == HTTPStatus.OK:

        def _parse_response_200(data: object) -> Union["ErrorResponse", "OrdersHistoryResponse"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = OrdersHistoryResponse.from_dict(data)

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
) -> Response[Union["ErrorResponse", "OrdersHistoryResponse"]]:
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
    locale: Locale,
    max_count: Union[Unset, None, float] = UNSET,
) -> Response[Union["ErrorResponse", "OrdersHistoryResponse"]]:
    """Orders History

     Get order history for an account. It is expected that returned orders will have a final status
    (`rejected`,
    `filled`, `cancelled`). This endpoint is optional. If you don't support orders history, please set
    the `supportOrdersHistory` flag to `false`.

    Args:
        account_id (str):
        locale (Locale): Locale (language) id. This parameter is required for trading integration
            only.
        max_count (Union[Unset, None, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['ErrorResponse', 'OrdersHistoryResponse']]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        client=client,
        locale=locale,
        max_count=max_count,
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
    locale: Locale,
    max_count: Union[Unset, None, float] = UNSET,
) -> Optional[Union["ErrorResponse", "OrdersHistoryResponse"]]:
    """Orders History

     Get order history for an account. It is expected that returned orders will have a final status
    (`rejected`,
    `filled`, `cancelled`). This endpoint is optional. If you don't support orders history, please set
    the `supportOrdersHistory` flag to `false`.

    Args:
        account_id (str):
        locale (Locale): Locale (language) id. This parameter is required for trading integration
            only.
        max_count (Union[Unset, None, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['ErrorResponse', 'OrdersHistoryResponse']
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
        locale=locale,
        max_count=max_count,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient,
    locale: Locale,
    max_count: Union[Unset, None, float] = UNSET,
) -> Response[Union["ErrorResponse", "OrdersHistoryResponse"]]:
    """Orders History

     Get order history for an account. It is expected that returned orders will have a final status
    (`rejected`,
    `filled`, `cancelled`). This endpoint is optional. If you don't support orders history, please set
    the `supportOrdersHistory` flag to `false`.

    Args:
        account_id (str):
        locale (Locale): Locale (language) id. This parameter is required for trading integration
            only.
        max_count (Union[Unset, None, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['ErrorResponse', 'OrdersHistoryResponse']]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        client=client,
        locale=locale,
        max_count=max_count,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    *,
    client: AuthenticatedClient,
    locale: Locale,
    max_count: Union[Unset, None, float] = UNSET,
) -> Optional[Union["ErrorResponse", "OrdersHistoryResponse"]]:
    """Orders History

     Get order history for an account. It is expected that returned orders will have a final status
    (`rejected`,
    `filled`, `cancelled`). This endpoint is optional. If you don't support orders history, please set
    the `supportOrdersHistory` flag to `false`.

    Args:
        account_id (str):
        locale (Locale): Locale (language) id. This parameter is required for trading integration
            only.
        max_count (Union[Unset, None, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['ErrorResponse', 'OrdersHistoryResponse']
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            locale=locale,
            max_count=max_count,
        )
    ).parsed