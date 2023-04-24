from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.order_preview_section_row import OrderPreviewSectionRow


T = TypeVar("T", bound="OrderPreviewSection")


@attr.s(auto_attribs=True)
class OrderPreviewSection:
    """Describes a single order preview section. Order preview can have multiple sections that are divided by separators
    and may have titles.

        Attributes:
            rows (List['OrderPreviewSectionRow']): Array of order preview items. Each item is a row of the section table.
            header (Union[Unset, str]): Optional title of the section.
    """

    rows: List["OrderPreviewSectionRow"]
    header: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        rows = []
        for rows_item_data in self.rows:
            rows_item = rows_item_data.to_dict()

            rows.append(rows_item)

        header = self.header

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "rows": rows,
            }
        )
        if header is not UNSET:
            field_dict["header"] = header

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.order_preview_section_row import OrderPreviewSectionRow

        d = src_dict.copy()
        rows = []
        _rows = d.pop("rows")
        for rows_item_data in _rows:
            rows_item = OrderPreviewSectionRow.from_dict(rows_item_data)

            rows.append(rows_item)

        header = d.pop("header", UNSET)

        order_preview_section = cls(
            rows=rows,
            header=header,
        )

        return order_preview_section
