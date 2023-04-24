from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="AccountSummaryRowItem")


@attr.s(auto_attribs=True)
class AccountSummaryRowItem:
    """
    Attributes:
        id (str): Unique Account Summary Row item identifier.
        title (str): Localized Account Summary Row item title.
    """

    id: str
    title: str

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        title = self.title

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "title": title,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        title = d.pop("title")

        account_summary_row_item = cls(
            id=id,
            title=title,
        )

        return account_summary_row_item
