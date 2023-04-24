from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.set_leverage_data_order_type import SetLeverageDataOrderType
from ..models.set_leverage_data_side import SetLeverageDataSide

T = TypeVar("T", bound="SetLeverageData")


@attr.s(auto_attribs=True)
class SetLeverageData:
    """
    Attributes:
        instrument (str): Broker instrument name. Example: BTCPERP.
        side (SetLeverageDataSide): Current order side in the order ticket.
        order_type (SetLeverageDataOrderType): Current order type selected in the order ticket.
        leverage (float): Leverage value set by the user Example: 25.
    """

    instrument: str
    side: SetLeverageDataSide
    order_type: SetLeverageDataOrderType
    leverage: float
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        instrument = self.instrument
        side = self.side.value

        order_type = self.order_type.value

        leverage = self.leverage

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "instrument": instrument,
                "side": side,
                "orderType": order_type,
                "leverage": leverage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        instrument = d.pop("instrument")

        side = SetLeverageDataSide(d.pop("side"))

        order_type = SetLeverageDataOrderType(d.pop("orderType"))

        leverage = d.pop("leverage")

        set_leverage_data = cls(
            instrument=instrument,
            side=side,
            order_type=order_type,
            leverage=leverage,
        )

        set_leverage_data.additional_properties = d
        return set_leverage_data

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
