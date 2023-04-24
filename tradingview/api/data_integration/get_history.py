from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.history_empty_bar_response import HistoryEmptyBarResponse
from ...models.history_success_response import HistorySuccessResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    symbol: str,
    resolution: str,
    from_: float,
    to: float,
    countback: Union[Unset, None, float] = UNSET,
) -> Dict[str, Any]:
    url = "{}/history".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["symbol"] = symbol

    params["resolution"] = resolution

    params["from"] = from_

    params["to"] = to

    params["countback"] = countback

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
) -> Optional[Union["ErrorResponse", "HistoryEmptyBarResponse", "HistorySuccessResponse"]]:
    if response.status_code == HTTPStatus.OK:

        def _parse_response_200(
            data: object,
        ) -> Union["ErrorResponse", "HistoryEmptyBarResponse", "HistorySuccessResponse"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = HistorySuccessResponse.from_dict(data)

                return response_200_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_1 = HistoryEmptyBarResponse.from_dict(data)

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
) -> Response[Union["ErrorResponse", "HistoryEmptyBarResponse", "HistorySuccessResponse"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    symbol: str,
    resolution: str,
    from_: float,
    to: float,
    countback: Union[Unset, None, float] = UNSET,
) -> Response[Union["ErrorResponse", "HistoryEmptyBarResponse", "HistorySuccessResponse"]]:
    r"""History

     Request for history bars. Each property of the response object is treated as a table column.

    Data should meet the following requirements:

    - real-time data obtained from the API streaming endpoint must match the historical data, obtained
    from the
      /history API. The allowed count of mismatched bars (candles) must not exceed 5% for frequently
    traded symbols,
      otherwise the integration to TradingView is not possible;
    - the data must not include unreasonable price gaps, historical data gaps on 1-minute and Daily-
    resolutions
      (temporal gaps), obviously incorrect prices (adhesions).

    Bar time for daily bars should be 00:00 UTC and is expected to be a trading day
    (not a day when the session starts).

    Bar time for monthly bars should be 00:00 UTC and is the first trading day of the month.

    If there is no data in the requested time period, you should return an empty response:
    `{\"s\":\"ok\",\"t\":[],\"o\":[],\"h\":[],\"l\":[],\"c\":[],\"v\":[]}`

    Args:
        symbol (str):
        resolution (str):
        from_ (float):
        to (float):
        countback (Union[Unset, None, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['ErrorResponse', 'HistoryEmptyBarResponse', 'HistorySuccessResponse']]
    """

    kwargs = _get_kwargs(
        client=client,
        symbol=symbol,
        resolution=resolution,
        from_=from_,
        to=to,
        countback=countback,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    symbol: str,
    resolution: str,
    from_: float,
    to: float,
    countback: Union[Unset, None, float] = UNSET,
) -> Optional[Union["ErrorResponse", "HistoryEmptyBarResponse", "HistorySuccessResponse"]]:
    r"""History

     Request for history bars. Each property of the response object is treated as a table column.

    Data should meet the following requirements:

    - real-time data obtained from the API streaming endpoint must match the historical data, obtained
    from the
      /history API. The allowed count of mismatched bars (candles) must not exceed 5% for frequently
    traded symbols,
      otherwise the integration to TradingView is not possible;
    - the data must not include unreasonable price gaps, historical data gaps on 1-minute and Daily-
    resolutions
      (temporal gaps), obviously incorrect prices (adhesions).

    Bar time for daily bars should be 00:00 UTC and is expected to be a trading day
    (not a day when the session starts).

    Bar time for monthly bars should be 00:00 UTC and is the first trading day of the month.

    If there is no data in the requested time period, you should return an empty response:
    `{\"s\":\"ok\",\"t\":[],\"o\":[],\"h\":[],\"l\":[],\"c\":[],\"v\":[]}`

    Args:
        symbol (str):
        resolution (str):
        from_ (float):
        to (float):
        countback (Union[Unset, None, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['ErrorResponse', 'HistoryEmptyBarResponse', 'HistorySuccessResponse']
    """

    return sync_detailed(
        client=client,
        symbol=symbol,
        resolution=resolution,
        from_=from_,
        to=to,
        countback=countback,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    symbol: str,
    resolution: str,
    from_: float,
    to: float,
    countback: Union[Unset, None, float] = UNSET,
) -> Response[Union["ErrorResponse", "HistoryEmptyBarResponse", "HistorySuccessResponse"]]:
    r"""History

     Request for history bars. Each property of the response object is treated as a table column.

    Data should meet the following requirements:

    - real-time data obtained from the API streaming endpoint must match the historical data, obtained
    from the
      /history API. The allowed count of mismatched bars (candles) must not exceed 5% for frequently
    traded symbols,
      otherwise the integration to TradingView is not possible;
    - the data must not include unreasonable price gaps, historical data gaps on 1-minute and Daily-
    resolutions
      (temporal gaps), obviously incorrect prices (adhesions).

    Bar time for daily bars should be 00:00 UTC and is expected to be a trading day
    (not a day when the session starts).

    Bar time for monthly bars should be 00:00 UTC and is the first trading day of the month.

    If there is no data in the requested time period, you should return an empty response:
    `{\"s\":\"ok\",\"t\":[],\"o\":[],\"h\":[],\"l\":[],\"c\":[],\"v\":[]}`

    Args:
        symbol (str):
        resolution (str):
        from_ (float):
        to (float):
        countback (Union[Unset, None, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['ErrorResponse', 'HistoryEmptyBarResponse', 'HistorySuccessResponse']]
    """

    kwargs = _get_kwargs(
        client=client,
        symbol=symbol,
        resolution=resolution,
        from_=from_,
        to=to,
        countback=countback,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    symbol: str,
    resolution: str,
    from_: float,
    to: float,
    countback: Union[Unset, None, float] = UNSET,
) -> Optional[Union["ErrorResponse", "HistoryEmptyBarResponse", "HistorySuccessResponse"]]:
    r"""History

     Request for history bars. Each property of the response object is treated as a table column.

    Data should meet the following requirements:

    - real-time data obtained from the API streaming endpoint must match the historical data, obtained
    from the
      /history API. The allowed count of mismatched bars (candles) must not exceed 5% for frequently
    traded symbols,
      otherwise the integration to TradingView is not possible;
    - the data must not include unreasonable price gaps, historical data gaps on 1-minute and Daily-
    resolutions
      (temporal gaps), obviously incorrect prices (adhesions).

    Bar time for daily bars should be 00:00 UTC and is expected to be a trading day
    (not a day when the session starts).

    Bar time for monthly bars should be 00:00 UTC and is the first trading day of the month.

    If there is no data in the requested time period, you should return an empty response:
    `{\"s\":\"ok\",\"t\":[],\"o\":[],\"h\":[],\"l\":[],\"c\":[],\"v\":[]}`

    Args:
        symbol (str):
        resolution (str):
        from_ (float):
        to (float):
        countback (Union[Unset, None, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['ErrorResponse', 'HistoryEmptyBarResponse', 'HistorySuccessResponse']
    """

    return (
        await asyncio_detailed(
            client=client,
            symbol=symbol,
            resolution=resolution,
            from_=from_,
            to=to,
            countback=countback,
        )
    ).parsed
