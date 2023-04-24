from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.account_manager_column_alignment import AccountManagerColumnAlignment
from ..types import UNSET, Unset

T = TypeVar("T", bound="AccountManagerColumn")


@attr.s(auto_attribs=True)
class AccountManagerColumn:
    """
    Attributes:
        id (str):  Example: balance.
        title (str): Localized title of a column. Example: Balance.
        tooltip (Union[Unset, str]): Tooltip that is shown on mouse hover. Example: Balance column.
        alignment (Union[Unset, AccountManagerColumnAlignment]): The cell value alignment. Default value is `left`
            Default: AccountManagerColumnAlignment.LEFT. Example: right.
        is_capitalize (Union[Unset, bool]): The first character of each word in the sentence will be capitalized. The
            rest of the symbols appearance does not change. Default: True.
    """

    id: str
    title: str
    tooltip: Union[Unset, str] = UNSET
    alignment: Union[Unset, AccountManagerColumnAlignment] = AccountManagerColumnAlignment.LEFT
    is_capitalize: Union[Unset, bool] = True

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        title = self.title
        tooltip = self.tooltip
        alignment: Union[Unset, str] = UNSET
        if not isinstance(self.alignment, Unset):
            alignment = self.alignment.value

        is_capitalize = self.is_capitalize

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "title": title,
            }
        )
        if tooltip is not UNSET:
            field_dict["tooltip"] = tooltip
        if alignment is not UNSET:
            field_dict["alignment"] = alignment
        if is_capitalize is not UNSET:
            field_dict["isCapitalize"] = is_capitalize

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        title = d.pop("title")

        tooltip = d.pop("tooltip", UNSET)

        _alignment = d.pop("alignment", UNSET)
        alignment: Union[Unset, AccountManagerColumnAlignment]
        if isinstance(_alignment, Unset):
            alignment = UNSET
        else:
            alignment = AccountManagerColumnAlignment(_alignment)

        is_capitalize = d.pop("isCapitalize", UNSET)

        account_manager_column = cls(
            id=id,
            title=title,
            tooltip=tooltip,
            alignment=alignment,
            is_capitalize=is_capitalize,
        )

        return account_manager_column
