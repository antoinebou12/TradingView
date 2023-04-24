from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="StreamingQuoteResponse")


@attr.s(auto_attribs=True)
class StreamingQuoteResponse:
    """
    Example:
        {'f': 'q', 'id': 'EURUSD', 't': 1547942400, 'ap': 1.47245, 'as': 100, 'bp': 1.47245, 'bs': 100}

    Attributes:
        f (str): Should always be `q`.
        id (str): Symbol.
        t (float): Unix time UTC.
        ap (float): Best ask price.
        as_ (float): Best ask size.
        bp (float): Best bid price.
        bs (float): Best bid size.
    """

    f: str
    id: str
    t: float
    ap: float
    as_: float
    bp: float
    bs: float
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        f = self.f
        id = self.id
        t = self.t
        ap = self.ap
        as_ = self.as_
        bp = self.bp
        bs = self.bs

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "f": f,
                "id": id,
                "t": t,
                "ap": ap,
                "as": as_,
                "bp": bp,
                "bs": bs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        f = d.pop("f")

        id = d.pop("id")

        t = d.pop("t")

        ap = d.pop("ap")

        as_ = d.pop("as")

        bp = d.pop("bp")

        bs = d.pop("bs")

        streaming_quote_response = cls(
            f=f,
            id=id,
            t=t,
            ap=ap,
            as_=as_,
            bp=bp,
            bs=bs,
        )

        streaming_quote_response.additional_properties = d
        return streaming_quote_response

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
