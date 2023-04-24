from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="StreamingAskBidTradeItem")


@attr.s(auto_attribs=True)
class StreamingAskBidTradeItem:
    """Ask or Bid.

    Attributes:
        id (str): Symbol Example: EURUSD.
        p (float): Price. Example: 1.47245.
        s (float): Size. Example: 100.
        t (float): Unix time UTC. Example: 1547942400.
    """

    id: str
    p: float
    s: float
    t: float
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        p = self.p
        s = self.s
        t = self.t

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "p": p,
                "s": s,
                "t": t,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        p = d.pop("p")

        s = d.pop("s")

        t = d.pop("t")

        streaming_ask_bid_trade_item = cls(
            id=id,
            p=p,
            s=s,
            t=t,
        )

        streaming_ask_bid_trade_item.additional_properties = d
        return streaming_ask_bid_trade_item

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
