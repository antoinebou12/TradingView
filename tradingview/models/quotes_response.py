from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

from ..models.ok_status import OkStatus

if TYPE_CHECKING:
    from ..models.quotes_response_d_item import QuotesResponseDItem


T = TypeVar("T", bound="QuotesResponse")


@attr.s(auto_attribs=True)
class QuotesResponse:
    """
    Attributes:
        s (OkStatus): Status will always be `ok`. Example: ok.
        d (List['QuotesResponseDItem']):
    """

    s: OkStatus
    d: List["QuotesResponseDItem"]

    def to_dict(self) -> Dict[str, Any]:
        s = self.s.value

        d = []
        for d_item_data in self.d:
            d_item = d_item_data.to_dict()

            d.append(d_item)

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
        from ..models.quotes_response_d_item import QuotesResponseDItem

        d = src_dict.copy()
        s = OkStatus(d.pop("s"))

        d = []
        _d = d.pop("d")
        for d_item_data in _d:
            d_item = QuotesResponseDItem.from_dict(d_item_data)

            d.append(d_item)

        quotes_response = cls(
            s=s,
            d=d,
        )

        return quotes_response
