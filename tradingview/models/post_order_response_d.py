from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostOrderResponseD")


@attr.s(auto_attribs=True)
class PostOrderResponseD:
    """
    Attributes:
        transaction_id (Union[Unset, float]): An unique transaction identifier
        order_id (Union[Unset, str]): New order identifier. Example: 1.
    """

    transaction_id: Union[Unset, float] = UNSET
    order_id: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        transaction_id = self.transaction_id
        order_id = self.order_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if transaction_id is not UNSET:
            field_dict["transactionId"] = transaction_id
        if order_id is not UNSET:
            field_dict["orderId"] = order_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        transaction_id = d.pop("transactionId", UNSET)

        order_id = d.pop("orderId", UNSET)

        post_order_response_d = cls(
            transaction_id=transaction_id,
            order_id=order_id,
        )

        return post_order_response_d
