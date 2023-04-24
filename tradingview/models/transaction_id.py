from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="TransactionId")


@attr.s(auto_attribs=True)
class TransactionId:
    """Transaction id is used in these endpoints as an identifier for latency tracking using
    [/trackLatency](#operation/trackLatency):
      [/placeOrder](#operation/placeOrder),
      [/modifyOrder](operation/#operation/modifyOrder),
      [/cancelOrder](#operation/cancelOrder),
      [/modifyPosition](#operation/modifyPosition),
      [/closePosition](#operation/closePosition)
    This field is used only if `supportTrackLatency` flag is set to true.

        Attributes:
            transaction_id (Union[Unset, float]): An unique transaction identifier
    """

    transaction_id: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        transaction_id = self.transaction_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if transaction_id is not UNSET:
            field_dict["transactionId"] = transaction_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        transaction_id = d.pop("transactionId", UNSET)

        transaction_id = cls(
            transaction_id=transaction_id,
        )

        transaction_id.additional_properties = d
        return transaction_id

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
