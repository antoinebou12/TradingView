from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.instruments_response import InstrumentsResponse
from ...models.locale import Locale
from ...types import UNSET, Response


def _get_kwargs(
    account_id: str,
    *,
    client: AuthenticatedClient,
    locale: Locale,
) -> Dict[str, Any]:
    url = "{}/accounts/{accountId}/instruments".format(client.base_url, accountId=account_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_locale = locale.value

    params["locale"] = json_locale

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
) -> Optional[Union["ErrorResponse", "InstrumentsResponse"]]:
    if response.status_code == HTTPStatus.OK:

        def _parse_response_200(data: object) -> Union["ErrorResponse", "InstrumentsResponse"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = InstrumentsResponse.from_dict(data)

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
) -> Response[Union["ErrorResponse", "InstrumentsResponse"]]:
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
) -> Response[Union["ErrorResponse", "InstrumentsResponse"]]:
    """Instruments

     Get the list of the instruments that are available for trading with the specified account.

    Args:
        account_id (str):
        locale (Locale): Locale (language) id. This parameter is required for trading integration
            only.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['ErrorResponse', 'InstrumentsResponse']]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        client=client,
        locale=locale,
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
) -> Optional[Union["ErrorResponse", "InstrumentsResponse"]]:
    """Instruments

     Get the list of the instruments that are available for trading with the specified account.

    Args:
        account_id (str):
        locale (Locale): Locale (language) id. This parameter is required for trading integration
            only.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['ErrorResponse', 'InstrumentsResponse']
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
        locale=locale,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient,
    locale: Locale,
) -> Response[Union["ErrorResponse", "InstrumentsResponse"]]:
    """Instruments

     Get the list of the instruments that are available for trading with the specified account.

    Args:
        account_id (str):
        locale (Locale): Locale (language) id. This parameter is required for trading integration
            only.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['ErrorResponse', 'InstrumentsResponse']]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        client=client,
        locale=locale,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    *,
    client: AuthenticatedClient,
    locale: Locale,
) -> Optional[Union["ErrorResponse", "InstrumentsResponse"]]:
    """Instruments

     Get the list of the instruments that are available for trading with the specified account.

    Args:
        account_id (str):
        locale (Locale): Locale (language) id. This parameter is required for trading integration
            only.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['ErrorResponse', 'InstrumentsResponse']
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            locale=locale,
        )
    ).parsed
