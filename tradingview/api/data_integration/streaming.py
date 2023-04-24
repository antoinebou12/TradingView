from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.streaming_ask_responsedeprecated import StreamingAskResponsedeprecated
from ...models.streaming_bid_responsedeprecated import StreamingBidResponsedeprecated
from ...models.streaming_daily_bar_response import StreamingDailyBarResponse
from ...models.streaming_heartbeat_response import StreamingHeartbeatResponse
from ...models.streaming_quote_response import StreamingQuoteResponse
from ...models.streaming_trade_response import StreamingTradeResponse
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/streaming".format(client.base_url)

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
) -> Optional[
    Union[
        "StreamingAskResponsedeprecated",
        "StreamingBidResponsedeprecated",
        "StreamingDailyBarResponse",
        "StreamingHeartbeatResponse",
        "StreamingQuoteResponse",
        "StreamingTradeResponse",
    ]
]:
    if response.status_code == HTTPStatus.OK:

        def _parse_response_200(
            data: object,
        ) -> Union[
            "StreamingAskResponsedeprecated",
            "StreamingBidResponsedeprecated",
            "StreamingDailyBarResponse",
            "StreamingHeartbeatResponse",
            "StreamingQuoteResponse",
            "StreamingTradeResponse",
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = StreamingQuoteResponse.from_dict(data)

                return response_200_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_1 = StreamingTradeResponse.from_dict(data)

                return response_200_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_2 = StreamingDailyBarResponse.from_dict(data)

                return response_200_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_3 = StreamingHeartbeatResponse.from_dict(data)

                return response_200_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_4 = StreamingAskResponsedeprecated.from_dict(data)

                return response_200_type_4
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_5 = StreamingBidResponsedeprecated.from_dict(data)

            return response_200_type_5

        response_200 = _parse_response_200(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[
    Union[
        "StreamingAskResponsedeprecated",
        "StreamingBidResponsedeprecated",
        "StreamingDailyBarResponse",
        "StreamingHeartbeatResponse",
        "StreamingQuoteResponse",
        "StreamingTradeResponse",
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[
    Union[
        "StreamingAskResponsedeprecated",
        "StreamingBidResponsedeprecated",
        "StreamingDailyBarResponse",
        "StreamingHeartbeatResponse",
        "StreamingQuoteResponse",
        "StreamingTradeResponse",
    ]
]:
    r"""Stream of prices

     Stream of prices. Server constantly keeps the connection alive. If the
    connection is broken - the server constantly tries to restore it.
    TradingView establishes up to 4 simultaneous connections to this endpoint and
    expects to get the same data to all of them.
    Transfer mode is `chunked encoding`. The data feed should set `'Transfer-Encoding:
    chunked'` and make sure that all intermediate proxies are set to use this
    mode. All messages are to be ended with `\n`. Data stream should contain
    real-time data only. It shouldn't contain snapshots of data.

    Data feed should provide trades and quotes:
    - If trades are not provided, then data feed should set trades with bid price and bid size (mid
    price with 0 size in case of Forex).
    - Size is always greater than `0`, except for the correction. In that case size can be `0`.
    - Quote must contain prices of the best ask and the best bid.
    - Daily bars are required if they cannot be built from trades (has-daily should be set to true in
    the symbol information in that case).

    The broker must remove unnecessary restrictions (firewall, rate limits, etc.) for the set of IP
    addresses of our servers.

    `StreamingHeartbeatResponse` is a technical message that prevents the feed from unsubscribing from
    streaming.
    It doesn't affect the price data and should be sent to /streaming every 5 seconds by default. The
    message
    can be used, for example, when the trading session is closed on weekends or in case of low liquidity
    on the exchange when TradingView does not receive price updates for a long time.

    Please note, that `StreamingAskResponse` and `StreamingBidResponse` are deprecated.
    The `StreamingQuoteResponse` should be used to provide ask / bid data.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['StreamingAskResponsedeprecated', 'StreamingBidResponsedeprecated', 'StreamingDailyBarResponse', 'StreamingHeartbeatResponse', 'StreamingQuoteResponse', 'StreamingTradeResponse']]
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
) -> Optional[
    Union[
        "StreamingAskResponsedeprecated",
        "StreamingBidResponsedeprecated",
        "StreamingDailyBarResponse",
        "StreamingHeartbeatResponse",
        "StreamingQuoteResponse",
        "StreamingTradeResponse",
    ]
]:
    r"""Stream of prices

     Stream of prices. Server constantly keeps the connection alive. If the
    connection is broken - the server constantly tries to restore it.
    TradingView establishes up to 4 simultaneous connections to this endpoint and
    expects to get the same data to all of them.
    Transfer mode is `chunked encoding`. The data feed should set `'Transfer-Encoding:
    chunked'` and make sure that all intermediate proxies are set to use this
    mode. All messages are to be ended with `\n`. Data stream should contain
    real-time data only. It shouldn't contain snapshots of data.

    Data feed should provide trades and quotes:
    - If trades are not provided, then data feed should set trades with bid price and bid size (mid
    price with 0 size in case of Forex).
    - Size is always greater than `0`, except for the correction. In that case size can be `0`.
    - Quote must contain prices of the best ask and the best bid.
    - Daily bars are required if they cannot be built from trades (has-daily should be set to true in
    the symbol information in that case).

    The broker must remove unnecessary restrictions (firewall, rate limits, etc.) for the set of IP
    addresses of our servers.

    `StreamingHeartbeatResponse` is a technical message that prevents the feed from unsubscribing from
    streaming.
    It doesn't affect the price data and should be sent to /streaming every 5 seconds by default. The
    message
    can be used, for example, when the trading session is closed on weekends or in case of low liquidity
    on the exchange when TradingView does not receive price updates for a long time.

    Please note, that `StreamingAskResponse` and `StreamingBidResponse` are deprecated.
    The `StreamingQuoteResponse` should be used to provide ask / bid data.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['StreamingAskResponsedeprecated', 'StreamingBidResponsedeprecated', 'StreamingDailyBarResponse', 'StreamingHeartbeatResponse', 'StreamingQuoteResponse', 'StreamingTradeResponse']
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[
    Union[
        "StreamingAskResponsedeprecated",
        "StreamingBidResponsedeprecated",
        "StreamingDailyBarResponse",
        "StreamingHeartbeatResponse",
        "StreamingQuoteResponse",
        "StreamingTradeResponse",
    ]
]:
    r"""Stream of prices

     Stream of prices. Server constantly keeps the connection alive. If the
    connection is broken - the server constantly tries to restore it.
    TradingView establishes up to 4 simultaneous connections to this endpoint and
    expects to get the same data to all of them.
    Transfer mode is `chunked encoding`. The data feed should set `'Transfer-Encoding:
    chunked'` and make sure that all intermediate proxies are set to use this
    mode. All messages are to be ended with `\n`. Data stream should contain
    real-time data only. It shouldn't contain snapshots of data.

    Data feed should provide trades and quotes:
    - If trades are not provided, then data feed should set trades with bid price and bid size (mid
    price with 0 size in case of Forex).
    - Size is always greater than `0`, except for the correction. In that case size can be `0`.
    - Quote must contain prices of the best ask and the best bid.
    - Daily bars are required if they cannot be built from trades (has-daily should be set to true in
    the symbol information in that case).

    The broker must remove unnecessary restrictions (firewall, rate limits, etc.) for the set of IP
    addresses of our servers.

    `StreamingHeartbeatResponse` is a technical message that prevents the feed from unsubscribing from
    streaming.
    It doesn't affect the price data and should be sent to /streaming every 5 seconds by default. The
    message
    can be used, for example, when the trading session is closed on weekends or in case of low liquidity
    on the exchange when TradingView does not receive price updates for a long time.

    Please note, that `StreamingAskResponse` and `StreamingBidResponse` are deprecated.
    The `StreamingQuoteResponse` should be used to provide ask / bid data.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['StreamingAskResponsedeprecated', 'StreamingBidResponsedeprecated', 'StreamingDailyBarResponse', 'StreamingHeartbeatResponse', 'StreamingQuoteResponse', 'StreamingTradeResponse']]
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
) -> Optional[
    Union[
        "StreamingAskResponsedeprecated",
        "StreamingBidResponsedeprecated",
        "StreamingDailyBarResponse",
        "StreamingHeartbeatResponse",
        "StreamingQuoteResponse",
        "StreamingTradeResponse",
    ]
]:
    r"""Stream of prices

     Stream of prices. Server constantly keeps the connection alive. If the
    connection is broken - the server constantly tries to restore it.
    TradingView establishes up to 4 simultaneous connections to this endpoint and
    expects to get the same data to all of them.
    Transfer mode is `chunked encoding`. The data feed should set `'Transfer-Encoding:
    chunked'` and make sure that all intermediate proxies are set to use this
    mode. All messages are to be ended with `\n`. Data stream should contain
    real-time data only. It shouldn't contain snapshots of data.

    Data feed should provide trades and quotes:
    - If trades are not provided, then data feed should set trades with bid price and bid size (mid
    price with 0 size in case of Forex).
    - Size is always greater than `0`, except for the correction. In that case size can be `0`.
    - Quote must contain prices of the best ask and the best bid.
    - Daily bars are required if they cannot be built from trades (has-daily should be set to true in
    the symbol information in that case).

    The broker must remove unnecessary restrictions (firewall, rate limits, etc.) for the set of IP
    addresses of our servers.

    `StreamingHeartbeatResponse` is a technical message that prevents the feed from unsubscribing from
    streaming.
    It doesn't affect the price data and should be sent to /streaming every 5 seconds by default. The
    message
    can be used, for example, when the trading session is closed on weekends or in case of low liquidity
    on the exchange when TradingView does not receive price updates for a long time.

    Please note, that `StreamingAskResponse` and `StreamingBidResponse` are deprecated.
    The `StreamingQuoteResponse` should be used to provide ask / bid data.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['StreamingAskResponsedeprecated', 'StreamingBidResponsedeprecated', 'StreamingDailyBarResponse', 'StreamingHeartbeatResponse', 'StreamingQuoteResponse', 'StreamingTradeResponse']
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
