from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="StreamingDailyBarResponse")


@attr.s(auto_attribs=True)
class StreamingDailyBarResponse:
    """
    Attributes:
        f (str): Should always be `d`. Example: d.
        id (str): Symbol Example: EURUSD.
        o (float): Open. Example: 3667.
        h (float): High. Example: 3667.24.
        l (float): Low. Example: 3661.55.
        c (float): Close. Example: 3662.25.
        v (float): Volume. Example: 34.
        t (float): Unix timestamp in seconds. Timestamp time should be always 00:00 at the start of the day. Example:
            1547931600.
    """

    f: str
    id: str
    o: float
    h: float
    l: float
    c: float
    v: float
    t: float
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        f = self.f
        id = self.id
        o = self.o
        h = self.h
        l = self.l
        c = self.c
        v = self.v
        t = self.t

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "f": f,
                "id": id,
                "o": o,
                "h": h,
                "l": l,
                "c": c,
                "v": v,
                "t": t,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        f = d.pop("f")

        id = d.pop("id")

        o = d.pop("o")

        h = d.pop("h")

        l = d.pop("l")

        c = d.pop("c")

        v = d.pop("v")

        t = d.pop("t")

        streaming_daily_bar_response = cls(
            f=f,
            id=id,
            o=o,
            h=h,
            l=l,
            c=c,
            v=v,
            t=t,
        )

        streaming_daily_bar_response.additional_properties = d
        return streaming_daily_bar_response

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
