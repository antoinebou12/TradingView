from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.depth_response import DepthResponse
from ...models.error_response import ErrorResponse
from ...models.locale import Locale
from ...types import UNSET, Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    locale: Locale,
    account_id: str,
    symbol: str,
) -> Dict[str, Any]:
    url = "{}/depth".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_locale = locale.value

    params["locale"] = json_locale

    params["accountId"] = account_id

    params["symbol"] = symbol

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union["DepthResponse", "ErrorResponse"]]:
    if response.status_code == HTTPStatus.OK:

        def _parse_response_200(data: object) -> Union["DepthResponse", "ErrorResponse"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = DepthResponse.from_dict(data)

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


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union["DepthResponse", "ErrorResponse"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    locale: Locale,
    account_id: str,
    symbol: str,
) -> Response[Union["DepthResponse", "ErrorResponse"]]:
    """Depth

     Get current depth of market for the instrument. Optional.

    Args:
        locale (Locale): Locale (language) id. This parameter is required for trading integration
            only.
        account_id (str):
        symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['DepthResponse', 'ErrorResponse']]
    """

    kwargs = _get_kwargs(
        client=client,
        locale=locale,
        account_id=account_id,
        symbol=symbol,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    locale: Locale,
    account_id: str,
    symbol: str,
) -> Optional[Union["DepthResponse", "ErrorResponse"]]:
    """Depth

     Get current depth of market for the instrument. Optional.

    Args:
        locale (Locale): Locale (language) id. This parameter is required for trading integration
            only.
        account_id (str):
        symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['DepthResponse', 'ErrorResponse']
    """

    return sync_detailed(
        client=client,
        locale=locale,
        account_id=account_id,
        symbol=symbol,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    locale: Locale,
    account_id: str,
    symbol: str,
) -> Response[Union["DepthResponse", "ErrorResponse"]]:
    """Depth

     Get current depth of market for the instrument. Optional.

    Args:
        locale (Locale): Locale (language) id. This parameter is required for trading integration
            only.
        account_id (str):
        symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['DepthResponse', 'ErrorResponse']]
    """

    kwargs = _get_kwargs(
        client=client,
        locale=locale,
        account_id=account_id,
        symbol=symbol,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    locale: Locale,
    account_id: str,
    symbol: str,
) -> Optional[Union["DepthResponse", "ErrorResponse"]]:
    """Depth

     Get current depth of market for the instrument. Optional.

    Args:
        locale (Locale): Locale (language) id. This parameter is required for trading integration
            only.
        account_id (str):
        symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['DepthResponse', 'ErrorResponse']
    """

    return (
        await asyncio_detailed(
            client=client,
            locale=locale,
            account_id=account_id,
            symbol=symbol,
        )
    ).parsed
