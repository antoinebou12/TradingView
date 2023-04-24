from typing import Any, Dict, List, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="Depth")


@attr.s(auto_attribs=True)
class Depth:
    """Depth of market for an instrument.

    Example:
        {'asks': [[45.1, 100], [48.4, 120]], 'bids': [[24.7, 80], [35.6, 30]]}

    Attributes:
        asks (List[List[float]]): Array of arrays with two numeric elements - price and volume. Must be sorted by
            `price` in ascending order.
        bids (List[List[float]]): Array of arrays with two numeric elements - price and volume. Must be sorted by
            `price` in ascending order.
    """

    asks: List[List[float]]
    bids: List[List[float]]

    def to_dict(self) -> Dict[str, Any]:
        asks = []
        for asks_item_data in self.asks:
            asks_item = asks_item_data

            asks.append(asks_item)

        bids = []
        for bids_item_data in self.bids:
            bids_item = bids_item_data

            bids.append(bids_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "asks": asks,
                "bids": bids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        asks = []
        _asks = d.pop("asks")
        for asks_item_data in _asks:
            asks_item = cast(List[float], asks_item_data)

            asks.append(asks_item)

        bids = []
        _bids = d.pop("bids")
        for bids_item_data in _bids:
            bids_item = cast(List[float], bids_item_data)

            bids.append(bids_item)

        depth = cls(
            asks=asks,
            bids=bids,
        )

        return depth
