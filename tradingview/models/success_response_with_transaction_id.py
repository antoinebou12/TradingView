from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.success_response_s import SuccessResponseS
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.transaction_id import TransactionId


T = TypeVar("T", bound="SuccessResponseWithTransactionId")


@attr.s(auto_attribs=True)
class SuccessResponseWithTransactionId:
    """
    Attributes:
        s (SuccessResponseS): Status will always be `ok`. Example: ok.
        d (Union[Unset, TransactionId]): Transaction id is used in these endpoints as an identifier for latency tracking
            using [/trackLatency](#operation/trackLatency):
              [/placeOrder](#operation/placeOrder),
              [/modifyOrder](operation/#operation/modifyOrder),
              [/cancelOrder](#operation/cancelOrder),
              [/modifyPosition](#operation/modifyPosition),
              [/closePosition](#operation/closePosition)
            This field is used only if `supportTrackLatency` flag is set to true.
    """

    s: SuccessResponseS
    d: Union[Unset, "TransactionId"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        s = self.s.value

        d: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.d, Unset):
            d = self.d.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "s": s,
            }
        )
        if d is not UNSET:
            field_dict["d"] = d

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.transaction_id import TransactionId

        d = src_dict.copy()
        s = SuccessResponseS(d.pop("s"))

        _d = d.pop("d", UNSET)
        d: Union[Unset, TransactionId]
        if isinstance(_d, Unset):
            d = UNSET
        else:
            d = TransactionId.from_dict(_d)

        success_response_with_transaction_id = cls(
            s=s,
            d=d,
        )

        success_response_with_transaction_id.additional_properties = d
        return success_response_with_transaction_id

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
