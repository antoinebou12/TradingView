from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AccountState")


@attr.s(auto_attribs=True)
class AccountState:
    """
    Example:
        {'balance': 41757.91, 'unrealizedPl': 1053.02, 'equity': 42857.56, 'amData': [[['90.22', '42857.56', '42857.56',
            '1099.65', '0.00', '41757.91']]], 'accountSummaryRowData': ['96883.89', '96837.12', '-46.77']}

    Attributes:
        balance (float): Account Balance.
        unrealized_pl (float): Unrealized profit/loss.
        equity (Union[Unset, float]): Equity. If this field is not specified, then it is calculated as balance +
            unrealizedPl.
        am_data (Union[Unset, List[List[List[str]]]]): Account manager data. Structure of Account manager is defined by
            the
            [/config](#operation/getConfiguration) endpoint. Each element of this array is a table.
        account_summary_row_data (Union[Unset, List[str]]): Account Summary Row data. Structure of Account Summary Row
            is defined by the
            [/config](#operation/getConfiguration) endpoint.
    """

    balance: float
    unrealized_pl: float
    equity: Union[Unset, float] = UNSET
    am_data: Union[Unset, List[List[List[str]]]] = UNSET
    account_summary_row_data: Union[Unset, List[str]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        balance = self.balance
        unrealized_pl = self.unrealized_pl
        equity = self.equity
        am_data: Union[Unset, List[List[List[str]]]] = UNSET
        if not isinstance(self.am_data, Unset):
            am_data = []
            for am_data_item_data in self.am_data:
                am_data_item = []
                for am_data_item_item_data in am_data_item_data:
                    am_data_item_item = am_data_item_item_data

                    am_data_item.append(am_data_item_item)

                am_data.append(am_data_item)

        account_summary_row_data: Union[Unset, List[str]] = UNSET
        if not isinstance(self.account_summary_row_data, Unset):
            account_summary_row_data = self.account_summary_row_data

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "balance": balance,
                "unrealizedPl": unrealized_pl,
            }
        )
        if equity is not UNSET:
            field_dict["equity"] = equity
        if am_data is not UNSET:
            field_dict["amData"] = am_data
        if account_summary_row_data is not UNSET:
            field_dict["accountSummaryRowData"] = account_summary_row_data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        balance = d.pop("balance")

        unrealized_pl = d.pop("unrealizedPl")

        equity = d.pop("equity", UNSET)

        am_data = []
        _am_data = d.pop("amData", UNSET)
        for am_data_item_data in _am_data or []:
            am_data_item = []
            _am_data_item = am_data_item_data
            for am_data_item_item_data in _am_data_item:
                am_data_item_item = cast(List[str], am_data_item_item_data)

                am_data_item.append(am_data_item_item)

            am_data.append(am_data_item)

        account_summary_row_data = cast(List[str], d.pop("accountSummaryRowData", UNSET))

        account_state = cls(
            balance=balance,
            unrealized_pl=unrealized_pl,
            equity=equity,
            am_data=am_data,
            account_summary_row_data=account_summary_row_data,
        )

        return account_state
