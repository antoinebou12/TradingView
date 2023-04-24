from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

from ..models.ok_status import OkStatus

if TYPE_CHECKING:
    from ..models.set_leverage import SetLeverage


T = TypeVar("T", bound="SetLeverageResponse")


@attr.s(auto_attribs=True)
class SetLeverageResponse:
    """
    Attributes:
        s (OkStatus): Status will always be `ok`. Example: ok.
        d (SetLeverage):  Example: {'leverage': 25}.
    """

    s: OkStatus
    d: "SetLeverage"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        s = self.s.value

        d = self.d.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "s": s,
                "d": d,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.set_leverage import SetLeverage

        d = src_dict.copy()
        s = OkStatus(d.pop("s"))

        d = SetLeverage.from_dict(d.pop("d"))

        set_leverage_response = cls(
            s=s,
            d=d,
        )

        set_leverage_response.additional_properties = d
        return set_leverage_response

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
