from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.group_list_response import GroupListResponse
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/groups".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union["ErrorResponse", "GroupListResponse"]]:
    if response.status_code == HTTPStatus.OK:

        def _parse_response_200(data: object) -> Union["ErrorResponse", "GroupListResponse"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = GroupListResponse.from_dict(data)

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
) -> Response[Union["ErrorResponse", "GroupListResponse"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Union["ErrorResponse", "GroupListResponse"]]:
    """Groups

     Get a list of possible groups of symbols.
    A group is a set of symbols that share a common access level. Any user can have access to any number
    of such groups.
    It is required only if you use groups of symbols in order to restrict access to the instrument's
    data.

    **IMPORTANT:**
    Please plan your symbol grouping carefully. Groups cannot be deleted, you can only remove all the
    symbols from there.

    **LIMITATIONS:**
    Each integration is limited to have up to 10 symbol groups.
    Each symbol group is limited to have up to 10K symbols in it.
    You cannot put the same symbol into 2 different groups.

    This endpoint allows you to specify a list of groups, and the
    [/permissions](#operation/getPermissions) endpoint specifies
    which groups are available for the certain user.

    When TradingView user logs into his broker account - he will gain access to one or more groups,
    depending on the [/permissions](#operation/getPermissions) endpoint.

    At the [/symbol_info](#operation/getSymbolInfo) endpoint TradingView adds the GET argument `group`
    with the name of the group. Thus, TradingView will receive information about which group each symbol
    belongs to.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['ErrorResponse', 'GroupListResponse']]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Optional[Union["ErrorResponse", "GroupListResponse"]]:
    """Groups

     Get a list of possible groups of symbols.
    A group is a set of symbols that share a common access level. Any user can have access to any number
    of such groups.
    It is required only if you use groups of symbols in order to restrict access to the instrument's
    data.

    **IMPORTANT:**
    Please plan your symbol grouping carefully. Groups cannot be deleted, you can only remove all the
    symbols from there.

    **LIMITATIONS:**
    Each integration is limited to have up to 10 symbol groups.
    Each symbol group is limited to have up to 10K symbols in it.
    You cannot put the same symbol into 2 different groups.

    This endpoint allows you to specify a list of groups, and the
    [/permissions](#operation/getPermissions) endpoint specifies
    which groups are available for the certain user.

    When TradingView user logs into his broker account - he will gain access to one or more groups,
    depending on the [/permissions](#operation/getPermissions) endpoint.

    At the [/symbol_info](#operation/getSymbolInfo) endpoint TradingView adds the GET argument `group`
    with the name of the group. Thus, TradingView will receive information about which group each symbol
    belongs to.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['ErrorResponse', 'GroupListResponse']
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Union["ErrorResponse", "GroupListResponse"]]:
    """Groups

     Get a list of possible groups of symbols.
    A group is a set of symbols that share a common access level. Any user can have access to any number
    of such groups.
    It is required only if you use groups of symbols in order to restrict access to the instrument's
    data.

    **IMPORTANT:**
    Please plan your symbol grouping carefully. Groups cannot be deleted, you can only remove all the
    symbols from there.

    **LIMITATIONS:**
    Each integration is limited to have up to 10 symbol groups.
    Each symbol group is limited to have up to 10K symbols in it.
    You cannot put the same symbol into 2 different groups.

    This endpoint allows you to specify a list of groups, and the
    [/permissions](#operation/getPermissions) endpoint specifies
    which groups are available for the certain user.

    When TradingView user logs into his broker account - he will gain access to one or more groups,
    depending on the [/permissions](#operation/getPermissions) endpoint.

    At the [/symbol_info](#operation/getSymbolInfo) endpoint TradingView adds the GET argument `group`
    with the name of the group. Thus, TradingView will receive information about which group each symbol
    belongs to.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['ErrorResponse', 'GroupListResponse']]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Optional[Union["ErrorResponse", "GroupListResponse"]]:
    """Groups

     Get a list of possible groups of symbols.
    A group is a set of symbols that share a common access level. Any user can have access to any number
    of such groups.
    It is required only if you use groups of symbols in order to restrict access to the instrument's
    data.

    **IMPORTANT:**
    Please plan your symbol grouping carefully. Groups cannot be deleted, you can only remove all the
    symbols from there.

    **LIMITATIONS:**
    Each integration is limited to have up to 10 symbol groups.
    Each symbol group is limited to have up to 10K symbols in it.
    You cannot put the same symbol into 2 different groups.

    This endpoint allows you to specify a list of groups, and the
    [/permissions](#operation/getPermissions) endpoint specifies
    which groups are available for the certain user.

    When TradingView user logs into his broker account - he will gain access to one or more groups,
    depending on the [/permissions](#operation/getPermissions) endpoint.

    At the [/symbol_info](#operation/getSymbolInfo) endpoint TradingView adds the GET argument `group`
    with the name of the group. Thus, TradingView will receive information about which group each symbol
    belongs to.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['ErrorResponse', 'GroupListResponse']
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
