from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_manager_column import AccountManagerColumn
    from ..models.account_manager_table import AccountManagerTable
    from ..models.account_summary_row_item import AccountSummaryRowItem
    from ..models.duration import Duration
    from ..models.pulling_interval import PullingInterval


T = TypeVar("T", bound="Config")


@attr.s(auto_attribs=True)
class Config:
    """
    Attributes:
        account_summary_row (Union[Unset, List['AccountSummaryRowItem']]): Localized Account Summary Row configuration.
            Account Summary Row is a panel at the top of the bottom widget with the key account indicators. The
            `supportCustomAccountSummaryRow` flag should be enabled in the account config, see the
            [/accounts](#operation/getAccounts) endpoint. Data of the Account Summary Row is filled using the
            [/state](/rest-api-spec/#operation/getState) endpoint. Example: [{'id': 'accountBalance', 'title': 'Account
            Balance'}, {'id': 'Equity', 'title': 'Realized P/L'}, {'id': 'Open Profit', 'title': 'Unrealized P/L'}].
        account_manager (Union[Unset, List['AccountManagerTable']]): Localized Account manager's tables configuration.
            Account manager is a
            page in the bottom widget. This page can have multiple tables. Data of
            the tables is filled using the [/state](/rest-api-spec/#operation/getState) endpoint.
             Example: [{'id': 'accountSummary', 'title': '', 'columns': [{'id': 'todayPL', 'title': "Today's P&L"}, {'id':
            'accountValue', 'title': 'Account Value'}, {'id': 'balance', 'title': 'Balance'}, {'id': 'totalMargin', 'title':
            'Margin'}, {'id': 'held', 'title': 'Held'}, {'id': 'buyingPower', 'title': 'Buying Power'}]}].
        durations (Union[Unset, List['Duration']]): Localized array of durations displayed in Order Ticket.
        order_custom_fields (Union[Unset, List['AccountManagerColumn']]): Additional order columns to be displayed in
            the orders table of the Account manager.
            The orders table has a default set of columns that can be extended using this configuration.
            The `supportOrderCustomFields` flag should be enabled in the [account
            configuration](https://www.tradingview.com/rest-api-spec/#operation/getAccounts).
            Data of the additional fields is filled from the
            [/orders](https://www.tradingview.com/rest-api-spec/#operation/getOrders) `customFields` value.
             Example: [{'id': 'commission', 'title': 'Commission', 'tooltip': 'Commission Fees', 'alignment': 'right'}].
        order_history_custom_fields (Union[Unset, List['AccountManagerColumn']]): Additional history columns to be
            displayed in the history table of the Account manager.
            The history table has a default set of columns that can be extended using this configuration.
            The `supportOrderHistoryCustomFields` and `supportOrdersHistory` flags should be enabled in the [account
            configuration](https://www.tradingview.com/rest-api-spec/#operation/getAccounts).
            Data of the additional fields is filled from the
            [/ordersHistory](/rest-api-spec/#operation/getOrdersHistory) `customFields` value.
             Example: [{'id': 'commission', 'title': 'Commission', 'tooltip': 'Commission Fees', 'alignment': 'right'}].
        position_custom_fields (Union[Unset, List['AccountManagerColumn']]): Additional position columns to be displayed
            in the positions table of the Account manager.
            The positions table has a default set of columns that can be extended using this configuration.
            The `supportPositionCustomFields` flag should be enabled in the [account
            configuration](https://www.tradingview.com/rest-api-spec/#operation/getAccounts).
            Data of the additional fields is filled from the
            [/positions](https://www.tradingview.com/rest-api-spec/#operation/getPositions) `customFields` value.
             Example: [{'id': 'exchangeFee', 'title': 'Exchange fee', 'tooltip': 'Exchange fee for the position',
            'alignment': 'right'}, {'id': 'routeFee', 'title': 'Route fee', 'tooltip': 'Route fee for the position',
            'alignment': 'right'}].
        pulling_interval (Union[Unset, PullingInterval]): Time intervals in milliseconds to pull data from the server.
    """

    account_summary_row: Union[Unset, List["AccountSummaryRowItem"]] = UNSET
    account_manager: Union[Unset, List["AccountManagerTable"]] = UNSET
    durations: Union[Unset, List["Duration"]] = UNSET
    order_custom_fields: Union[Unset, List["AccountManagerColumn"]] = UNSET
    order_history_custom_fields: Union[Unset, List["AccountManagerColumn"]] = UNSET
    position_custom_fields: Union[Unset, List["AccountManagerColumn"]] = UNSET
    pulling_interval: Union[Unset, "PullingInterval"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        account_summary_row: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.account_summary_row, Unset):
            account_summary_row = []
            for componentsschemas_account_summary_row_item_data in self.account_summary_row:
                componentsschemas_account_summary_row_item = componentsschemas_account_summary_row_item_data.to_dict()

                account_summary_row.append(componentsschemas_account_summary_row_item)

        account_manager: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.account_manager, Unset):
            account_manager = []
            for componentsschemas_account_manager_item_data in self.account_manager:
                componentsschemas_account_manager_item = componentsschemas_account_manager_item_data.to_dict()

                account_manager.append(componentsschemas_account_manager_item)

        durations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.durations, Unset):
            durations = []
            for componentsschemas_durations_item_data in self.durations:
                componentsschemas_durations_item = componentsschemas_durations_item_data.to_dict()

                durations.append(componentsschemas_durations_item)

        order_custom_fields: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.order_custom_fields, Unset):
            order_custom_fields = []
            for componentsschemas_order_custom_fields_item_data in self.order_custom_fields:
                componentsschemas_order_custom_fields_item = componentsschemas_order_custom_fields_item_data.to_dict()

                order_custom_fields.append(componentsschemas_order_custom_fields_item)

        order_history_custom_fields: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.order_history_custom_fields, Unset):
            order_history_custom_fields = []
            for componentsschemas_order_history_custom_fields_item_data in self.order_history_custom_fields:
                componentsschemas_order_history_custom_fields_item = (
                    componentsschemas_order_history_custom_fields_item_data.to_dict()
                )

                order_history_custom_fields.append(componentsschemas_order_history_custom_fields_item)

        position_custom_fields: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.position_custom_fields, Unset):
            position_custom_fields = []
            for componentsschemas_position_custom_fields_item_data in self.position_custom_fields:
                componentsschemas_position_custom_fields_item = (
                    componentsschemas_position_custom_fields_item_data.to_dict()
                )

                position_custom_fields.append(componentsschemas_position_custom_fields_item)

        pulling_interval: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pulling_interval, Unset):
            pulling_interval = self.pulling_interval.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if account_summary_row is not UNSET:
            field_dict["accountSummaryRow"] = account_summary_row
        if account_manager is not UNSET:
            field_dict["accountManager"] = account_manager
        if durations is not UNSET:
            field_dict["durations"] = durations
        if order_custom_fields is not UNSET:
            field_dict["orderCustomFields"] = order_custom_fields
        if order_history_custom_fields is not UNSET:
            field_dict["orderHistoryCustomFields"] = order_history_custom_fields
        if position_custom_fields is not UNSET:
            field_dict["positionCustomFields"] = position_custom_fields
        if pulling_interval is not UNSET:
            field_dict["pullingInterval"] = pulling_interval

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.account_manager_column import AccountManagerColumn
        from ..models.account_manager_table import AccountManagerTable
        from ..models.account_summary_row_item import AccountSummaryRowItem
        from ..models.duration import Duration
        from ..models.pulling_interval import PullingInterval

        d = src_dict.copy()
        account_summary_row = []
        _account_summary_row = d.pop("accountSummaryRow", UNSET)
        for componentsschemas_account_summary_row_item_data in _account_summary_row or []:
            componentsschemas_account_summary_row_item = AccountSummaryRowItem.from_dict(
                componentsschemas_account_summary_row_item_data
            )

            account_summary_row.append(componentsschemas_account_summary_row_item)

        account_manager = []
        _account_manager = d.pop("accountManager", UNSET)
        for componentsschemas_account_manager_item_data in _account_manager or []:
            componentsschemas_account_manager_item = AccountManagerTable.from_dict(
                componentsschemas_account_manager_item_data
            )

            account_manager.append(componentsschemas_account_manager_item)

        durations = []
        _durations = d.pop("durations", UNSET)
        for componentsschemas_durations_item_data in _durations or []:
            componentsschemas_durations_item = Duration.from_dict(componentsschemas_durations_item_data)

            durations.append(componentsschemas_durations_item)

        order_custom_fields = []
        _order_custom_fields = d.pop("orderCustomFields", UNSET)
        for componentsschemas_order_custom_fields_item_data in _order_custom_fields or []:
            componentsschemas_order_custom_fields_item = AccountManagerColumn.from_dict(
                componentsschemas_order_custom_fields_item_data
            )

            order_custom_fields.append(componentsschemas_order_custom_fields_item)

        order_history_custom_fields = []
        _order_history_custom_fields = d.pop("orderHistoryCustomFields", UNSET)
        for componentsschemas_order_history_custom_fields_item_data in _order_history_custom_fields or []:
            componentsschemas_order_history_custom_fields_item = AccountManagerColumn.from_dict(
                componentsschemas_order_history_custom_fields_item_data
            )

            order_history_custom_fields.append(componentsschemas_order_history_custom_fields_item)

        position_custom_fields = []
        _position_custom_fields = d.pop("positionCustomFields", UNSET)
        for componentsschemas_position_custom_fields_item_data in _position_custom_fields or []:
            componentsschemas_position_custom_fields_item = AccountManagerColumn.from_dict(
                componentsschemas_position_custom_fields_item_data
            )

            position_custom_fields.append(componentsschemas_position_custom_fields_item)

        _pulling_interval = d.pop("pullingInterval", UNSET)
        pulling_interval: Union[Unset, PullingInterval]
        if isinstance(_pulling_interval, Unset):
            pulling_interval = UNSET
        else:
            pulling_interval = PullingInterval.from_dict(_pulling_interval)

        config = cls(
            account_summary_row=account_summary_row,
            account_manager=account_manager,
            durations=durations,
            order_custom_fields=order_custom_fields,
            order_history_custom_fields=order_history_custom_fields,
            position_custom_fields=position_custom_fields,
            pulling_interval=pulling_interval,
        )

        return config
