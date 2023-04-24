from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CheckBoxMetainfo")


@attr.s(auto_attribs=True)
class CheckBoxMetainfo:
    """
    Attributes:
        id (str): Unique field identifier. Example: customInputFieldId.
        title (str): Localized checkbox display name. Example: Additional parameter.
        save_to_settings (Union[Unset, bool]): Whether the value should be stored in the user settings and preserved for
            the next time the dialog is displayed. Example: True.
        help_ (Union[Unset, str]): Help text displayed when hovering over the checkbox. Example: Brief help text.
        checked (Union[Unset, bool]): Initial checkbox value.
        mutable (Union[Unset, bool]): Whether this field can be changed during the order modification. Default: True.
    """

    id: str
    title: str
    save_to_settings: Union[Unset, bool] = False
    help_: Union[Unset, str] = UNSET
    checked: Union[Unset, bool] = False
    mutable: Union[Unset, bool] = True
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        title = self.title
        save_to_settings = self.save_to_settings
        help_ = self.help_
        checked = self.checked
        mutable = self.mutable

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "title": title,
            }
        )
        if save_to_settings is not UNSET:
            field_dict["saveToSettings"] = save_to_settings
        if help_ is not UNSET:
            field_dict["help"] = help_
        if checked is not UNSET:
            field_dict["checked"] = checked
        if mutable is not UNSET:
            field_dict["mutable"] = mutable

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        title = d.pop("title")

        save_to_settings = d.pop("saveToSettings", UNSET)

        help_ = d.pop("help", UNSET)

        checked = d.pop("checked", UNSET)

        mutable = d.pop("mutable", UNSET)

        check_box_metainfo = cls(
            id=id,
            title=title,
            save_to_settings=save_to_settings,
            help_=help_,
            checked=checked,
            mutable=mutable,
        )

        check_box_metainfo.additional_properties = d
        return check_box_metainfo

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
