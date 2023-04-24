from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.order_preview_section import OrderPreviewSection


T = TypeVar("T", bound="PreviewOrder")


@attr.s(auto_attribs=True)
class PreviewOrder:
    """
    Example:
        {'confirmId': 112358, 'sections': [{'header': 'Estimated', 'rows': [{'title': 'Estimated Commission', 'value':
            0.01}, {'title': 'Estimated Price', 'value': 4091}]}, {'rows': [{'title': 'Margin Value', 'value': 12100},
            {'title': 'Time In Force', 'value': 'DAY'}]}], 'warnings': ['Estimated money impact is for main order only.',
            'Order can be executed outside regular trading hours.'], 'errors': ['Failed to build order confirmation.']}

    Attributes:
        sections (List['OrderPreviewSection']):
        confirm_id (Union[Unset, str]): An optional identifier of an order. It is sent back to the server in the place
            order request. Example: 112358.
        warnings (Union[Unset, List[str]]): Optional array of text warnings.
        errors (Union[Unset, List[str]]): Optional array of text errors.
    """

    sections: List["OrderPreviewSection"]
    confirm_id: Union[Unset, str] = UNSET
    warnings: Union[Unset, List[str]] = UNSET
    errors: Union[Unset, List[str]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        sections = []
        for sections_item_data in self.sections:
            sections_item = sections_item_data.to_dict()

            sections.append(sections_item)

        confirm_id = self.confirm_id
        warnings: Union[Unset, List[str]] = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = self.warnings

        errors: Union[Unset, List[str]] = UNSET
        if not isinstance(self.errors, Unset):
            errors = self.errors

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "sections": sections,
            }
        )
        if confirm_id is not UNSET:
            field_dict["confirmId"] = confirm_id
        if warnings is not UNSET:
            field_dict["warnings"] = warnings
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.order_preview_section import OrderPreviewSection

        d = src_dict.copy()
        sections = []
        _sections = d.pop("sections")
        for sections_item_data in _sections:
            sections_item = OrderPreviewSection.from_dict(sections_item_data)

            sections.append(sections_item)

        confirm_id = d.pop("confirmId", UNSET)

        warnings = cast(List[str], d.pop("warnings", UNSET))

        errors = cast(List[str], d.pop("errors", UNSET))

        preview_order = cls(
            sections=sections,
            confirm_id=confirm_id,
            warnings=warnings,
            errors=errors,
        )

        return preview_order
