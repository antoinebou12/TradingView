from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.get_leverage_data_order_type import GetLeverageDataOrderType
from ..models.get_leverage_data_side import GetLeverageDataSide

T = TypeVar("T", bound="GetLeverageData")


@attr.s(auto_attribs=True)
class GetLeverageData:
    """
    Attributes:
        instrument (str): Broker instrument name. Example: BTCPERP.
        side (GetLeverageDataSide): Current order side in the order ticket.
        order_type (GetLeverageDataOrderType): Current order type selected in the order ticket.
    """

    instrument: str
    side: GetLeverageDataSide
    order_type: GetLeverageDataOrderType
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        instrument = self.instrument
        side = self.side.value

        order_type = self.order_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "instrument": instrument,
                "side": side,
                "orderType": order_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        instrument = d.pop("instrument")

        side = GetLeverageDataSide(d.pop("side"))

        order_type = GetLeverageDataOrderType(d.pop("orderType"))

        get_leverage_data = cls(
            instrument=instrument,
            side=side,
            order_type=order_type,
        )

        get_leverage_data.additional_properties = d
        return get_leverage_data

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
