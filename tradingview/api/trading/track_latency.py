from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.success_response import SuccessResponse
from ...models.track_latency_data import TrackLatencyData
from ...types import Response


def _get_kwargs(
    account_id: str,
    *,
    client: AuthenticatedClient,
    form_data: TrackLatencyData,
) -> Dict[str, Any]:
    url = "{}/accounts/{accountId}/trackLatency".format(client.base_url, accountId=account_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "data": form_data.to_dict(),
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[SuccessResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SuccessResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[SuccessResponse]:
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
    form_data: TrackLatencyData,
) -> Response[SuccessResponse]:
    """Latency Tracking

     Endpoint is used to collect performance and statistical data for a particular request.
    Applies to the following endpoints:
      Place order: [/placeOrder](#operation/placeOrder)
      Modify order: [/modifyOrder](#operation/modifyOrder)
      Cancel order: [/cancelOrder](#operation/cancelOrder)
      Modify position: [/modifyPosition](#operation/modifyPosition)
      Close position: [/closePosition](#operation/closePosition)
    To enable latency tracking functionality the `supportTrackLatency` flag should be set to true in the
    account config. Please see the [/accounts](#operation/getAccounts) endpoint.

    Args:
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SuccessResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        client=client,
        form_data=form_data,
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
    form_data: TrackLatencyData,
) -> Optional[SuccessResponse]:
    """Latency Tracking

     Endpoint is used to collect performance and statistical data for a particular request.
    Applies to the following endpoints:
      Place order: [/placeOrder](#operation/placeOrder)
      Modify order: [/modifyOrder](#operation/modifyOrder)
      Cancel order: [/cancelOrder](#operation/cancelOrder)
      Modify position: [/modifyPosition](#operation/modifyPosition)
      Close position: [/closePosition](#operation/closePosition)
    To enable latency tracking functionality the `supportTrackLatency` flag should be set to true in the
    account config. Please see the [/accounts](#operation/getAccounts) endpoint.

    Args:
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SuccessResponse
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
        form_data=form_data,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient,
    form_data: TrackLatencyData,
) -> Response[SuccessResponse]:
    """Latency Tracking

     Endpoint is used to collect performance and statistical data for a particular request.
    Applies to the following endpoints:
      Place order: [/placeOrder](#operation/placeOrder)
      Modify order: [/modifyOrder](#operation/modifyOrder)
      Cancel order: [/cancelOrder](#operation/cancelOrder)
      Modify position: [/modifyPosition](#operation/modifyPosition)
      Close position: [/closePosition](#operation/closePosition)
    To enable latency tracking functionality the `supportTrackLatency` flag should be set to true in the
    account config. Please see the [/accounts](#operation/getAccounts) endpoint.

    Args:
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SuccessResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        client=client,
        form_data=form_data,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    *,
    client: AuthenticatedClient,
    form_data: TrackLatencyData,
) -> Optional[SuccessResponse]:
    """Latency Tracking

     Endpoint is used to collect performance and statistical data for a particular request.
    Applies to the following endpoints:
      Place order: [/placeOrder](#operation/placeOrder)
      Modify order: [/modifyOrder](#operation/modifyOrder)
      Cancel order: [/cancelOrder](#operation/cancelOrder)
      Modify position: [/modifyPosition](#operation/modifyPosition)
      Close position: [/closePosition](#operation/closePosition)
    To enable latency tracking functionality the `supportTrackLatency` flag should be set to true in the
    account config. Please see the [/accounts](#operation/getAccounts) endpoint.

    Args:
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SuccessResponse
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            form_data=form_data,
        )
    ).parsed
