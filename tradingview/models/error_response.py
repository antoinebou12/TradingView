from typing import Any, Dict, Type, TypeVar

import attr

from ..models.error_response_s import ErrorResponseS

T = TypeVar("T", bound="ErrorResponse")


@attr.s(auto_attribs=True)
class ErrorResponse:
    """
    Attributes:
        s (ErrorResponseS): Status will always be `error`. Example: error.
        errmsg (str): Error message. Example: An error occurred..
    """

    s: ErrorResponseS
    errmsg: str

    def to_dict(self) -> Dict[str, Any]:
        s = self.s.value

        errmsg = self.errmsg

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "s": s,
                "errmsg": errmsg,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        s = ErrorResponseS(d.pop("s"))

        errmsg = d.pop("errmsg")

        error_response = cls(
            s=s,
            errmsg=errmsg,
        )

        return error_response
