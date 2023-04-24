from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.modify_position_data_side import ModifyPositionDataSide
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModifyPositionData")


@attr.s(auto_attribs=True)
class ModifyPositionData:
    """
    Attributes:
        side (Union[Unset, ModifyPositionDataSide]): New side of the position. This parameter is used to reverse the
            position,
            if the `supportNativeReversePosition` flag is enabled in the account config.
            Please see the [/accounts](#operation/getAccounts) endpoint.
        stop_loss (Union[Unset, float]): StopLoss price. Example: 1.283568.
        trailing_stop_pips (Union[Unset, float]): Distance from the stop loss level to the order price in pips.
        take_profit (Union[Unset, float]): TakeProfit price. Example: 1.294436.
        current_ask (Union[Unset, float]): Current ask price for the instrument that the user sees in the order panel.
            Example: 1.287367.
        current_bid (Union[Unset, float]): Current bid price for the instrument that the user sees in the order panel.
            Example: 1.28554.
    """

    side: Union[Unset, ModifyPositionDataSide] = UNSET
    stop_loss: Union[Unset, float] = UNSET
    trailing_stop_pips: Union[Unset, float] = UNSET
    take_profit: Union[Unset, float] = UNSET
    current_ask: Union[Unset, float] = UNSET
    current_bid: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        side: Union[Unset, str] = UNSET
        if not isinstance(self.side, Unset):
            side = self.side.value

        stop_loss = self.stop_loss
        trailing_stop_pips = self.trailing_stop_pips
        take_profit = self.take_profit
        current_ask = self.current_ask
        current_bid = self.current_bid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if side is not UNSET:
            field_dict["side"] = side
        if stop_loss is not UNSET:
            field_dict["stopLoss"] = stop_loss
        if trailing_stop_pips is not UNSET:
            field_dict["trailingStopPips"] = trailing_stop_pips
        if take_profit is not UNSET:
            field_dict["takeProfit"] = take_profit
        if current_ask is not UNSET:
            field_dict["currentAsk"] = current_ask
        if current_bid is not UNSET:
            field_dict["currentBid"] = current_bid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _side = d.pop("side", UNSET)
        side: Union[Unset, ModifyPositionDataSide]
        if isinstance(_side, Unset):
            side = UNSET
        else:
            side = ModifyPositionDataSide(_side)

        stop_loss = d.pop("stopLoss", UNSET)

        trailing_stop_pips = d.pop("trailingStopPips", UNSET)

        take_profit = d.pop("takeProfit", UNSET)

        current_ask = d.pop("currentAsk", UNSET)

        current_bid = d.pop("currentBid", UNSET)

        modify_position_data = cls(
            side=side,
            stop_loss=stop_loss,
            trailing_stop_pips=trailing_stop_pips,
            take_profit=take_profit,
            current_ask=current_ask,
            current_bid=current_bid,
        )

        modify_position_data.additional_properties = d
        return modify_position_data

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
