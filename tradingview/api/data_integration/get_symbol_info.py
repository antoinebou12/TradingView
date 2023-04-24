from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.symbol_info_response import SymbolInfoResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    group: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/symbol_info".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["group"] = group

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
) -> Optional[Union["ErrorResponse", "SymbolInfoResponse"]]:
    if response.status_code == HTTPStatus.OK:

        def _parse_response_200(data: object) -> Union["ErrorResponse", "SymbolInfoResponse"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = SymbolInfoResponse.from_dict(data)

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
) -> Response[Union["ErrorResponse", "SymbolInfoResponse"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    group: Union[Unset, None, str] = UNSET,
) -> Response[Union["ErrorResponse", "SymbolInfoResponse"]]:
    """Symbol Info

     Get a list of all instruments.

    Args:
        group (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['ErrorResponse', 'SymbolInfoResponse']]
    """

    kwargs = _get_kwargs(
        client=client,
        group=group,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    group: Union[Unset, None, str] = UNSET,
) -> Optional[Union["ErrorResponse", "SymbolInfoResponse"]]:
    """Symbol Info

     Get a list of all instruments.

    Args:
        group (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['ErrorResponse', 'SymbolInfoResponse']
    """

    return sync_detailed(
        client=client,
        group=group,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    group: Union[Unset, None, str] = UNSET,
) -> Response[Union["ErrorResponse", "SymbolInfoResponse"]]:
    """Symbol Info

     Get a list of all instruments.

    Args:
        group (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['ErrorResponse', 'SymbolInfoResponse']]
    """

    kwargs = _get_kwargs(
        client=client,
        group=group,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    group: Union[Unset, None, str] = UNSET,
) -> Optional[Union["ErrorResponse", "SymbolInfoResponse"]]:
    """Symbol Info

     Get a list of all instruments.

    Args:
        group (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['ErrorResponse', 'SymbolInfoResponse']
    """

    return (
        await asyncio_detailed(
            client=client,
            group=group,
        )
    ).parsed
