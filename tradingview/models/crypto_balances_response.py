from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

from ..models.ok_status import OkStatus

if TYPE_CHECKING:
    from ..models.crypto_balance import CryptoBalance


T = TypeVar("T", bound="CryptoBalancesResponse")


@attr.s(auto_attribs=True)
class CryptoBalancesResponse:
    """
    Attributes:
        s (OkStatus): Status will always be `ok`. Example: ok.
        d (List['CryptoBalance']):
    """

    s: OkStatus
    d: List["CryptoBalance"]

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
        from ..models.crypto_balance import CryptoBalance

        d = src_dict.copy()
        s = OkStatus(d.pop("s"))

        d = []
        _d = d.pop("d")
        for d_item_data in _d:
            d_item = CryptoBalance.from_dict(d_item_data)

            d.append(d_item)

        crypto_balances_response = cls(
            s=s,
            d=d,
        )

        return crypto_balances_response
