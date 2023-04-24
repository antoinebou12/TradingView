from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SingleQuote")


@attr.s(auto_attribs=True)
class SingleQuote:
    """Price and restriction data for an instrument.

    Attributes:
        ask (float): Ask price. Example: 1.13836.
        bid (float): Bid price. Example: 1.13834.
        buy_pip_value (Union[Unset, float]): Value of 1 pip in the account currency, used for calculating risks and
            trade value in the Order dialog for buy orders. Example: 1.
        sell_pip_value (Union[Unset, float]): Value of 1 pip in the account currency, used for calculating risks and
            trade value in the Order dialog for sell orders. Example: 1.
        hard_to_borrow (Union[Unset, bool]): Specify if the instrument is hard to borrow.
        not_shortable (Union[Unset, bool]): Specify if the instrument is not shortable.
        halted (Union[Unset, bool]): Specify if the instrument is halted.
    """

    ask: float
    bid: float
    buy_pip_value: Union[Unset, float] = UNSET
    sell_pip_value: Union[Unset, float] = UNSET
    hard_to_borrow: Union[Unset, bool] = False
    not_shortable: Union[Unset, bool] = False
    halted: Union[Unset, bool] = False

    def to_dict(self) -> Dict[str, Any]:
        ask = self.ask
        bid = self.bid
        buy_pip_value = self.buy_pip_value
        sell_pip_value = self.sell_pip_value
        hard_to_borrow = self.hard_to_borrow
        not_shortable = self.not_shortable
        halted = self.halted

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "ask": ask,
                "bid": bid,
            }
        )
        if buy_pip_value is not UNSET:
            field_dict["buyPipValue"] = buy_pip_value
        if sell_pip_value is not UNSET:
            field_dict["sellPipValue"] = sell_pip_value
        if hard_to_borrow is not UNSET:
            field_dict["hardToBorrow"] = hard_to_borrow
        if not_shortable is not UNSET:
            field_dict["notShortable"] = not_shortable
        if halted is not UNSET:
            field_dict["halted"] = halted

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ask = d.pop("ask")

        bid = d.pop("bid")

        buy_pip_value = d.pop("buyPipValue", UNSET)

        sell_pip_value = d.pop("sellPipValue", UNSET)

        hard_to_borrow = d.pop("hardToBorrow", UNSET)

        not_shortable = d.pop("notShortable", UNSET)

        halted = d.pop("halted", UNSET)

        single_quote = cls(
            ask=ask,
            bid=bid,
            buy_pip_value=buy_pip_value,
            sell_pip_value=sell_pip_value,
            hard_to_borrow=hard_to_borrow,
            not_shortable=not_shortable,
            halted=halted,
        )

        return single_quote
