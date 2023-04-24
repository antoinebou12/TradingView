from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar

import attr

from ..models.stop_loss_percent_validation_rule_id import StopLossPercentValidationRuleId

if TYPE_CHECKING:
    from ..models.stop_loss_percent_validation_rule_options import StopLossPercentValidationRuleOptions


T = TypeVar("T", bound="StopLossPercentValidationRule")


@attr.s(auto_attribs=True)
class StopLossPercentValidationRule:
    """Stop Loss Percent Price Range Rule applied to field validation in the Order dialog.

    Attributes:
        id (StopLossPercentValidationRuleId):
        options (StopLossPercentValidationRuleOptions):
    """

    id: StopLossPercentValidationRuleId
    options: "StopLossPercentValidationRuleOptions"

    def to_dict(self) -> Dict[str, Any]:
        id = self.id.value

        options = self.options.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "options": options,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.stop_loss_percent_validation_rule_options import StopLossPercentValidationRuleOptions

        d = src_dict.copy()
        id = StopLossPercentValidationRuleId(d.pop("id"))

        options = StopLossPercentValidationRuleOptions.from_dict(d.pop("options"))

        stop_loss_percent_validation_rule = cls(
            id=id,
            options=options,
        )

        return stop_loss_percent_validation_rule
