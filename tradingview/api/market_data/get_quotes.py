from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.locale import Locale
from ...models.quotes_response import QuotesResponse
from ...types import UNSET, Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    locale: Locale,
    account_id: str,
    symbols: str,
) -> Dict[str, Any]:
    url = "{}/quotes".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_locale = locale.value

    params["locale"] = json_locale

    params["accountId"] = account_id

    params["symbols"] = symbols

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union["ErrorResponse", "QuotesResponse"]]:
    if response.status_code == HTTPStatus.OK:

        def _parse_response_200(data: object) -> Union["ErrorResponse", "QuotesResponse"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = QuotesResponse.from_dict(data)

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


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union["ErrorResponse", "QuotesResponse"]]:
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
    symbols: str,
) -> Response[Union["ErrorResponse", "QuotesResponse"]]:
    """Quotes

     Get current prices of the instrument.
    The `bid` and `ask` fields are required, and the `buyPipValue` and `sellPipValue` fields
    are desirable if the account currency is different from the currency of the instrument.
    The same values should be sent for these fields if different values for buying and selling are not
    supported.

    Args:
        locale (Locale): Locale (language) id. This parameter is required for trading integration
            only.
        account_id (str):
        symbols (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['ErrorResponse', 'QuotesResponse']]
    """

    kwargs = _get_kwargs(
        client=client,
        locale=locale,
        account_id=account_id,
        symbols=symbols,
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
    symbols: str,
) -> Optional[Union["ErrorResponse", "QuotesResponse"]]:
    """Quotes

     Get current prices of the instrument.
    The `bid` and `ask` fields are required, and the `buyPipValue` and `sellPipValue` fields
    are desirable if the account currency is different from the currency of the instrument.
    The same values should be sent for these fields if different values for buying and selling are not
    supported.

    Args:
        locale (Locale): Locale (language) id. This parameter is required for trading integration
            only.
        account_id (str):
        symbols (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['ErrorResponse', 'QuotesResponse']
    """

    return sync_detailed(
        client=client,
        locale=locale,
        account_id=account_id,
        symbols=symbols,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    locale: Locale,
    account_id: str,
    symbols: str,
) -> Response[Union["ErrorResponse", "QuotesResponse"]]:
    """Quotes

     Get current prices of the instrument.
    The `bid` and `ask` fields are required, and the `buyPipValue` and `sellPipValue` fields
    are desirable if the account currency is different from the currency of the instrument.
    The same values should be sent for these fields if different values for buying and selling are not
    supported.

    Args:
        locale (Locale): Locale (language) id. This parameter is required for trading integration
            only.
        account_id (str):
        symbols (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['ErrorResponse', 'QuotesResponse']]
    """

    kwargs = _get_kwargs(
        client=client,
        locale=locale,
        account_id=account_id,
        symbols=symbols,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    locale: Locale,
    account_id: str,
    symbols: str,
) -> Optional[Union["ErrorResponse", "QuotesResponse"]]:
    """Quotes

     Get current prices of the instrument.
    The `bid` and `ask` fields are required, and the `buyPipValue` and `sellPipValue` fields
    are desirable if the account currency is different from the currency of the instrument.
    The same values should be sent for these fields if different values for buying and selling are not
    supported.

    Args:
        locale (Locale): Locale (language) id. This parameter is required for trading integration
            only.
        account_id (str):
        symbols (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['ErrorResponse', 'QuotesResponse']
    """

    return (
        await asyncio_detailed(
            client=client,
            locale=locale,
            account_id=account_id,
            symbols=symbols,
        )
    ).parsed
