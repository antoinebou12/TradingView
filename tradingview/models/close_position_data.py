from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClosePositionData")


@attr.s(auto_attribs=True)
class ClosePositionData:
    """
    Attributes:
        amount (Union[Unset, float]): Amount to close. This property is used if supportPartialClosePosition flag is
            `true`.
    """

    amount: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amount = self.amount

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        amount = d.pop("amount", UNSET)

        close_position_data = cls(
            amount=amount,
        )

        close_position_data.additional_properties = d
        return close_position_data

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
