from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar

import attr

from ..models.ok_status import OkStatus

if TYPE_CHECKING:
    from ..models.access_token import AccessToken


T = TypeVar("T", bound="AuthorizeResponse")


@attr.s(auto_attribs=True)
class AuthorizeResponse:
    """
    Attributes:
        s (OkStatus): Status will always be `ok`. Example: ok.
        d (AccessToken): Access token.
    """

    s: OkStatus
    d: "AccessToken"

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
        from ..models.access_token import AccessToken

        d = src_dict.copy()
        s = OkStatus(d.pop("s"))

        d = AccessToken.from_dict(d.pop("d"))

        authorize_response = cls(
            s=s,
            d=d,
        )

        return authorize_response
