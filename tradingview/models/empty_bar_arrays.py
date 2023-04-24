from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="EmptyBarArrays")


@attr.s(auto_attribs=True)
class EmptyBarArrays:
    """Empty Bars data.

    Attributes:
        t (Union[Unset, List[float]]): Empty array
        o (Union[Unset, List[float]]): Empty array
        h (Union[Unset, List[float]]): Empty array
        l (Union[Unset, List[float]]): Empty array
        c (Union[Unset, List[float]]): Empty array
        v (Union[Unset, List[float]]): Empty array
    """

    t: Union[Unset, List[float]] = UNSET
    o: Union[Unset, List[float]] = UNSET
    h: Union[Unset, List[float]] = UNSET
    l: Union[Unset, List[float]] = UNSET
    c: Union[Unset, List[float]] = UNSET
    v: Union[Unset, List[float]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        t: Union[Unset, List[float]] = UNSET
        if not isinstance(self.t, Unset):
            t = self.t

        o: Union[Unset, List[float]] = UNSET
        if not isinstance(self.o, Unset):
            o = self.o

        h: Union[Unset, List[float]] = UNSET
        if not isinstance(self.h, Unset):
            h = self.h

        l: Union[Unset, List[float]] = UNSET
        if not isinstance(self.l, Unset):
            l = self.l

        c: Union[Unset, List[float]] = UNSET
        if not isinstance(self.c, Unset):
            c = self.c

        v: Union[Unset, List[float]] = UNSET
        if not isinstance(self.v, Unset):
            v = self.v

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if t is not UNSET:
            field_dict["t"] = t
        if o is not UNSET:
            field_dict["o"] = o
        if h is not UNSET:
            field_dict["h"] = h
        if l is not UNSET:
            field_dict["l"] = l
        if c is not UNSET:
            field_dict["c"] = c
        if v is not UNSET:
            field_dict["v"] = v

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        t = cast(List[float], d.pop("t", UNSET))

        o = cast(List[float], d.pop("o", UNSET))

        h = cast(List[float], d.pop("h", UNSET))

        l = cast(List[float], d.pop("l", UNSET))

        c = cast(List[float], d.pop("c", UNSET))

        v = cast(List[float], d.pop("v", UNSET))

        empty_bar_arrays = cls(
            t=t,
            o=o,
            h=h,
            l=l,
            c=c,
            v=v,
        )

        empty_bar_arrays.additional_properties = d
        return empty_bar_arrays

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
