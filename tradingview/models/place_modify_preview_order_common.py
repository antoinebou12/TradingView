from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlaceModifyPreviewOrderCommon")


@attr.s(auto_attribs=True)
class PlaceModifyPreviewOrderCommon:
    """
    Attributes:
        qty (Union[Unset, float]): The number of units. Example: 1.
        limit_price (Union[Unset, float]): Limit Price for Limit or StopLimit order. Example: 1.23456.
        stop_price (Union[Unset, float]): Stop Price for Stop or StopLimit order.
        duration_type (Union[Unset, str]): Duration ID (if supported). Example: gtt.
        duration_date_time (Union[Unset, float]): Expiration datetime Unix timestamp (if supported by duration type).
            Example: 1548406235.
        stop_loss (Union[Unset, float]): StopLoss price (if supported).
        trailing_stop_pips (Union[Unset, float]): Distance from the stop loss level to the current market price in pips
            (if supported by the broker).
        take_profit (Union[Unset, float]): TakeProfit price (if supported).
        digital_signature (Union[Unset, str]): Digital signature (if supported). Example: 954345868.
        current_ask (Union[Unset, float]): Current ask price for the instrument that the user sees in the order panel.
            Example: 1.25.
        current_bid (Union[Unset, float]): Current bid price for the instrument that the user sees in the order panel.
            Example: 1.23.
    """

    qty: Union[Unset, float] = UNSET
    limit_price: Union[Unset, float] = UNSET
    stop_price: Union[Unset, float] = UNSET
    duration_type: Union[Unset, str] = UNSET
    duration_date_time: Union[Unset, float] = UNSET
    stop_loss: Union[Unset, float] = UNSET
    trailing_stop_pips: Union[Unset, float] = UNSET
    take_profit: Union[Unset, float] = UNSET
    digital_signature: Union[Unset, str] = UNSET
    current_ask: Union[Unset, float] = UNSET
    current_bid: Union[Unset, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        qty = self.qty
        limit_price = self.limit_price
        stop_price = self.stop_price
        duration_type = self.duration_type
        duration_date_time = self.duration_date_time
        stop_loss = self.stop_loss
        trailing_stop_pips = self.trailing_stop_pips
        take_profit = self.take_profit
        digital_signature = self.digital_signature
        current_ask = self.current_ask
        current_bid = self.current_bid

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if qty is not UNSET:
            field_dict["qty"] = qty
        if limit_price is not UNSET:
            field_dict["limitPrice"] = limit_price
        if stop_price is not UNSET:
            field_dict["stopPrice"] = stop_price
        if duration_type is not UNSET:
            field_dict["durationType"] = duration_type
        if duration_date_time is not UNSET:
            field_dict["durationDateTime"] = duration_date_time
        if stop_loss is not UNSET:
            field_dict["stopLoss"] = stop_loss
        if trailing_stop_pips is not UNSET:
            field_dict["trailingStopPips"] = trailing_stop_pips
        if take_profit is not UNSET:
            field_dict["takeProfit"] = take_profit
        if digital_signature is not UNSET:
            field_dict["digitalSignature"] = digital_signature
        if current_ask is not UNSET:
            field_dict["currentAsk"] = current_ask
        if current_bid is not UNSET:
            field_dict["currentBid"] = current_bid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        qty = d.pop("qty", UNSET)

        limit_price = d.pop("limitPrice", UNSET)

        stop_price = d.pop("stopPrice", UNSET)

        duration_type = d.pop("durationType", UNSET)

        duration_date_time = d.pop("durationDateTime", UNSET)

        stop_loss = d.pop("stopLoss", UNSET)

        trailing_stop_pips = d.pop("trailingStopPips", UNSET)

        take_profit = d.pop("takeProfit", UNSET)

        digital_signature = d.pop("digitalSignature", UNSET)

        current_ask = d.pop("currentAsk", UNSET)

        current_bid = d.pop("currentBid", UNSET)

        place_modify_preview_order_common = cls(
            qty=qty,
            limit_price=limit_price,
            stop_price=stop_price,
            duration_type=duration_type,
            duration_date_time=duration_date_time,
            stop_loss=stop_loss,
            trailing_stop_pips=trailing_stop_pips,
            take_profit=take_profit,
            digital_signature=digital_signature,
            current_ask=current_ask,
            current_bid=current_bid,
        )

        return place_modify_preview_order_common
