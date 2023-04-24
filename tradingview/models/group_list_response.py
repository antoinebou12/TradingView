from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar

import attr

from ..models.ok_status import OkStatus

if TYPE_CHECKING:
    from ..models.group_list import GroupList


T = TypeVar("T", bound="GroupListResponse")


@attr.s(auto_attribs=True)
class GroupListResponse:
    """
    Attributes:
        s (OkStatus): Status will always be `ok`. Example: ok.
        d (GroupList):  Example: {'groups': [{'id': 'broker_stocks'}, {'id': 'broker_futures'}, {'id': 'broker_forex'},
            {'id': 'broker_crypto'}]}.
    """

    s: OkStatus
    d: "GroupList"

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
        from ..models.group_list import GroupList

        d = src_dict.copy()
        s = OkStatus(d.pop("s"))

        d = GroupList.from_dict(d.pop("d"))

        group_list_response = cls(
            s=s,
            d=d,
        )

        return group_list_response
