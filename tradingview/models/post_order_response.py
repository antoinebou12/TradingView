from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar

import attr

from ..models.ok_status import OkStatus

if TYPE_CHECKING:
    from ..models.post_order_response_d import PostOrderResponseD


T = TypeVar("T", bound="PostOrderResponse")


@attr.s(auto_attribs=True)
class PostOrderResponse:
    """
    Attributes:
        s (OkStatus): Status will always be `ok`. Example: ok.
        d (PostOrderResponseD):
    """

    s: OkStatus
    d: "PostOrderResponseD"

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
        from ..models.post_order_response_d import PostOrderResponseD

        d = src_dict.copy()
        s = OkStatus(d.pop("s"))

        d = PostOrderResponseD.from_dict(d.pop("d"))

        post_order_response = cls(
            s=s,
            d=d,
        )

        return post_order_response
