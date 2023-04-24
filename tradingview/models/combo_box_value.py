from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="ComboBoxValue")


@attr.s(auto_attribs=True)
class ComboBoxValue:
    """
    Attributes:
        text (str): Localized display name. Example: text.
        value (str): Value that is sent back to the server if the item is selected. Example: value.
    """

    text: str
    value: str

    def to_dict(self) -> Dict[str, Any]:
        text = self.text
        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "text": text,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        text = d.pop("text")

        value = d.pop("value")

        combo_box_value = cls(
            text=text,
            value=value,
        )

        return combo_box_value
