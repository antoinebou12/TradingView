from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.limit_percent_validation_rule import LimitPercentValidationRule
    from ..models.order_dialog_custom_fields import OrderDialogCustomFields
    from ..models.stop_loss_percent_validation_rule import StopLossPercentValidationRule
    from ..models.stop_percent_validation_rule import StopPercentValidationRule
    from ..models.take_profit_percent_validation_rule import TakeProfitPercentValidationRule


T = TypeVar("T", bound="InstrumentUi")


@attr.s(auto_attribs=True)
class InstrumentUi:
    """Order dialog configuration for the symbol. It will override configuration,
    specified in the [/accounts](#operation/getAccounts) endpoint.

        Attributes:
            order_dialog_custom_fields (Union[Unset, OrderDialogCustomFields]): Additional custom controls to be displayed
                in the Order dialog. At the moment, the only possible control types are combobox and checkbox. Data of the
                additional fields is filled from the [/orders](#operation/getOrders) endpoint.
            validation_rules (Union[Unset, List[Union['LimitPercentValidationRule', 'StopLossPercentValidationRule',
                'StopPercentValidationRule', 'TakeProfitPercentValidationRule']]]): Rules applied to field validation in the
                Order dialog.
                Please note: `stopPercent` and `limitPercent` validation rules are not applied
                if the `supportStopOrdersInBothDirections` or `supportStopLimitOrdersInBothDirections` flag is set to `true`.
                 Example: [{'id': 'slPercent', 'options': {'min': 10, 'max': 90}}, {'id': 'tpPercent', 'options': {'min': 10,
                'max': 90}}, {'id': 'limitPercent', 'options': {'min': 10, 'max': 20}}, {'id': 'stopPercent', 'options': {'min':
                10, 'max': 20}}].
    """

    order_dialog_custom_fields: Union[Unset, "OrderDialogCustomFields"] = UNSET
    validation_rules: Union[
        Unset,
        List[
            Union[
                "LimitPercentValidationRule",
                "StopLossPercentValidationRule",
                "StopPercentValidationRule",
                "TakeProfitPercentValidationRule",
            ]
        ],
    ] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from ..models.limit_percent_validation_rule import LimitPercentValidationRule
        from ..models.stop_loss_percent_validation_rule import StopLossPercentValidationRule
        from ..models.stop_percent_validation_rule import StopPercentValidationRule

        order_dialog_custom_fields: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.order_dialog_custom_fields, Unset):
            order_dialog_custom_fields = self.order_dialog_custom_fields.to_dict()

        validation_rules: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.validation_rules, Unset):
            validation_rules = []
            for validation_rules_item_data in self.validation_rules:
                validation_rules_item: Dict[str, Any]

                if isinstance(validation_rules_item_data, StopPercentValidationRule):
                    validation_rules_item = validation_rules_item_data.to_dict()

                elif isinstance(validation_rules_item_data, LimitPercentValidationRule):
                    validation_rules_item = validation_rules_item_data.to_dict()

                elif isinstance(validation_rules_item_data, StopLossPercentValidationRule):
                    validation_rules_item = validation_rules_item_data.to_dict()

                else:
                    validation_rules_item = validation_rules_item_data.to_dict()

                validation_rules.append(validation_rules_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if order_dialog_custom_fields is not UNSET:
            field_dict["orderDialogCustomFields"] = order_dialog_custom_fields
        if validation_rules is not UNSET:
            field_dict["validationRules"] = validation_rules

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.limit_percent_validation_rule import LimitPercentValidationRule
        from ..models.order_dialog_custom_fields import OrderDialogCustomFields
        from ..models.stop_loss_percent_validation_rule import StopLossPercentValidationRule
        from ..models.stop_percent_validation_rule import StopPercentValidationRule
        from ..models.take_profit_percent_validation_rule import TakeProfitPercentValidationRule

        d = src_dict.copy()
        _order_dialog_custom_fields = d.pop("orderDialogCustomFields", UNSET)
        order_dialog_custom_fields: Union[Unset, OrderDialogCustomFields]
        if isinstance(_order_dialog_custom_fields, Unset):
            order_dialog_custom_fields = UNSET
        else:
            order_dialog_custom_fields = OrderDialogCustomFields.from_dict(_order_dialog_custom_fields)

        validation_rules = []
        _validation_rules = d.pop("validationRules", UNSET)
        for validation_rules_item_data in _validation_rules or []:

            def _parse_validation_rules_item(
                data: object,
            ) -> Union[
                "LimitPercentValidationRule",
                "StopLossPercentValidationRule",
                "StopPercentValidationRule",
                "TakeProfitPercentValidationRule",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    validation_rules_item_type_0 = StopPercentValidationRule.from_dict(data)

                    return validation_rules_item_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    validation_rules_item_type_1 = LimitPercentValidationRule.from_dict(data)

                    return validation_rules_item_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    validation_rules_item_type_2 = StopLossPercentValidationRule.from_dict(data)

                    return validation_rules_item_type_2
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                validation_rules_item_type_3 = TakeProfitPercentValidationRule.from_dict(data)

                return validation_rules_item_type_3

            validation_rules_item = _parse_validation_rules_item(validation_rules_item_data)

            validation_rules.append(validation_rules_item)

        instrument_ui = cls(
            order_dialog_custom_fields=order_dialog_custom_fields,
            validation_rules=validation_rules,
        )

        return instrument_ui
