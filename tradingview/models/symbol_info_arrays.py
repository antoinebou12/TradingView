from typing import Any, Dict, List, Optional, Type, TypeVar, Union, cast

import attr

from ..models.symbol_info_arrays_bar_source_item import SymbolInfoArraysBarSourceItem
from ..models.symbol_info_arrays_bar_transform_item import SymbolInfoArraysBarTransformItem
from ..models.symbol_info_arrays_timezone_item import SymbolInfoArraysTimezoneItem
from ..models.symbol_type import SymbolType
from ..types import UNSET, Unset

T = TypeVar("T", bound="SymbolInfoArrays")


@attr.s(auto_attribs=True)
class SymbolInfoArrays:
    """SymbolInfo is an object containing symbols metadata. Each value of this  object is an array of values which
    size is equal to symbols count or a single value that is applied to all symbols.
    You can use a single value for all fields except for `supported-resolutions` and `intraday-multipliers`.

        Attributes:
            symbol (List[str]): It is a symbol name which is a string that users see. Also, the symbol name is used for data
                requests
                if you are not using tickers. `symbol` must contain uppercase letters and can optionally contain numbers,
                dots, or underscores. Learn more about `symbol`
                in the [manual](https://www.tradingview.com/broker-api-docs/data/Symbol_info.html#symbol-naming-rules).
                 Example: ['VIXG2019', 'AAPLE', 'EURUSD'].
            description (List[str]): Description of a symbol. Will be displayed in the chart legend for this symbol.
                 Example: ['Volatility Index', 'Apple Inc', 'EUR/USD'].
            exchange_listed (List[str]): Short name of exchange where this symbol is listed. Example: ['CBOE', 'NASDAQ',
                'FOREX'].
            exchange_traded (List[str]): Short name of exchange where this symbol is traded. Example: ['CBOE', 'NASDAQ',
                'FOREX'].
            minmovement (List[float]): Minimal integer price change. Example: [1.0, 1.0, 1.0].
            pricescale (List[float]): Indicates how many decimal points the price has. For example, if the price has 2
                decimal points (ex., 300.01),
                then `pricescale` is `100`. If it has 3 decimals, then `pricescale` is `1000` etc. If the price doesn't have
                decimals,
                set `pricescale` to `1`.
                 Example: [100, 100, 100000].
            type (List[SymbolType]): Symbol type (forex/stock etc.). Example: ['futures', 'stock', 'forex'].
            timezone (List[SymbolInfoArraysTimezoneItem]): Timezone of the exchange for this symbol. We expect to get the
                name of the time zone in olsondb format.
                 Example: ['America/New_York', 'America/New_York', 'America/New_York'].
            session_regular (List[str]): Session time format is HHMM-HHMM. E.g., a session that starts at 9:30 am and ends
                at 4:00 pm should look like `0930-1600`.
                There is a special case for symbols traded 24/7 (e.g., Bitcoin and other cryptocurrencies): the session string
                should be `24x7`.
                To specify an overnight session set start time greater than end time (ie, `1700-0900`).
                Session time is expected to be in exchange time zone.
                 Example: ['0000-2359:23456', '0930-1600', '1700-1700'].
            currency (Optional[List[Optional[str]]]): Symbol currency, also named as counter currency. If a symbol is a
                currency pair, then the currency field has
                to contain the second currency of this pair. For example, `USD` is a currency for `EURUSD` ticker.
                Fiat currency must meet the ISO 4217 standard.
                 Example: ['USD', 'USD', 'USD'].
            base_currency (Union[Unset, None, List[Optional[str]]]): For currency pairs only. This field contains the first
                currency of the pair. For example, base currency for
                `EURUSD` ticker is `EUR`. Fiat currency must meet the ISO 4217 standard.
                 Example: [None, None, 'EUR'].
            minmovement2 (Union[Unset, List[float]]): This is a number for complex price formatting cases. The default value
                is `0`. Example: [0, 0, 0].
            fractional (Union[Unset, List[bool]]): Boolean showing whether this symbol wants to have complex price
                formatting (see `minmovement2`) or not. The default value is `false`.
                 Example: [False, False, False].
            root (Union[Unset, None, List[Optional[str]]]): Root of the features. It's required for futures symbol types
                only.
                Provide a null value for other symbol types.
                 Example: ['VIX', None, None].
            root_description (Union[Unset, None, List[Optional[str]]]): Short description of the futures root that will be
                displayed in the symbol search.
                It's required for futures only. Provide a null value for other symbol types.
                 Example: ['Volatility Index', None, None].
            has_intraday (Union[Unset, List[bool]]): Boolean value showing whether the symbol includes intraday (minutes)
                historical data. If it's `false` then all buttons for intraday resolutions
                will be disabled for this particular symbol. If it is set to `true`, all
                resolutions that are supplied directly by the datafeed must be provided
                in `intraday-multipliers` array. The default value is `true`.
                 Example: [True, True, True].
            has_no_volume (Union[Unset, List[bool]]): Boolean showing whether the symbol includes volume data or not. The
                default value is `false`. Example: [False, False, True].
            is_cfd (Union[Unset, List[bool]]): Boolean value showing whether the symbol is CFD. The base instrument type is
                set using the type field.
            ticker (Union[Unset, List[str]]): This is a unique identifier for this particular symbol in your symbology.
                If you specify this property then its value will be used for all data requests for this symbol.
                 Example: ['VIXG2019', 'AAPLE', 'EURUSD'].
            session_extended (Union[Unset, List[Optional[str]]]): An extended session, includes `session-premarket` and
                `session-postmarket`.
                The start time should be earlier or be equal to the start time of the `session-regular`
                and be equal to the start time of the `session-premarket` if it exists.
                 Example: ['0000-2359:23456', '0400-2000', '1700-1700'].
            session_premarket (Union[Unset, List[Optional[str]]]): An additional session before `session-regular`. The start
                time should be equal to the start time of the `session-extended`.
                The end time should be equal or less than the start time of the `session-regular`.
                 Example: [None, '0400-0930', None].
            session_postmarket (Union[Unset, List[Optional[str]]]): An additional session after the `session-regular`. The
                start time should be equal or greater
                than the end time of the `session-regular`. The end time should be equal to the end time of the `session-
                extended`.
                 Example: [None, '1600-2000', None].
            supported_resolutions (Union[Unset, List[List[str]]]): An array of resolutions which should be enabled in
                resolutions picker
                for this symbol. Each item of an array is expected to be a string.
                 Example: [['1', '3', '5', '15', '30', '60', '240', 'D', 'W'], ['1', '3', '5', '15', '30', '60', '240', 'D',
                'W'], ['1', '3', '5', '15', '30', '60', '240', 'D', 'W']].
            has_daily (Union[Unset, List[bool]]): The boolean value showing whether data feed has its own daily
                resolution bars or not. If `has-daily` = `false` then Charting Library
                will build the respective resolutions using 1-minute bars by itself.
                If not, then it will request those bars from the data feed.
                The default value is `true`.
                 Example: [True, True, True].
            intraday_multipliers (Union[Unset, List[List[str]]]): This is an array containing intraday resolutions (in
                minutes) that the data feed may provide.
                E.g., if the data feed supports resolutions such as `["1", "5", "15"]`, but has 1-minute bars
                for some symbols then you should set `intraday-multipliers` of this symbol to `[1]`. This will
                make Charting Library build 5 and 15-minute resolutions by itself.
                 Example: [['1', '3', '5', '15', '30', '60', '240'], ['1', '3', '5', '15', '30', '60', '240'], ['1', '3', '5',
                '15', '30', '60', '240']].
            has_weekly_and_monthly (Union[Unset, List[bool]]): The boolean value showing whether data feed has its own
                weekly
                and monthly resolution bars or not. If `has-weekly-and-monthly` = `false`
                then Charting Library will build the respective resolutions using daily
                bars by itself. If not, then it will request those bars from the data feed.
                The default value is `false`.
                 Example: [False, False, False].
            pointvalue (Union[Unset, List[float]]): The currency value of a single whole unit price change in the
                instrument's currency.
                If the value is not provided it is assumed to be `1`.
                 Example: [10, 1, 1e-05].
            expiration (Union[Unset, None, List[Optional[float]]]): Expiration of the futures in the following format:
                YYYYMMDD. Required for futures type symbols only.
                 Example: [20190213, None, None].
            bar_source (Union[Unset, List[SymbolInfoArraysBarSourceItem]]): The principle of building bars. The default
                value is `trade`. Example: ['trade', 'bid', 'ask'].
            bar_transform (Union[Unset, List[SymbolInfoArraysBarTransformItem]]): The principle of bar alignment. The
                default value is `none`. Example: ['openprev', 'openprev', 'none'].
            bar_fillgaps (Union[Unset, List[bool]]): Is used to create the zero-volume bars in the absence of any trades
                (i.e. bars with zero volume and equal OHLC values ).
                The default value is `false`.
                 Example: ['true', 'true', 'false'].
            isin (Union[Unset, List[str]]): International Securities Identification Number. It's needed for classic stock
                instruments only. Example: ['ZAE000190252', 'ZAE0001201977', 'ZAE000567432'].
            wkn (Union[Unset, List[str]]): German Securities Identification Code. It's needed for classic German stock
                instruments only. Example: ['A12ABB', 'A66RTT', 'A13DDE'].
    """

    symbol: List[str]
    description: List[str]
    exchange_listed: List[str]
    exchange_traded: List[str]
    minmovement: List[float]
    pricescale: List[float]
    type: List[SymbolType]
    timezone: List[SymbolInfoArraysTimezoneItem]
    session_regular: List[str]
    currency: Optional[List[Optional[str]]]
    base_currency: Union[Unset, None, List[Optional[str]]] = UNSET
    minmovement2: Union[Unset, List[float]] = UNSET
    fractional: Union[Unset, List[bool]] = UNSET
    root: Union[Unset, None, List[Optional[str]]] = UNSET
    root_description: Union[Unset, None, List[Optional[str]]] = UNSET
    has_intraday: Union[Unset, List[bool]] = UNSET
    has_no_volume: Union[Unset, List[bool]] = UNSET
    is_cfd: Union[Unset, List[bool]] = UNSET
    ticker: Union[Unset, List[str]] = UNSET
    session_extended: Union[Unset, List[Optional[str]]] = UNSET
    session_premarket: Union[Unset, List[Optional[str]]] = UNSET
    session_postmarket: Union[Unset, List[Optional[str]]] = UNSET
    supported_resolutions: Union[Unset, List[List[str]]] = UNSET
    has_daily: Union[Unset, List[bool]] = UNSET
    intraday_multipliers: Union[Unset, List[List[str]]] = UNSET
    has_weekly_and_monthly: Union[Unset, List[bool]] = UNSET
    pointvalue: Union[Unset, List[float]] = UNSET
    expiration: Union[Unset, None, List[Optional[float]]] = UNSET
    bar_source: Union[Unset, List[SymbolInfoArraysBarSourceItem]] = UNSET
    bar_transform: Union[Unset, List[SymbolInfoArraysBarTransformItem]] = UNSET
    bar_fillgaps: Union[Unset, List[bool]] = UNSET
    isin: Union[Unset, List[str]] = UNSET
    wkn: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        symbol = self.symbol

        description = self.description

        exchange_listed = self.exchange_listed

        exchange_traded = self.exchange_traded

        minmovement = self.minmovement

        pricescale = self.pricescale

        type = []
        for type_item_data in self.type:
            type_item = type_item_data.value

            type.append(type_item)

        timezone = []
        for timezone_item_data in self.timezone:
            timezone_item = timezone_item_data.value

            timezone.append(timezone_item)

        session_regular = self.session_regular

        if self.currency is None:
            currency = None
        else:
            currency = self.currency

        base_currency: Union[Unset, None, List[Optional[str]]] = UNSET
        if not isinstance(self.base_currency, Unset):
            if self.base_currency is None:
                base_currency = None
            else:
                base_currency = self.base_currency

        minmovement2: Union[Unset, List[float]] = UNSET
        if not isinstance(self.minmovement2, Unset):
            minmovement2 = self.minmovement2

        fractional: Union[Unset, List[bool]] = UNSET
        if not isinstance(self.fractional, Unset):
            fractional = self.fractional

        root: Union[Unset, None, List[Optional[str]]] = UNSET
        if not isinstance(self.root, Unset):
            if self.root is None:
                root = None
            else:
                root = self.root

        root_description: Union[Unset, None, List[Optional[str]]] = UNSET
        if not isinstance(self.root_description, Unset):
            if self.root_description is None:
                root_description = None
            else:
                root_description = self.root_description

        has_intraday: Union[Unset, List[bool]] = UNSET
        if not isinstance(self.has_intraday, Unset):
            has_intraday = self.has_intraday

        has_no_volume: Union[Unset, List[bool]] = UNSET
        if not isinstance(self.has_no_volume, Unset):
            has_no_volume = self.has_no_volume

        is_cfd: Union[Unset, List[bool]] = UNSET
        if not isinstance(self.is_cfd, Unset):
            is_cfd = self.is_cfd

        ticker: Union[Unset, List[str]] = UNSET
        if not isinstance(self.ticker, Unset):
            ticker = self.ticker

        session_extended: Union[Unset, List[Optional[str]]] = UNSET
        if not isinstance(self.session_extended, Unset):
            session_extended = self.session_extended

        session_premarket: Union[Unset, List[Optional[str]]] = UNSET
        if not isinstance(self.session_premarket, Unset):
            session_premarket = self.session_premarket

        session_postmarket: Union[Unset, List[Optional[str]]] = UNSET
        if not isinstance(self.session_postmarket, Unset):
            session_postmarket = self.session_postmarket

        supported_resolutions: Union[Unset, List[List[str]]] = UNSET
        if not isinstance(self.supported_resolutions, Unset):
            supported_resolutions = []
            for supported_resolutions_item_data in self.supported_resolutions:
                supported_resolutions_item = supported_resolutions_item_data

                supported_resolutions.append(supported_resolutions_item)

        has_daily: Union[Unset, List[bool]] = UNSET
        if not isinstance(self.has_daily, Unset):
            has_daily = self.has_daily

        intraday_multipliers: Union[Unset, List[List[str]]] = UNSET
        if not isinstance(self.intraday_multipliers, Unset):
            intraday_multipliers = []
            for intraday_multipliers_item_data in self.intraday_multipliers:
                intraday_multipliers_item = intraday_multipliers_item_data

                intraday_multipliers.append(intraday_multipliers_item)

        has_weekly_and_monthly: Union[Unset, List[bool]] = UNSET
        if not isinstance(self.has_weekly_and_monthly, Unset):
            has_weekly_and_monthly = self.has_weekly_and_monthly

        pointvalue: Union[Unset, List[float]] = UNSET
        if not isinstance(self.pointvalue, Unset):
            pointvalue = self.pointvalue

        expiration: Union[Unset, None, List[Optional[float]]] = UNSET
        if not isinstance(self.expiration, Unset):
            if self.expiration is None:
                expiration = None
            else:
                expiration = self.expiration

        bar_source: Union[Unset, List[str]] = UNSET
        if not isinstance(self.bar_source, Unset):
            bar_source = []
            for bar_source_item_data in self.bar_source:
                bar_source_item = bar_source_item_data.value

                bar_source.append(bar_source_item)

        bar_transform: Union[Unset, List[str]] = UNSET
        if not isinstance(self.bar_transform, Unset):
            bar_transform = []
            for bar_transform_item_data in self.bar_transform:
                bar_transform_item = bar_transform_item_data.value

                bar_transform.append(bar_transform_item)

        bar_fillgaps: Union[Unset, List[bool]] = UNSET
        if not isinstance(self.bar_fillgaps, Unset):
            bar_fillgaps = self.bar_fillgaps

        isin: Union[Unset, List[str]] = UNSET
        if not isinstance(self.isin, Unset):
            isin = self.isin

        wkn: Union[Unset, List[str]] = UNSET
        if not isinstance(self.wkn, Unset):
            wkn = self.wkn

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "symbol": symbol,
                "description": description,
                "exchange-listed": exchange_listed,
                "exchange-traded": exchange_traded,
                "minmovement": minmovement,
                "pricescale": pricescale,
                "type": type,
                "timezone": timezone,
                "session-regular": session_regular,
                "currency": currency,
            }
        )
        if base_currency is not UNSET:
            field_dict["base-currency"] = base_currency
        if minmovement2 is not UNSET:
            field_dict["minmovement2"] = minmovement2
        if fractional is not UNSET:
            field_dict["fractional"] = fractional
        if root is not UNSET:
            field_dict["root"] = root
        if root_description is not UNSET:
            field_dict["root-description"] = root_description
        if has_intraday is not UNSET:
            field_dict["has-intraday"] = has_intraday
        if has_no_volume is not UNSET:
            field_dict["has-no-volume"] = has_no_volume
        if is_cfd is not UNSET:
            field_dict["is-cfd"] = is_cfd
        if ticker is not UNSET:
            field_dict["ticker"] = ticker
        if session_extended is not UNSET:
            field_dict["session-extended"] = session_extended
        if session_premarket is not UNSET:
            field_dict["session-premarket"] = session_premarket
        if session_postmarket is not UNSET:
            field_dict["session-postmarket"] = session_postmarket
        if supported_resolutions is not UNSET:
            field_dict["supported-resolutions"] = supported_resolutions
        if has_daily is not UNSET:
            field_dict["has-daily"] = has_daily
        if intraday_multipliers is not UNSET:
            field_dict["intraday-multipliers"] = intraday_multipliers
        if has_weekly_and_monthly is not UNSET:
            field_dict["has-weekly-and-monthly"] = has_weekly_and_monthly
        if pointvalue is not UNSET:
            field_dict["pointvalue"] = pointvalue
        if expiration is not UNSET:
            field_dict["expiration"] = expiration
        if bar_source is not UNSET:
            field_dict["bar-source"] = bar_source
        if bar_transform is not UNSET:
            field_dict["bar-transform"] = bar_transform
        if bar_fillgaps is not UNSET:
            field_dict["bar-fillgaps"] = bar_fillgaps
        if isin is not UNSET:
            field_dict["isin"] = isin
        if wkn is not UNSET:
            field_dict["wkn"] = wkn

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        symbol = cast(List[str], d.pop("symbol"))

        description = cast(List[str], d.pop("description"))

        exchange_listed = cast(List[str], d.pop("exchange-listed"))

        exchange_traded = cast(List[str], d.pop("exchange-traded"))

        minmovement = cast(List[float], d.pop("minmovement"))

        pricescale = cast(List[float], d.pop("pricescale"))

        type = []
        _type = d.pop("type")
        for type_item_data in _type:
            type_item = SymbolType(type_item_data)

            type.append(type_item)

        timezone = []
        _timezone = d.pop("timezone")
        for timezone_item_data in _timezone:
            timezone_item = SymbolInfoArraysTimezoneItem(timezone_item_data)

            timezone.append(timezone_item)

        session_regular = cast(List[str], d.pop("session-regular"))

        currency = cast(List[Optional[str]], d.pop("currency"))

        base_currency = cast(List[Optional[str]], d.pop("base-currency", UNSET))

        minmovement2 = cast(List[float], d.pop("minmovement2", UNSET))

        fractional = cast(List[bool], d.pop("fractional", UNSET))

        root = cast(List[Optional[str]], d.pop("root", UNSET))

        root_description = cast(List[Optional[str]], d.pop("root-description", UNSET))

        has_intraday = cast(List[bool], d.pop("has-intraday", UNSET))

        has_no_volume = cast(List[bool], d.pop("has-no-volume", UNSET))

        is_cfd = cast(List[bool], d.pop("is-cfd", UNSET))

        ticker = cast(List[str], d.pop("ticker", UNSET))

        session_extended = cast(List[Optional[str]], d.pop("session-extended", UNSET))

        session_premarket = cast(List[Optional[str]], d.pop("session-premarket", UNSET))

        session_postmarket = cast(List[Optional[str]], d.pop("session-postmarket", UNSET))

        supported_resolutions = []
        _supported_resolutions = d.pop("supported-resolutions", UNSET)
        for supported_resolutions_item_data in _supported_resolutions or []:
            supported_resolutions_item = cast(List[str], supported_resolutions_item_data)

            supported_resolutions.append(supported_resolutions_item)

        has_daily = cast(List[bool], d.pop("has-daily", UNSET))

        intraday_multipliers = []
        _intraday_multipliers = d.pop("intraday-multipliers", UNSET)
        for intraday_multipliers_item_data in _intraday_multipliers or []:
            intraday_multipliers_item = cast(List[str], intraday_multipliers_item_data)

            intraday_multipliers.append(intraday_multipliers_item)

        has_weekly_and_monthly = cast(List[bool], d.pop("has-weekly-and-monthly", UNSET))

        pointvalue = cast(List[float], d.pop("pointvalue", UNSET))

        expiration = cast(List[Optional[float]], d.pop("expiration", UNSET))

        bar_source = []
        _bar_source = d.pop("bar-source", UNSET)
        for bar_source_item_data in _bar_source or []:
            bar_source_item = SymbolInfoArraysBarSourceItem(bar_source_item_data)

            bar_source.append(bar_source_item)

        bar_transform = []
        _bar_transform = d.pop("bar-transform", UNSET)
        for bar_transform_item_data in _bar_transform or []:
            bar_transform_item = SymbolInfoArraysBarTransformItem(bar_transform_item_data)

            bar_transform.append(bar_transform_item)

        bar_fillgaps = cast(List[bool], d.pop("bar-fillgaps", UNSET))

        isin = cast(List[str], d.pop("isin", UNSET))

        wkn = cast(List[str], d.pop("wkn", UNSET))

        symbol_info_arrays = cls(
            symbol=symbol,
            description=description,
            exchange_listed=exchange_listed,
            exchange_traded=exchange_traded,
            minmovement=minmovement,
            pricescale=pricescale,
            type=type,
            timezone=timezone,
            session_regular=session_regular,
            currency=currency,
            base_currency=base_currency,
            minmovement2=minmovement2,
            fractional=fractional,
            root=root,
            root_description=root_description,
            has_intraday=has_intraday,
            has_no_volume=has_no_volume,
            is_cfd=is_cfd,
            ticker=ticker,
            session_extended=session_extended,
            session_premarket=session_premarket,
            session_postmarket=session_postmarket,
            supported_resolutions=supported_resolutions,
            has_daily=has_daily,
            intraday_multipliers=intraday_multipliers,
            has_weekly_and_monthly=has_weekly_and_monthly,
            pointvalue=pointvalue,
            expiration=expiration,
            bar_source=bar_source,
            bar_transform=bar_transform,
            bar_fillgaps=bar_fillgaps,
            isin=isin,
            wkn=wkn,
        )

        symbol_info_arrays.additional_properties = d
        return symbol_info_arrays

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
