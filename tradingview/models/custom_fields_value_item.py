from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="CustomFieldsValueItem")


@attr.s(auto_attribs=True)
class CustomFieldsValueItem:
    """
    Attributes:
        id (str): Column identifier as defined in [/config](#operation/getConfiguration) response.
        value (str): Localized column value
    """

    id: str
    value: str

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        value = d.pop("value")

        custom_fields_value_item = cls(
            id=id,
            value=value,
        )

        return custom_fields_value_item
