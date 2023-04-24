from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar

import attr

from ..models.ok_status import OkStatus

if TYPE_CHECKING:
    from ..models.config import Config


T = TypeVar("T", bound="ConfigResponse")


@attr.s(auto_attribs=True)
class ConfigResponse:
    """
    Attributes:
        s (OkStatus): Status will always be `ok`. Example: ok.
        d (Config):
    """

    s: OkStatus
    d: "Config"

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
        from ..models.config import Config

        d = src_dict.copy()
        s = OkStatus(d.pop("s"))

        d = Config.from_dict(d.pop("d"))

        config_response = cls(
            s=s,
            d=d,
        )

        return config_response
