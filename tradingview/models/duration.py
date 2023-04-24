from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.duration_supported_order_types_item import DurationSupportedOrderTypesItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="Duration")


@attr.s(auto_attribs=True)
class Duration:
    """Single duration option.

    Attributes:
        id (str): Duration identifier. Example: GTT.
        title (str): Localized title. Example: Good Till Time.
        has_date_picker (Union[Unset, bool]): Display date control in Order Ticket for this duration type. Example:
            True.
        has_time_picker (Union[Unset, bool]): Display time control in Order Ticket for this duration type. Example:
            True.
        default (Union[Unset, bool]): Default duration. Only one duration object in the durations array can have a
            `true` value for this field. The default duration will be used when the user places orders in the silent mode
            and it will be the selected one when the user opens the Order dialog for the first time. Example: True.
        supported_order_types (Union[Unset, List[DurationSupportedOrderTypesItem]]): An optional array of order types to
            which the duration will be applied. Example: ['stop', 'stoplimit'].
    """

    id: str
    title: str
    has_date_picker: Union[Unset, bool] = False
    has_time_picker: Union[Unset, bool] = False
    default: Union[Unset, bool] = False
    supported_order_types: Union[Unset, List[DurationSupportedOrderTypesItem]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        title = self.title
        has_date_picker = self.has_date_picker
        has_time_picker = self.has_time_picker
        default = self.default
        supported_order_types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.supported_order_types, Unset):
            supported_order_types = []
            for supported_order_types_item_data in self.supported_order_types:
                supported_order_types_item = supported_order_types_item_data.value

                supported_order_types.append(supported_order_types_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "title": title,
            }
        )
        if has_date_picker is not UNSET:
            field_dict["hasDatePicker"] = has_date_picker
        if has_time_picker is not UNSET:
            field_dict["hasTimePicker"] = has_time_picker
        if default is not UNSET:
            field_dict["default"] = default
        if supported_order_types is not UNSET:
            field_dict["supportedOrderTypes"] = supported_order_types

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        title = d.pop("title")

        has_date_picker = d.pop("hasDatePicker", UNSET)

        has_time_picker = d.pop("hasTimePicker", UNSET)

        default = d.pop("default", UNSET)

        supported_order_types = []
        _supported_order_types = d.pop("supportedOrderTypes", UNSET)
        for supported_order_types_item_data in _supported_order_types or []:
            supported_order_types_item = DurationSupportedOrderTypesItem(supported_order_types_item_data)

            supported_order_types.append(supported_order_types_item)

        duration = cls(
            id=id,
            title=title,
            has_date_picker=has_date_picker,
            has_time_picker=has_time_picker,
            default=default,
            supported_order_types=supported_order_types,
        )

        return duration
