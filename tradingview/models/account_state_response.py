from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar

import attr

from ..models.ok_status import OkStatus

if TYPE_CHECKING:
    from ..models.account_state import AccountState


T = TypeVar("T", bound="AccountStateResponse")


@attr.s(auto_attribs=True)
class AccountStateResponse:
    """
    Attributes:
        s (OkStatus): Status will always be `ok`. Example: ok.
        d (AccountState):  Example: {'balance': 41757.91, 'unrealizedPl': 1053.02, 'equity': 42857.56, 'amData':
            [[['90.22', '42857.56', '42857.56', '1099.65', '0.00', '41757.91']]], 'accountSummaryRowData': ['96883.89',
            '96837.12', '-46.77']}.
    """

    s: OkStatus
    d: "AccountState"

    def to_dict(self) -> Dict[str, Any]:
        s = self.s.value

        d = self.d.to_dict()

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
        from ..models.account_state import AccountState

        d = src_dict.copy()
        s = OkStatus(d.pop("s"))

        d = AccountState.from_dict(d.pop("d"))

        account_state_response = cls(
            s=s,
            d=d,
        )

        return account_state_response
