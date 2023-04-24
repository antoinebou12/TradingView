from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar

import attr

from ..models.ok_status import OkStatus

if TYPE_CHECKING:
    from ..models.preview_leverage import PreviewLeverage


T = TypeVar("T", bound="PreviewLeverageResponse")


@attr.s(auto_attribs=True)
class PreviewLeverageResponse:
    """
    Attributes:
        s (OkStatus): Status will always be `ok`. Example: ok.
        d (PreviewLeverage):  Example: {'infos': ['Borrowing limit at current leverage 0.3057 BTC or 0.00000 USDT',
            'Required position margin at current leverage 0.3057 BTC'], 'warnings': ['Your leverage is comparatively high.
            Please be aware of risks'], 'errors': ['Invalid leverage value']}.
    """

    s: OkStatus
    d: "PreviewLeverage"

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
        from ..models.preview_leverage import PreviewLeverage

        d = src_dict.copy()
        s = OkStatus(d.pop("s"))

        d = PreviewLeverage.from_dict(d.pop("d"))

        preview_leverage_response = cls(
            s=s,
            d=d,
        )

        return preview_leverage_response
