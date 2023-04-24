from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..models.symbol_type import SymbolType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.instrument_ui import InstrumentUi


T = TypeVar("T", bound="Instrument")


@attr.s(auto_attribs=True)
class Instrument:
    """
    Attributes:
        name (str): Broker instrument name. Example: EURUSD.
        description (str): Instrument description. Example: EUR/USD.
        pip_size (float): Size of 1 pip.
            It is equal to `minTick` for non-forex symbols. For forex pairs it equals either the `minTick`,
            or the `minTick` multiplied by `10`. For example, for IBM `minTick` it is 0.01, for EURCAD `minTick` it is
            0.00001.
             Example: 0.0001.
        pip_value (float): Value of 1 pip in the account currency.
             Example: 8.845e-05.
        min_tick (float): Minimum price movement. For example, for IBM `minTick` is 0.01, for EURCAD `minTick` is
            0.00001. Example: 1e-05.
        type (SymbolType): Symbol type (forex, stock, etc.). Example: forex.
        min_qty (Union[Unset, float]): Minimum quantity for trading. If `lotSize` is set, then the specified value must
            be in lots. Example: 1.
        max_qty (Union[Unset, float]): Maximum quantity for trading. If `lotSize` is set, then the specified value must
            be in lots. Example: 100000000.
        qty_step (Union[Unset, float]): Quantity step. If `lotSize` is set, then the specified value must be in lots.
            Example: 100.
        lot_size (Union[Unset, float]): Financial instrument units standardized number as set by the exchange or broker
            for buying or selling. Example: 10.
        base_currency (Union[Unset, str]): The first currency quoted in a currency pair. Used for crypto currencies
            only. Example: LTC.
        quote_currency (Union[Unset, str]): A quote currency is the second currency quoted in a currency pair. Used for
            crypto currencies only.
             Example: BTC.
        margin_rate (Union[Unset, float]): Margin rate for this instrument. Example: 0.05.
        has_quotes (Union[Unset, bool]): Indicates if your API provides quotes for this instrument. Assigning `false` to
            this field prevents `/quotes` request and makes ask/bid displayed from a TradingView server depending on users
            data subscriptions on TradingView. Use of this flag must be agreed with TradingView Default: True.
        units (Union[Unset, str]): Units of quantity or amount. Displayed instead of the `Units` label in the
            Quantity/Amount field
        variable_min_tick (Union[Unset, str]): Dynamic minimum price movement. It is used if the instrument's minimum
            price movement changes depending on the price range. For example, '0.01 10 0.02 25 0.05', where `minTick` is
            0.01 for a price less than 10, `minTick` is 0.02 for a price less than 25, `minTick` is 0.05 for a price more
            and equal than 25. Example: 0.01 10 0.02 25 0.05.
        ui (Union[Unset, InstrumentUi]): Order dialog configuration for the symbol. It will override configuration,
            specified in the [/accounts](#operation/getAccounts) endpoint.
    """

    name: str
    description: str
    pip_size: float
    pip_value: float
    min_tick: float
    type: SymbolType
    min_qty: Union[Unset, float] = UNSET
    max_qty: Union[Unset, float] = UNSET
    qty_step: Union[Unset, float] = UNSET
    lot_size: Union[Unset, float] = UNSET
    base_currency: Union[Unset, str] = UNSET
    quote_currency: Union[Unset, str] = UNSET
    margin_rate: Union[Unset, float] = UNSET
    has_quotes: Union[Unset, bool] = True
    units: Union[Unset, str] = UNSET
    variable_min_tick: Union[Unset, str] = UNSET
    ui: Union[Unset, "InstrumentUi"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        description = self.description
        pip_size = self.pip_size
        pip_value = self.pip_value
        min_tick = self.min_tick
        type = self.type.value

        min_qty = self.min_qty
        max_qty = self.max_qty
        qty_step = self.qty_step
        lot_size = self.lot_size
        base_currency = self.base_currency
        quote_currency = self.quote_currency
        margin_rate = self.margin_rate
        has_quotes = self.has_quotes
        units = self.units
        variable_min_tick = self.variable_min_tick
        ui: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ui, Unset):
            ui = self.ui.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
                "description": description,
                "pipSize": pip_size,
                "pipValue": pip_value,
                "minTick": min_tick,
                "type": type,
            }
        )
        if min_qty is not UNSET:
            field_dict["minQty"] = min_qty
        if max_qty is not UNSET:
            field_dict["maxQty"] = max_qty
        if qty_step is not UNSET:
            field_dict["qtyStep"] = qty_step
        if lot_size is not UNSET:
            field_dict["lotSize"] = lot_size
        if base_currency is not UNSET:
            field_dict["baseCurrency"] = base_currency
        if quote_currency is not UNSET:
            field_dict["quoteCurrency"] = quote_currency
        if margin_rate is not UNSET:
            field_dict["marginRate"] = margin_rate
        if has_quotes is not UNSET:
            field_dict["hasQuotes"] = has_quotes
        if units is not UNSET:
            field_dict["units"] = units
        if variable_min_tick is not UNSET:
            field_dict["variableMinTick"] = variable_min_tick
        if ui is not UNSET:
            field_dict["ui"] = ui

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.instrument_ui import InstrumentUi

        d = src_dict.copy()
        name = d.pop("name")

        description = d.pop("description")

        pip_size = d.pop("pipSize")

        pip_value = d.pop("pipValue")

        min_tick = d.pop("minTick")

        type = SymbolType(d.pop("type"))

        min_qty = d.pop("minQty", UNSET)

        max_qty = d.pop("maxQty", UNSET)

        qty_step = d.pop("qtyStep", UNSET)

        lot_size = d.pop("lotSize", UNSET)

        base_currency = d.pop("baseCurrency", UNSET)

        quote_currency = d.pop("quoteCurrency", UNSET)

        margin_rate = d.pop("marginRate", UNSET)

        has_quotes = d.pop("hasQuotes", UNSET)

        units = d.pop("units", UNSET)

        variable_min_tick = d.pop("variableMinTick", UNSET)

        _ui = d.pop("ui", UNSET)
        ui: Union[Unset, InstrumentUi]
        if isinstance(_ui, Unset):
            ui = UNSET
        else:
            ui = InstrumentUi.from_dict(_ui)

        instrument = cls(
            name=name,
            description=description,
            pip_size=pip_size,
            pip_value=pip_value,
            min_tick=min_tick,
            type=type,
            min_qty=min_qty,
            max_qty=max_qty,
            qty_step=qty_step,
            lot_size=lot_size,
            base_currency=base_currency,
            quote_currency=quote_currency,
            margin_rate=margin_rate,
            has_quotes=has_quotes,
            units=units,
            variable_min_tick=variable_min_tick,
            ui=ui,
        )

        return instrument
