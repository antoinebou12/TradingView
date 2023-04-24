from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.order_history_status_status import OrderHistoryStatusStatus

T = TypeVar("T", bound="OrderHistoryStatus")


@attr.s(auto_attribs=True)
class OrderHistoryStatus:
    """
    Attributes:
        status (OrderHistoryStatusStatus): String constants to describe a final order status.

            `Status`  | Description
            ----------|-------------
            rejected  | order is rejected for some reason
            filled    | order is fully executed
            cancelled  | order is cancelled
    """

    status: OrderHistoryStatusStatus
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
        status = OrderHistoryStatusStatus(d.pop("status"))

        order_history_status = cls(
            status=status,
        )

        order_history_status.additional_properties = d
        return order_history_status

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
