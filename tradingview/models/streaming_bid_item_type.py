from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="StreamingBidItemType")


@attr.s(auto_attribs=True)
class StreamingBidItemType:
    """Bid

    Attributes:
        f (Union[Unset, str]): Should always be `b`. Example: b.
    """

    f: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        f = self.f

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if f is not UNSET:
            field_dict["f"] = f

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        f = d.pop("f", UNSET)

        streaming_bid_item_type = cls(
            f=f,
        )

        streaming_bid_item_type.additional_properties = d
        return streaming_bid_item_type

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
