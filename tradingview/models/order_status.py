from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.order_status_status import OrderStatusStatus

T = TypeVar("T", bound="OrderStatus")


@attr.s(auto_attribs=True)
class OrderStatus:
    """
    Example:
        working

    Attributes:
        status (OrderStatusStatus): String constants to describe an order status.

            `Status`  | Description
            ----------|-------------
            placing   | order is not created on a broker's side yet
            inactive  | bracket order is created but waiting for a base order to be filled
            working   | order is created but not fully executed yet
            rejected  | order is rejected for some reason
            filled    | order is fully executed
            cancelled  | order is cancelled
    """

    status: OrderStatusStatus
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        status = OrderStatusStatus(d.pop("status"))

        order_status = cls(
            status=status,
        )

        order_status.additional_properties = d
        return order_status

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
