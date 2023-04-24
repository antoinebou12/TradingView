from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CryptoBalance")


@attr.s(auto_attribs=True)
class CryptoBalance:
    """
    Attributes:
        symbol (str): Crypto currency symbol. Example: BTC.
        total (float): Total amount of the balance. Example: 1000.
        available (float): The balance available to the user. Example: 10.
        long_name (Union[Unset, str]): Crypto currency name. Example: Bitcoin.
        reserved (Union[Unset, float]): Reserved balance amount that can't be used at the moment for any reasons.
            Example: 90.
        btc_value (Union[Unset, float]): Total balance amount in BTC. Example: 1000.
        value (Union[Unset, float]): Balance amount in additional currency. Example: 100000.
        value_currency (Union[Unset, str]): Currency of the value. It can be either code, or symbol. Example: USD.
    """

    symbol: str
    total: float
    available: float
    long_name: Union[Unset, str] = UNSET
    reserved: Union[Unset, float] = UNSET
    btc_value: Union[Unset, float] = UNSET
    value: Union[Unset, float] = UNSET
    value_currency: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        symbol = self.symbol
        total = self.total
        available = self.available
        long_name = self.long_name
        reserved = self.reserved
        btc_value = self.btc_value
        value = self.value
        value_currency = self.value_currency

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "symbol": symbol,
                "total": total,
                "available": available,
            }
        )
        if long_name is not UNSET:
            field_dict["longName"] = long_name
        if reserved is not UNSET:
            field_dict["reserved"] = reserved
        if btc_value is not UNSET:
            field_dict["btcValue"] = btc_value
        if value is not UNSET:
            field_dict["value"] = value
        if value_currency is not UNSET:
            field_dict["valueCurrency"] = value_currency

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        symbol = d.pop("symbol")

        total = d.pop("total")

        available = d.pop("available")

        long_name = d.pop("longName", UNSET)

        reserved = d.pop("reserved", UNSET)

        btc_value = d.pop("btcValue", UNSET)

        value = d.pop("value", UNSET)

        value_currency = d.pop("valueCurrency", UNSET)

        crypto_balance = cls(
            symbol=symbol,
            total=total,
            available=available,
            long_name=long_name,
            reserved=reserved,
            btc_value=btc_value,
            value=value,
            value_currency=value_currency,
        )

        return crypto_balance
