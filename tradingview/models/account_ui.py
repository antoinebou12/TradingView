from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_manager_column import AccountManagerColumn
    from ..models.account_manager_table import AccountManagerTable
    from ..models.account_summary_row_item import AccountSummaryRowItem
    from ..models.order_dialog_custom_fields import OrderDialogCustomFields


T = TypeVar("T", bound="AccountUi")


@attr.s(auto_attribs=True)
class AccountUi:
    """Account manager and Order dialog configuration for the account.
    The Account manager configuration will override configuration, specified in the
    [/config](#operation/getConfiguration) endpoint.

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
            order_dialog_custom_fields (Union[Unset, OrderDialogCustomFields]): Additional custom controls to be displayed
                in the Order dialog. At the moment, the only possible control types are combobox and checkbox. Data of the
                additional fields is filled from the [/orders](#operation/getOrders) endpoint.
    """

    account_summary_row: Union[Unset, List["AccountSummaryRowItem"]] = UNSET
    account_manager: Union[Unset, List["AccountManagerTable"]] = UNSET
    order_custom_fields: Union[Unset, List["AccountManagerColumn"]] = UNSET
    order_history_custom_fields: Union[Unset, List["AccountManagerColumn"]] = UNSET
    position_custom_fields: Union[Unset, List["AccountManagerColumn"]] = UNSET
    order_dialog_custom_fields: Union[Unset, "OrderDialogCustomFields"] = UNSET

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

        order_dialog_custom_fields: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.order_dialog_custom_fields, Unset):
            order_dialog_custom_fields = self.order_dialog_custom_fields.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if account_summary_row is not UNSET:
            field_dict["accountSummaryRow"] = account_summary_row
        if account_manager is not UNSET:
            field_dict["accountManager"] = account_manager
        if order_custom_fields is not UNSET:
            field_dict["orderCustomFields"] = order_custom_fields
        if order_history_custom_fields is not UNSET:
            field_dict["orderHistoryCustomFields"] = order_history_custom_fields
        if position_custom_fields is not UNSET:
            field_dict["positionCustomFields"] = position_custom_fields
        if order_dialog_custom_fields is not UNSET:
            field_dict["orderDialogCustomFields"] = order_dialog_custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.account_manager_column import AccountManagerColumn
        from ..models.account_manager_table import AccountManagerTable
        from ..models.account_summary_row_item import AccountSummaryRowItem
        from ..models.order_dialog_custom_fields import OrderDialogCustomFields

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

        _order_dialog_custom_fields = d.pop("orderDialogCustomFields", UNSET)
        order_dialog_custom_fields: Union[Unset, OrderDialogCustomFields]
        if isinstance(_order_dialog_custom_fields, Unset):
            order_dialog_custom_fields = UNSET
        else:
            order_dialog_custom_fields = OrderDialogCustomFields.from_dict(_order_dialog_custom_fields)

        account_ui = cls(
            account_summary_row=account_summary_row,
            account_manager=account_manager,
            order_custom_fields=order_custom_fields,
            order_history_custom_fields=order_history_custom_fields,
            position_custom_fields=position_custom_fields,
            order_dialog_custom_fields=order_dialog_custom_fields,
        )

        return account_ui
