from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PullingInterval")


@attr.s(auto_attribs=True)
class PullingInterval:
    """Time intervals in milliseconds to pull data from the server.

    Attributes:
        quotes (Union[Unset, float]): Time interval in milliseconds to request quote and level 2 depth updates. Default:
            500.0. Example: 500.
        orders (Union[Unset, float]): Time interval in milliseconds to request orders. Default: 500.0. Example: 500.
        positions (Union[Unset, float]): Time interval in milliseconds to request positions. Default: 1000.0. Example:
            1000.
        account_manager (Union[Unset, float]): Time interval in milliseconds to update Account manager tables. Default:
            500.0. Example: 1000.
        balances (Union[Unset, float]): Time interval in milliseconds to request balances. Default: 1000.0. Example:
            1000.
    """

    quotes: Union[Unset, float] = 500.0
    orders: Union[Unset, float] = 500.0
    positions: Union[Unset, float] = 1000.0
    account_manager: Union[Unset, float] = 500.0
    balances: Union[Unset, float] = 1000.0

    def to_dict(self) -> Dict[str, Any]:
        quotes = self.quotes
        orders = self.orders
        positions = self.positions
        account_manager = self.account_manager
        balances = self.balances

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if quotes is not UNSET:
            field_dict["quotes"] = quotes
        if orders is not UNSET:
            field_dict["orders"] = orders
        if positions is not UNSET:
            field_dict["positions"] = positions
        if account_manager is not UNSET:
            field_dict["accountManager"] = account_manager
        if balances is not UNSET:
            field_dict["balances"] = balances

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        quotes = d.pop("quotes", UNSET)

        orders = d.pop("orders", UNSET)

        positions = d.pop("positions", UNSET)

        account_manager = d.pop("accountManager", UNSET)

        balances = d.pop("balances", UNSET)

        pulling_interval = cls(
            quotes=quotes,
            orders=orders,
            positions=positions,
            account_manager=account_manager,
            balances=balances,
        )

        return pulling_interval
