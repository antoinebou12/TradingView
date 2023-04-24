from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar

import attr

from ..models.ok_status import OkStatus

if TYPE_CHECKING:
    from ..models.preview_order import PreviewOrder


T = TypeVar("T", bound="PreviewOrderResponse")


@attr.s(auto_attribs=True)
class PreviewOrderResponse:
    """
    Attributes:
        s (OkStatus): Status will always be `ok`. Example: ok.
        d (PreviewOrder):  Example: {'confirmId': 112358, 'sections': [{'header': 'Estimated', 'rows': [{'title':
            'Estimated Commission', 'value': 0.01}, {'title': 'Estimated Price', 'value': 4091}]}, {'rows': [{'title':
            'Margin Value', 'value': 12100}, {'title': 'Time In Force', 'value': 'DAY'}]}], 'warnings': ['Estimated money
            impact is for main order only.', 'Order can be executed outside regular trading hours.'], 'errors': ['Failed to
            build order confirmation.']}.
    """

    s: OkStatus
    d: "PreviewOrder"

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
        from ..models.preview_order import PreviewOrder

        d = src_dict.copy()
        s = OkStatus(d.pop("s"))

        d = PreviewOrder.from_dict(d.pop("d"))

        preview_order_response = cls(
            s=s,
            d=d,
        )

        return preview_order_response
