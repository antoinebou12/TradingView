from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrderCommonDuration")


@attr.s(auto_attribs=True)
class OrderCommonDuration:
    """Expiration type and Unix timestamp date/time.

    Attributes:
        type (str): Duration ID. Internal ID that you set in [/config](#operation/getConfiguration) response.
        datetime_ (Union[Unset, float]): Unix timestamp (UTC).
    """

    type: str
    datetime_: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        datetime_ = self.datetime_

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if datetime_ is not UNSET:
            field_dict["datetime"] = datetime_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        datetime_ = d.pop("datetime", UNSET)

        order_common_duration = cls(
            type=type,
            datetime_=datetime_,
        )

        order_common_duration.additional_properties = d
        return order_common_duration

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
