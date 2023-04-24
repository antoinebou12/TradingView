from typing import Any, Dict, List, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="BarsArrays")


@attr.s(auto_attribs=True)
class BarsArrays:
    """Bars data.

    Attributes:
        t (List[float]): Bar time, Unix timestamp (UTC). Daily bars should only have the date
            part, time should be 0.
             Example: [1547942400, 1547942460, 1547942520].
        o (List[float]): Open price. Example: [3667, 3662.25, 3664.29].
        h (List[float]): High price. Example: [3667.24, 3664.47, 3664.3].
        l (List[float]): Low price. Example: [3661.55, 3661.9, 3662.43].
        c (List[float]): Close price. Example: [3662.25, 3663.13, 3664.01].
        v (List[float]): Volume. Example: [34.7336, 2.4413, 11.7075].
    """

    t: List[float]
    o: List[float]
    h: List[float]
    l: List[float]
    c: List[float]
    v: List[float]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        t = self.t

        o = self.o

        h = self.h

        l = self.l

        c = self.c

        v = self.v

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "t": t,
                "o": o,
                "h": h,
                "l": l,
                "c": c,
                "v": v,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        t = cast(List[float], d.pop("t"))

        o = cast(List[float], d.pop("o"))

        h = cast(List[float], d.pop("h"))

        l = cast(List[float], d.pop("l"))

        c = cast(List[float], d.pop("c"))

        v = cast(List[float], d.pop("v"))

        bars_arrays = cls(
            t=t,
            o=o,
            h=h,
            l=l,
            c=c,
            v=v,
        )

        bars_arrays.additional_properties = d
        return bars_arrays

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
