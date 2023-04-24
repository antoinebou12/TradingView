from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar

import attr

from ..models.ok_status import OkStatus

if TYPE_CHECKING:
    from ..models.permission_groups import PermissionGroups


T = TypeVar("T", bound="PermissionsResponse")


@attr.s(auto_attribs=True)
class PermissionsResponse:
    """
    Attributes:
        s (OkStatus): Status will always be `ok`. Example: ok.
        d (PermissionGroups):  Example: {'groups': ['broker_futures', 'broker_stocks', 'broker_forex']}.
    """

    s: OkStatus
    d: "PermissionGroups"

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
        from ..models.permission_groups import PermissionGroups

        d = src_dict.copy()
        s = OkStatus(d.pop("s"))

        d = PermissionGroups.from_dict(d.pop("d"))

        permissions_response = cls(
            s=s,
            d=d,
        )

        return permissions_response
