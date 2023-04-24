from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar

import attr

from ..models.ok_status import OkStatus

if TYPE_CHECKING:
    from ..models.get_leverage import GetLeverage


T = TypeVar("T", bound="GetLeverageResponse")


@attr.s(auto_attribs=True)
class GetLeverageResponse:
    """
    Attributes:
        s (OkStatus): Status will always be `ok`. Example: ok.
        d (GetLeverage):  Example: {'title': 'Adjust Leverage', 'leverage': 5, 'min': 1, 'max': 10, 'step': 1}.
    """

    s: OkStatus
    d: "GetLeverage"

    def to_dict(self) -> Dict[str, Any]:
        s = self.s.value

        d = self.d.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "s": s,
                "d": d,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_leverage import GetLeverage

        d = src_dict.copy()
        s = OkStatus(d.pop("s"))

        d = GetLeverage.from_dict(d.pop("d"))

        get_leverage_response = cls(
            s=s,
            d=d,
        )

        return get_leverage_response
