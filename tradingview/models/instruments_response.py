from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

from ..models.ok_status import OkStatus

if TYPE_CHECKING:
    from ..models.instrument import Instrument


T = TypeVar("T", bound="InstrumentsResponse")


@attr.s(auto_attribs=True)
class InstrumentsResponse:
    """
    Attributes:
        s (OkStatus): Status will always be `ok`. Example: ok.
        d (List['Instrument']):
    """

    s: OkStatus
    d: List["Instrument"]

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
        from ..models.instrument import Instrument

        d = src_dict.copy()
        s = OkStatus(d.pop("s"))

        d = []
        _d = d.pop("d")
        for d_item_data in _d:
            d_item = Instrument.from_dict(d_item_data)

            d.append(d_item)

        instruments_response = cls(
            s=s,
            d=d,
        )

        return instruments_response
