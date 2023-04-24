from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.group_list_groups_item import GroupListGroupsItem


T = TypeVar("T", bound="GroupList")


@attr.s(auto_attribs=True)
class GroupList:
    """
    Example:
        {'groups': [{'id': 'broker_stocks'}, {'id': 'broker_futures'}, {'id': 'broker_forex'}, {'id': 'broker_crypto'}]}

    Attributes:
        groups (Union[Unset, List['GroupListGroupsItem']]): Each element of this array is an group object.
    """

    groups: Union[Unset, List["GroupListGroupsItem"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        groups: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()

                groups.append(groups_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if groups is not UNSET:
            field_dict["groups"] = groups

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.group_list_groups_item import GroupListGroupsItem

        d = src_dict.copy()
        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            groups_item = GroupListGroupsItem.from_dict(groups_item_data)

            groups.append(groups_item)

        group_list = cls(
            groups=groups,
        )

        return group_list
