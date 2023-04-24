from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

from ..models.ok_status import OkStatus

if TYPE_CHECKING:
    from ..models.order import Order


T = TypeVar("T", bound="OrdersResponse")


@attr.s(auto_attribs=True)
class OrdersResponse:
    """
    Attributes:
        s (OkStatus): Status will always be `ok`. Example: ok.
        d (List['Order']):  Example: [{'id': '1', 'instrument': 'EURUSD', 'qty': 100, 'side': 'buy', 'type': 'limit',
            'avgPrice': 0, 'limitPrice': 1.14344, 'duration': {'type': 'gtt', 'datetime': 1548406235}, 'status': 'working',
            'customFields': [{'id': 'commission', 'value': '1.25'}]}, {'id': '2', 'instrument': 'EURUSD', 'qty': 100,
            'side': 'sell', 'type': 'limit', 'filledQty': 50, 'avgPrice': 0, 'limitPrice': 1.15094, 'parentId': '1',
            'parentType': 'order', 'duration': {'type': 'gtt', 'datetime': 1548406235}, 'status': 'inactive',
            'customFields': [{'id': 'commission', 'value': ''}]}, {'id': '3', 'instrument': 'EURUSD', 'qty': 1000000,
            'side': 'sell', 'type': 'limit', 'filledQty': 0, 'avgPrice': 0, 'limitPrice': 1.15094, 'parentId': '1',
            'parentType': 'order', 'duration': {'type': 'gtt', 'datetime': 1548406235}, 'status': 'rejected', 'message':
            {'text': 'Insufficient Margin', 'type': 'error'}}].
    """

    s: OkStatus
    d: List["Order"]

    def to_dict(self) -> Dict[str, Any]:
        s = self.s.value

        d = []
        for d_item_data in self.d:
            d_item = d_item_data.to_dict()

            d.append(d_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "s": s,
                "d": d,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.order import Order

        d = src_dict.copy()
        s = OkStatus(d.pop("s"))

        d = []
        _d = d.pop("d")
        for d_item_data in _d:
            d_item = Order.from_dict(d_item_data)

            d.append(d_item)

        orders_response = cls(
            s=s,
            d=d,
        )

        return orders_response
