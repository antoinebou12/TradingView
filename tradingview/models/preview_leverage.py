from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PreviewLeverage")


@attr.s(auto_attribs=True)
class PreviewLeverage:
    """
    Example:
        {'infos': ['Borrowing limit at current leverage 0.3057 BTC or 0.00000 USDT', 'Required position margin at
            current leverage 0.3057 BTC'], 'warnings': ['Your leverage is comparatively high. Please be aware of risks'],
            'errors': ['Invalid leverage value']}

    Attributes:
        infos (Union[Unset, List[str]]): An array of information messages if any.
        warnings (Union[Unset, List[str]]): An array of warning messages if any.
        errors (Union[Unset, List[str]]): An array of error messages if any.
    """

    infos: Union[Unset, List[str]] = UNSET
    warnings: Union[Unset, List[str]] = UNSET
    errors: Union[Unset, List[str]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        infos: Union[Unset, List[str]] = UNSET
        if not isinstance(self.infos, Unset):
            infos = self.infos

        warnings: Union[Unset, List[str]] = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = self.warnings

        errors: Union[Unset, List[str]] = UNSET
        if not isinstance(self.errors, Unset):
            errors = self.errors

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if infos is not UNSET:
            field_dict["infos"] = infos
        if warnings is not UNSET:
            field_dict["warnings"] = warnings
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        infos = cast(List[str], d.pop("infos", UNSET))

        warnings = cast(List[str], d.pop("warnings", UNSET))

        errors = cast(List[str], d.pop("errors", UNSET))

        preview_leverage = cls(
            infos=infos,
            warnings=warnings,
            errors=errors,
        )

        return preview_leverage
