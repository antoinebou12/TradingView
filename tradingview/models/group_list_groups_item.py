from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="GroupListGroupsItem")


@attr.s(auto_attribs=True)
class GroupListGroupsItem:
    """
    Attributes:
        id (str): All characters in a group id must be either a lowercase alphabetic character or an underscore.
            A group id should start with the same prefix related to the broker's name.
    """

    id: str

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        group_list_groups_item = cls(
            id=id,
        )

        return group_list_groups_item
