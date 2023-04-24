from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_manager_column import AccountManagerColumn


T = TypeVar("T", bound="AccountManagerTable")


@attr.s(auto_attribs=True)
class AccountManagerTable:
    """
    Attributes:
        id (str):  Example: accountSummary.
        columns (List['AccountManagerColumn']):
        title (Union[Unset, str]): Localized title of a table. Example: Account Summary.
    """

    id: str
    columns: List["AccountManagerColumn"]
    title: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        columns = []
        for columns_item_data in self.columns:
            columns_item = columns_item_data.to_dict()

            columns.append(columns_item)

        title = self.title

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "columns": columns,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.account_manager_column import AccountManagerColumn

        d = src_dict.copy()
        id = d.pop("id")

        columns = []
        _columns = d.pop("columns")
        for columns_item_data in _columns:
            columns_item = AccountManagerColumn.from_dict(columns_item_data)

            columns.append(columns_item)

        title = d.pop("title", UNSET)

        account_manager_table = cls(
            id=id,
            columns=columns,
            title=title,
        )

        return account_manager_table
