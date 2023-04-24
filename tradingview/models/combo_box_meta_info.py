from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.combo_box_value import ComboBoxValue


T = TypeVar("T", bound="ComboBoxMetaInfo")


@attr.s(auto_attribs=True)
class ComboBoxMetaInfo:
    """
    Attributes:
        id (str): Unique field identifier. Example: customInputFieldId.
        title (str): Localized field display name. Example: Additional parameters.
        items (List['ComboBoxValue']):
        save_to_settings (Union[Unset, bool]): Whether the value should be stored in the user settings and preserved for
            the next time the dialog is displayed. Example: True.
        mutable (Union[Unset, bool]): Whether this field can be changed during the order modification. Default: True.
        force_user_enter_initial_value (Union[Unset, bool]): If this flag is set to true, the user will not be able to
            place an order without explicitly entering a value, so instant order placement is not available. Example: True.
    """

    id: str
    title: str
    items: List["ComboBoxValue"]
    save_to_settings: Union[Unset, bool] = False
    mutable: Union[Unset, bool] = True
    force_user_enter_initial_value: Union[Unset, bool] = False

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        title = self.title
        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()

            items.append(items_item)

        save_to_settings = self.save_to_settings
        mutable = self.mutable
        force_user_enter_initial_value = self.force_user_enter_initial_value

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "title": title,
                "items": items,
            }
        )
        if save_to_settings is not UNSET:
            field_dict["saveToSettings"] = save_to_settings
        if mutable is not UNSET:
            field_dict["mutable"] = mutable
        if force_user_enter_initial_value is not UNSET:
            field_dict["forceUserEnterInitialValue"] = force_user_enter_initial_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.combo_box_value import ComboBoxValue

        d = src_dict.copy()
        id = d.pop("id")

        title = d.pop("title")

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = ComboBoxValue.from_dict(items_item_data)

            items.append(items_item)

        save_to_settings = d.pop("saveToSettings", UNSET)

        mutable = d.pop("mutable", UNSET)

        force_user_enter_initial_value = d.pop("forceUserEnterInitialValue", UNSET)

        combo_box_meta_info = cls(
            id=id,
            title=title,
            items=items,
            save_to_settings=save_to_settings,
            mutable=mutable,
            force_user_enter_initial_value=force_user_enter_initial_value,
        )

        return combo_box_meta_info
