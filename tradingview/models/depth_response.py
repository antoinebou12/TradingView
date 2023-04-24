from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar

import attr

from ..models.ok_status import OkStatus

if TYPE_CHECKING:
    from ..models.depth import Depth


T = TypeVar("T", bound="DepthResponse")


@attr.s(auto_attribs=True)
class DepthResponse:
    """
    Attributes:
        s (OkStatus): Status will always be `ok`. Example: ok.
        d (Depth): Depth of market for an instrument. Example: {'asks': [[45.1, 100], [48.4, 120]], 'bids': [[24.7, 80],
            [35.6, 30]]}.
    """

    s: OkStatus
    d: "Depth"

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
        from ..models.depth import Depth

        d = src_dict.copy()
        s = OkStatus(d.pop("s"))

        d = Depth.from_dict(d.pop("d"))

        depth_response = cls(
            s=s,
            d=d,
        )

        return depth_response
