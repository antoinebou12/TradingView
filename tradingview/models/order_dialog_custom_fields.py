from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.check_box_metainfo import CheckBoxMetainfo
    from ..models.combo_box_meta_info import ComboBoxMetaInfo


T = TypeVar("T", bound="OrderDialogCustomFields")


@attr.s(auto_attribs=True)
class OrderDialogCustomFields:
    """Additional custom controls to be displayed in the Order dialog. At the moment, the only possible control types are
    combobox and checkbox. Data of the additional fields is filled from the [/orders](#operation/getOrders) endpoint.

        Attributes:
            combo_box (Union[Unset, List['ComboBoxMetaInfo']]):
            checkbox (Union[Unset, List['CheckBoxMetainfo']]):
    """

    combo_box: Union[Unset, List["ComboBoxMetaInfo"]] = UNSET
    checkbox: Union[Unset, List["CheckBoxMetainfo"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        combo_box: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.combo_box, Unset):
            combo_box = []
            for combo_box_item_data in self.combo_box:
                combo_box_item = combo_box_item_data.to_dict()

                combo_box.append(combo_box_item)

        checkbox: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.checkbox, Unset):
            checkbox = []
            for checkbox_item_data in self.checkbox:
                checkbox_item = checkbox_item_data.to_dict()

                checkbox.append(checkbox_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if combo_box is not UNSET:
            field_dict["comboBox"] = combo_box
        if checkbox is not UNSET:
            field_dict["checkbox"] = checkbox

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.check_box_metainfo import CheckBoxMetainfo
        from ..models.combo_box_meta_info import ComboBoxMetaInfo

        d = src_dict.copy()
        combo_box = []
        _combo_box = d.pop("comboBox", UNSET)
        for combo_box_item_data in _combo_box or []:
            combo_box_item = ComboBoxMetaInfo.from_dict(combo_box_item_data)

            combo_box.append(combo_box_item)

        checkbox = []
        _checkbox = d.pop("checkbox", UNSET)
        for checkbox_item_data in _checkbox or []:
            checkbox_item = CheckBoxMetainfo.from_dict(checkbox_item_data)

            checkbox.append(checkbox_item)

        order_dialog_custom_fields = cls(
            combo_box=combo_box,
            checkbox=checkbox,
        )

        return order_dialog_custom_fields
