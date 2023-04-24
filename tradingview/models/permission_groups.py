from typing import Any, Dict, List, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="PermissionGroups")


@attr.s(auto_attribs=True)
class PermissionGroups:
    """
    Example:
        {'groups': ['broker_futures', 'broker_stocks', 'broker_forex']}

    Attributes:
        groups (List[str]): Groups list. Each element of this array is a group identifier.
    """

    groups: List[str]

    def to_dict(self) -> Dict[str, Any]:
        groups = self.groups

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "groups": groups,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        groups = cast(List[str], d.pop("groups"))

        permission_groups = cls(
            groups=groups,
        )

        return permission_groups
