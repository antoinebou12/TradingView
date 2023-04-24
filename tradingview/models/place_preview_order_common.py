from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.place_preview_order_common_side import PlacePreviewOrderCommonSide
from ..models.place_preview_order_common_type import PlacePreviewOrderCommonType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PlacePreviewOrderCommon")


@attr.s(auto_attribs=True)
class PlacePreviewOrderCommon:
    """
    Attributes:
        instrument (Union[Unset, str]): Instrument. Example: EURUSD.
        side (Union[Unset, PlacePreviewOrderCommonSide]): Side. Example: buy.
        type (Union[Unset, PlacePreviewOrderCommonType]): Type. Example: limit.
    """

    instrument: Union[Unset, str] = UNSET
    side: Union[Unset, PlacePreviewOrderCommonSide] = UNSET
    type: Union[Unset, PlacePreviewOrderCommonType] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        instrument = self.instrument
        side: Union[Unset, str] = UNSET
        if not isinstance(self.side, Unset):
            side = self.side.value

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if instrument is not UNSET:
            field_dict["instrument"] = instrument
        if side is not UNSET:
            field_dict["side"] = side
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        instrument = d.pop("instrument", UNSET)

        _side = d.pop("side", UNSET)
        side: Union[Unset, PlacePreviewOrderCommonSide]
        if isinstance(_side, Unset):
            side = UNSET
        else:
            side = PlacePreviewOrderCommonSide(_side)

        _type = d.pop("type", UNSET)
        type: Union[Unset, PlacePreviewOrderCommonType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = PlacePreviewOrderCommonType(_type)

        place_preview_order_common = cls(
            instrument=instrument,
            side=side,
            type=type,
        )

        return place_preview_order_common
