from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.success_response_s import SuccessResponseS
from ..types import UNSET, Unset

T = TypeVar("T", bound="HistoryEmptyBarResponse")


@attr.s(auto_attribs=True)
class HistoryEmptyBarResponse:
    """
    Attributes:
        s (SuccessResponseS): Status will always be `ok`. Example: ok.
        t (Union[Unset, List[float]]): Empty array
        o (Union[Unset, List[float]]): Empty array
        h (Union[Unset, List[float]]): Empty array
        l (Union[Unset, List[float]]): Empty array
        c (Union[Unset, List[float]]): Empty array
        v (Union[Unset, List[float]]): Empty array
    """

    s: SuccessResponseS
    t: Union[Unset, List[float]] = UNSET
    o: Union[Unset, List[float]] = UNSET
    h: Union[Unset, List[float]] = UNSET
    l: Union[Unset, List[float]] = UNSET
    c: Union[Unset, List[float]] = UNSET
    v: Union[Unset, List[float]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        s = self.s.value

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
        field_dict.update(
            {
                "s": s,
            }
        )
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
        s = SuccessResponseS(d.pop("s"))

        t = cast(List[float], d.pop("t", UNSET))

        o = cast(List[float], d.pop("o", UNSET))

        h = cast(List[float], d.pop("h", UNSET))

        l = cast(List[float], d.pop("l", UNSET))

        c = cast(List[float], d.pop("c", UNSET))

        v = cast(List[float], d.pop("v", UNSET))

        history_empty_bar_response = cls(
            s=s,
            t=t,
            o=o,
            h=h,
            l=l,
            c=c,
            v=v,
        )

        history_empty_bar_response.additional_properties = d
        return history_empty_bar_response

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
