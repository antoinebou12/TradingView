from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AccountFlags")


@attr.s(auto_attribs=True)
class AccountFlags:
    """
    Attributes:
        support_brackets (Union[Unset, bool]): Whether the integration supports brackets. Deprecated. Use
            supportOrderBrackets and supportPositionBrackets instead.
        support_order_brackets (Union[Unset, bool]): Whether the integration supports brackets (take profit and stop
            loss) for orders.
        support_market_brackets (Union[Unset, bool]): Whether the integration supports brackets for market orders.
            Default: True.
        support_position_brackets (Union[Unset, bool]): Whether the integration supports adding (or modifying) stop loss
            and take profit to positions.
        support_positions (Union[Unset, bool]): Whether the integration supports the Positions tab. If you set it to
            `false`, the `/positions` endpoint will not be used. Default: True.
        support_multiposition (Union[Unset, bool]): Whether the integration supports multiple positions at one
            instrument at the same time.
        support_close_position (Union[Unset, bool]): Whether the integration supports closing of a position without a
            need for a user to fill an order.
        support_partial_close_position (Union[Unset, bool]): Whether the integration supports partial closing of a
            position.
        support_reverse_position (Union[Unset, bool]): Whether the integration supports reversing of a position. If this
            flag is set to `false` the reverse position button will be hidden. Default: True.
        support_native_reverse_position (Union[Unset, bool]): Whether the integration natively supports reversing of a
            position. If it is natively supported then TradingView will send a request to the [Modify Position
            endpoint](#operation/modifyPosition) with the `side` parameter set. If it is not natively supported then a
            reversing order will be placed.
        support_market_orders (Union[Unset, bool]): Whether the integration supports market orders. Default: True.
        support_limit_orders (Union[Unset, bool]): Whether the integration supports limit orders. Default: True.
        support_stop_orders (Union[Unset, bool]): Whether the integration supports stop orders. Default: True.
        support_stop_limit_orders (Union[Unset, bool]): Whether the integration supports StopLimit orders.
        support_trailing_stop (Union[Unset, bool]): Whether the integration supports trailing stop orders.
        support_stop_orders_in_both_directions (Union[Unset, bool]): Whether Stop orders should behave like Market-if-
            touched in both directions. Enabling this flag removes the direction check from the order dialog.
        support_stop_limit_orders_in_both_directions (Union[Unset, bool]): Whether StopLimit orders should behave like
            Limit-if-touched in both directions. Enabling this flag removes the direction check from the order dialog.
        support_partial_order_execution (Union[Unset, bool]): Whether the integration supports partial order's
            execution. If this flag is set to `true`, then the 'Filled Qty' column will be displayed on the Orders tab.
        support_modify_order (Union[Unset, bool]): Whether the integration supports the modification of the existing
            order. Deprecated. Use supportModifyOrderPrice, supportEditAmount and supportModifyBrackets instead.
        support_modify_order_price (Union[Unset, bool]): Whether the integration supports order price editing. If you
            set it to `false`, the price control in the order ticket will be disabled when modifying an order. Default:
            True.
        support_edit_amount (Union[Unset, bool]): Whether the integration supports editing orders quantity. If you set
            it to `false`, the quantity control in the order ticket will be disabled when modifying an order. Default: True.
        support_modify_brackets (Union[Unset, bool]): Whether the integration supports order brackets editing. If you
            set it to `false`, the bracket's control in the order ticket will be disabled when modifying an order, and
            'Modify' button will be hidden on a chart and in the Account Manager. Default: True.
        support_modify_duration (Union[Unset, bool]): Whether the integration supports the modification of the duration
            of the existing order.
        support_crypto_exchange_order_ticket (Union[Unset, bool]): Whether the account is used to exchange(trade) crypto
            currencies. This flag switches the Order Ticket to the Crypto Exchange mode. It adds second currency quantity
            control, currency labels etc.
        support_digital_signature (Union[Unset, bool]): Whether the integration supports Digital signature input field
            in the Order Ticket.
        support_place_order_preview (Union[Unset, bool]): Whether the integration supports providing and displaying
            information (such as commission, margin, value, etc.) about the order being placed before submitting it.
        support_modify_order_preview (Union[Unset, bool]): Whether the integration supports providing and displaying
            information (such as commission, margin, value, etc.) about the order being modified before submitting it.
        show_quantity_instead_of_amount (Union[Unset, bool]): Renames Amount to Quantity in the Order Ticket.
        support_balances (Union[Unset, bool]): Whether the integration supports [/balances](/rest-api-
            spec/#operation/getBalances) request.
        support_orders_history (Union[Unset, bool]): Whether the integration supports [/ordersHistory](/rest-api-
            spec/#operation/getOrdersHistory) request.
        support_executions (Union[Unset, bool]): Whether the integration supports [/executions](/rest-api-
            spec/#operation/getExecutions) request.
        support_leverage (Union[Unset, bool]): Whether the integration supports leverage. If the flag is set to `true`,
            broker will calculate leverage using [/getLeverage](/rest-api-spec/#operation/getLeverage) endpoint.
        support_leverage_button (Union[Unset, bool]): Whether the integration supports leverage button. If the flag is
            set to `true`, a leverage input field will appear in the Order Widget. Click on the input field will activate a
            dedicated Leverage Dialog. Please note, that the flag `supportLeverage` should be enabled for the button to
            display. Default: True.
        support_dom (Union[Unset, bool]): Whether the integration supports DOM (Depth of market) widget to be available.
            Default: True.
        support_level_2_data (Union[Unset, bool]): Whether the integration supports Level 2 data. It is required to
            display DOM levels. You must implement [/depth](/rest-api-spec/#operation/getDepth) endpoint to display DOM.
        support_pl_update (Union[Unset, bool]): Whether the integration provide `unrealizedPl` for positions. Otherwise
            P&L will be calculated automatically based on a simple algorithm. Default: True.
        support_display_broker_name_in_symbol_search (Union[Unset, bool]): Whether the integration involves displaying
            broker instrument names in the Symbol Search. You may usually want to disable it if broker symbols are the same
            or you are using internal numbers as broker symbol names. Default: True.
        support_logout (Union[Unset, bool]): Whether the integration supports logout.
        support_custom_account_summary_row (Union[Unset, bool]): Whether the integration supports custom Account Summary
            Row.
        support_position_custom_fields (Union[Unset, bool]): Whether the integration supports custom fields for
            position.
        support_order_custom_fields (Union[Unset, bool]): Whether the integration supports custom fields for order.
        support_order_history_custom_fields (Union[Unset, bool]): Whether the integration supports custom fields for
            order history.
        support_track_latency (Union[Unset, bool]): Whether the integration supports latency tracking. See the
            [/trackLatency](#operation/trackLatency) endpoint.
    """

    support_brackets: Union[Unset, bool] = UNSET
    support_order_brackets: Union[Unset, bool] = False
    support_market_brackets: Union[Unset, bool] = True
    support_position_brackets: Union[Unset, bool] = False
    support_positions: Union[Unset, bool] = True
    support_multiposition: Union[Unset, bool] = False
    support_close_position: Union[Unset, bool] = False
    support_partial_close_position: Union[Unset, bool] = False
    support_reverse_position: Union[Unset, bool] = True
    support_native_reverse_position: Union[Unset, bool] = False
    support_market_orders: Union[Unset, bool] = True
    support_limit_orders: Union[Unset, bool] = True
    support_stop_orders: Union[Unset, bool] = True
    support_stop_limit_orders: Union[Unset, bool] = False
    support_trailing_stop: Union[Unset, bool] = False
    support_stop_orders_in_both_directions: Union[Unset, bool] = False
    support_stop_limit_orders_in_both_directions: Union[Unset, bool] = False
    support_partial_order_execution: Union[Unset, bool] = False
    support_modify_order: Union[Unset, bool] = UNSET
    support_modify_order_price: Union[Unset, bool] = True
    support_edit_amount: Union[Unset, bool] = True
    support_modify_brackets: Union[Unset, bool] = True
    support_modify_duration: Union[Unset, bool] = False
    support_crypto_exchange_order_ticket: Union[Unset, bool] = False
    support_digital_signature: Union[Unset, bool] = False
    support_place_order_preview: Union[Unset, bool] = False
    support_modify_order_preview: Union[Unset, bool] = False
    show_quantity_instead_of_amount: Union[Unset, bool] = False
    support_balances: Union[Unset, bool] = False
    support_orders_history: Union[Unset, bool] = False
    support_executions: Union[Unset, bool] = False
    support_leverage: Union[Unset, bool] = False
    support_leverage_button: Union[Unset, bool] = True
    support_dom: Union[Unset, bool] = True
    support_level_2_data: Union[Unset, bool] = False
    support_pl_update: Union[Unset, bool] = True
    support_display_broker_name_in_symbol_search: Union[Unset, bool] = True
    support_logout: Union[Unset, bool] = False
    support_custom_account_summary_row: Union[Unset, bool] = False
    support_position_custom_fields: Union[Unset, bool] = False
    support_order_custom_fields: Union[Unset, bool] = False
    support_order_history_custom_fields: Union[Unset, bool] = False
    support_track_latency: Union[Unset, bool] = False

    def to_dict(self) -> Dict[str, Any]:
        support_brackets = self.support_brackets
        support_order_brackets = self.support_order_brackets
        support_market_brackets = self.support_market_brackets
        support_position_brackets = self.support_position_brackets
        support_positions = self.support_positions
        support_multiposition = self.support_multiposition
        support_close_position = self.support_close_position
        support_partial_close_position = self.support_partial_close_position
        support_reverse_position = self.support_reverse_position
        support_native_reverse_position = self.support_native_reverse_position
        support_market_orders = self.support_market_orders
        support_limit_orders = self.support_limit_orders
        support_stop_orders = self.support_stop_orders
        support_stop_limit_orders = self.support_stop_limit_orders
        support_trailing_stop = self.support_trailing_stop
        support_stop_orders_in_both_directions = self.support_stop_orders_in_both_directions
        support_stop_limit_orders_in_both_directions = self.support_stop_limit_orders_in_both_directions
        support_partial_order_execution = self.support_partial_order_execution
        support_modify_order = self.support_modify_order
        support_modify_order_price = self.support_modify_order_price
        support_edit_amount = self.support_edit_amount
        support_modify_brackets = self.support_modify_brackets
        support_modify_duration = self.support_modify_duration
        support_crypto_exchange_order_ticket = self.support_crypto_exchange_order_ticket
        support_digital_signature = self.support_digital_signature
        support_place_order_preview = self.support_place_order_preview
        support_modify_order_preview = self.support_modify_order_preview
        show_quantity_instead_of_amount = self.show_quantity_instead_of_amount
        support_balances = self.support_balances
        support_orders_history = self.support_orders_history
        support_executions = self.support_executions
        support_leverage = self.support_leverage
        support_leverage_button = self.support_leverage_button
        support_dom = self.support_dom
        support_level_2_data = self.support_level_2_data
        support_pl_update = self.support_pl_update
        support_display_broker_name_in_symbol_search = self.support_display_broker_name_in_symbol_search
        support_logout = self.support_logout
        support_custom_account_summary_row = self.support_custom_account_summary_row
        support_position_custom_fields = self.support_position_custom_fields
        support_order_custom_fields = self.support_order_custom_fields
        support_order_history_custom_fields = self.support_order_history_custom_fields
        support_track_latency = self.support_track_latency

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if support_brackets is not UNSET:
            field_dict["supportBrackets"] = support_brackets
        if support_order_brackets is not UNSET:
            field_dict["supportOrderBrackets"] = support_order_brackets
        if support_market_brackets is not UNSET:
            field_dict["supportMarketBrackets"] = support_market_brackets
        if support_position_brackets is not UNSET:
            field_dict["supportPositionBrackets"] = support_position_brackets
        if support_positions is not UNSET:
            field_dict["supportPositions"] = support_positions
        if support_multiposition is not UNSET:
            field_dict["supportMultiposition"] = support_multiposition
        if support_close_position is not UNSET:
            field_dict["supportClosePosition"] = support_close_position
        if support_partial_close_position is not UNSET:
            field_dict["supportPartialClosePosition"] = support_partial_close_position
        if support_reverse_position is not UNSET:
            field_dict["supportReversePosition"] = support_reverse_position
        if support_native_reverse_position is not UNSET:
            field_dict["supportNativeReversePosition"] = support_native_reverse_position
        if support_market_orders is not UNSET:
            field_dict["supportMarketOrders"] = support_market_orders
        if support_limit_orders is not UNSET:
            field_dict["supportLimitOrders"] = support_limit_orders
        if support_stop_orders is not UNSET:
            field_dict["supportStopOrders"] = support_stop_orders
        if support_stop_limit_orders is not UNSET:
            field_dict["supportStopLimitOrders"] = support_stop_limit_orders
        if support_trailing_stop is not UNSET:
            field_dict["supportTrailingStop"] = support_trailing_stop
        if support_stop_orders_in_both_directions is not UNSET:
            field_dict["supportStopOrdersInBothDirections"] = support_stop_orders_in_both_directions
        if support_stop_limit_orders_in_both_directions is not UNSET:
            field_dict["supportStopLimitOrdersInBothDirections"] = support_stop_limit_orders_in_both_directions
        if support_partial_order_execution is not UNSET:
            field_dict["supportPartialOrderExecution"] = support_partial_order_execution
        if support_modify_order is not UNSET:
            field_dict["supportModifyOrder"] = support_modify_order
        if support_modify_order_price is not UNSET:
            field_dict["supportModifyOrderPrice"] = support_modify_order_price
        if support_edit_amount is not UNSET:
            field_dict["supportEditAmount"] = support_edit_amount
        if support_modify_brackets is not UNSET:
            field_dict["supportModifyBrackets"] = support_modify_brackets
        if support_modify_duration is not UNSET:
            field_dict["supportModifyDuration"] = support_modify_duration
        if support_crypto_exchange_order_ticket is not UNSET:
            field_dict["supportCryptoExchangeOrderTicket"] = support_crypto_exchange_order_ticket
        if support_digital_signature is not UNSET:
            field_dict["supportDigitalSignature"] = support_digital_signature
        if support_place_order_preview is not UNSET:
            field_dict["supportPlaceOrderPreview"] = support_place_order_preview
        if support_modify_order_preview is not UNSET:
            field_dict["supportModifyOrderPreview"] = support_modify_order_preview
        if show_quantity_instead_of_amount is not UNSET:
            field_dict["showQuantityInsteadOfAmount"] = show_quantity_instead_of_amount
        if support_balances is not UNSET:
            field_dict["supportBalances"] = support_balances
        if support_orders_history is not UNSET:
            field_dict["supportOrdersHistory"] = support_orders_history
        if support_executions is not UNSET:
            field_dict["supportExecutions"] = support_executions
        if support_leverage is not UNSET:
            field_dict["supportLeverage"] = support_leverage
        if support_leverage_button is not UNSET:
            field_dict["supportLeverageButton"] = support_leverage_button
        if support_dom is not UNSET:
            field_dict["supportDOM"] = support_dom
        if support_level_2_data is not UNSET:
            field_dict["supportLevel2Data"] = support_level_2_data
        if support_pl_update is not UNSET:
            field_dict["supportPLUpdate"] = support_pl_update
        if support_display_broker_name_in_symbol_search is not UNSET:
            field_dict["supportDisplayBrokerNameInSymbolSearch"] = support_display_broker_name_in_symbol_search
        if support_logout is not UNSET:
            field_dict["supportLogout"] = support_logout
        if support_custom_account_summary_row is not UNSET:
            field_dict["supportCustomAccountSummaryRow"] = support_custom_account_summary_row
        if support_position_custom_fields is not UNSET:
            field_dict["supportPositionCustomFields"] = support_position_custom_fields
        if support_order_custom_fields is not UNSET:
            field_dict["supportOrderCustomFields"] = support_order_custom_fields
        if support_order_history_custom_fields is not UNSET:
            field_dict["supportOrderHistoryCustomFields"] = support_order_history_custom_fields
        if support_track_latency is not UNSET:
            field_dict["supportTrackLatency"] = support_track_latency

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        support_brackets = d.pop("supportBrackets", UNSET)

        support_order_brackets = d.pop("supportOrderBrackets", UNSET)

        support_market_brackets = d.pop("supportMarketBrackets", UNSET)

        support_position_brackets = d.pop("supportPositionBrackets", UNSET)

        support_positions = d.pop("supportPositions", UNSET)

        support_multiposition = d.pop("supportMultiposition", UNSET)

        support_close_position = d.pop("supportClosePosition", UNSET)

        support_partial_close_position = d.pop("supportPartialClosePosition", UNSET)

        support_reverse_position = d.pop("supportReversePosition", UNSET)

        support_native_reverse_position = d.pop("supportNativeReversePosition", UNSET)

        support_market_orders = d.pop("supportMarketOrders", UNSET)

        support_limit_orders = d.pop("supportLimitOrders", UNSET)

        support_stop_orders = d.pop("supportStopOrders", UNSET)

        support_stop_limit_orders = d.pop("supportStopLimitOrders", UNSET)

        support_trailing_stop = d.pop("supportTrailingStop", UNSET)

        support_stop_orders_in_both_directions = d.pop("supportStopOrdersInBothDirections", UNSET)

        support_stop_limit_orders_in_both_directions = d.pop("supportStopLimitOrdersInBothDirections", UNSET)

        support_partial_order_execution = d.pop("supportPartialOrderExecution", UNSET)

        support_modify_order = d.pop("supportModifyOrder", UNSET)

        support_modify_order_price = d.pop("supportModifyOrderPrice", UNSET)

        support_edit_amount = d.pop("supportEditAmount", UNSET)

        support_modify_brackets = d.pop("supportModifyBrackets", UNSET)

        support_modify_duration = d.pop("supportModifyDuration", UNSET)

        support_crypto_exchange_order_ticket = d.pop("supportCryptoExchangeOrderTicket", UNSET)

        support_digital_signature = d.pop("supportDigitalSignature", UNSET)

        support_place_order_preview = d.pop("supportPlaceOrderPreview", UNSET)

        support_modify_order_preview = d.pop("supportModifyOrderPreview", UNSET)

        show_quantity_instead_of_amount = d.pop("showQuantityInsteadOfAmount", UNSET)

        support_balances = d.pop("supportBalances", UNSET)

        support_orders_history = d.pop("supportOrdersHistory", UNSET)

        support_executions = d.pop("supportExecutions", UNSET)

        support_leverage = d.pop("supportLeverage", UNSET)

        support_leverage_button = d.pop("supportLeverageButton", UNSET)

        support_dom = d.pop("supportDOM", UNSET)

        support_level_2_data = d.pop("supportLevel2Data", UNSET)

        support_pl_update = d.pop("supportPLUpdate", UNSET)

        support_display_broker_name_in_symbol_search = d.pop("supportDisplayBrokerNameInSymbolSearch", UNSET)

        support_logout = d.pop("supportLogout", UNSET)

        support_custom_account_summary_row = d.pop("supportCustomAccountSummaryRow", UNSET)

        support_position_custom_fields = d.pop("supportPositionCustomFields", UNSET)

        support_order_custom_fields = d.pop("supportOrderCustomFields", UNSET)

        support_order_history_custom_fields = d.pop("supportOrderHistoryCustomFields", UNSET)

        support_track_latency = d.pop("supportTrackLatency", UNSET)

        account_flags = cls(
            support_brackets=support_brackets,
            support_order_brackets=support_order_brackets,
            support_market_brackets=support_market_brackets,
            support_position_brackets=support_position_brackets,
            support_positions=support_positions,
            support_multiposition=support_multiposition,
            support_close_position=support_close_position,
            support_partial_close_position=support_partial_close_position,
            support_reverse_position=support_reverse_position,
            support_native_reverse_position=support_native_reverse_position,
            support_market_orders=support_market_orders,
            support_limit_orders=support_limit_orders,
            support_stop_orders=support_stop_orders,
            support_stop_limit_orders=support_stop_limit_orders,
            support_trailing_stop=support_trailing_stop,
            support_stop_orders_in_both_directions=support_stop_orders_in_both_directions,
            support_stop_limit_orders_in_both_directions=support_stop_limit_orders_in_both_directions,
            support_partial_order_execution=support_partial_order_execution,
            support_modify_order=support_modify_order,
            support_modify_order_price=support_modify_order_price,
            support_edit_amount=support_edit_amount,
            support_modify_brackets=support_modify_brackets,
            support_modify_duration=support_modify_duration,
            support_crypto_exchange_order_ticket=support_crypto_exchange_order_ticket,
            support_digital_signature=support_digital_signature,
            support_place_order_preview=support_place_order_preview,
            support_modify_order_preview=support_modify_order_preview,
            show_quantity_instead_of_amount=show_quantity_instead_of_amount,
            support_balances=support_balances,
            support_orders_history=support_orders_history,
            support_executions=support_executions,
            support_leverage=support_leverage,
            support_leverage_button=support_leverage_button,
            support_dom=support_dom,
            support_level_2_data=support_level_2_data,
            support_pl_update=support_pl_update,
            support_display_broker_name_in_symbol_search=support_display_broker_name_in_symbol_search,
            support_logout=support_logout,
            support_custom_account_summary_row=support_custom_account_summary_row,
            support_position_custom_fields=support_position_custom_fields,
            support_order_custom_fields=support_order_custom_fields,
            support_order_history_custom_fields=support_order_history_custom_fields,
            support_track_latency=support_track_latency,
        )

        return account_flags
