from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="OrderPreviewSectionRow")


@attr.s(auto_attribs=True)
class OrderPreviewSectionRow:
    """Describes a single row of a section table of the order preview.

    Attributes:
        title (str): Description of the item.
        value (str): Formatted value of the item.
    """

    title: str
    value: str

    def to_dict(self) -> Dict[str, Any]:
        title = self.title
        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "title": title,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        title = d.pop("title")

        value = d.pop("value")

        order_preview_section_row = cls(
            title=title,
            value=value,
        )

        return order_preview_section_row
