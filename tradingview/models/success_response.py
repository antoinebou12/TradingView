from typing import Any, Dict, Type, TypeVar

import attr

from ..models.success_response_s import SuccessResponseS

T = TypeVar("T", bound="SuccessResponse")


@attr.s(auto_attribs=True)
class SuccessResponse:
    """
    Attributes:
        s (SuccessResponseS): Status will always be `ok`. Example: ok.
    """

    s: SuccessResponseS

    def to_dict(self) -> Dict[str, Any]:
        s = self.s.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "s": s,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        s = SuccessResponseS(d.pop("s"))

        success_response = cls(
            s=s,
        )

        return success_response
