from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar

import attr

from ..models.take_profit_percent_validation_rule_id import TakeProfitPercentValidationRuleId

if TYPE_CHECKING:
    from ..models.take_profit_percent_validation_rule_options import TakeProfitPercentValidationRuleOptions


T = TypeVar("T", bound="TakeProfitPercentValidationRule")


@attr.s(auto_attribs=True)
class TakeProfitPercentValidationRule:
    """Take Profit Percent Price Range Rule applied to field validation in the Order dialog.

    Attributes:
        id (TakeProfitPercentValidationRuleId):
        options (TakeProfitPercentValidationRuleOptions):
    """

    id: TakeProfitPercentValidationRuleId
    options: "TakeProfitPercentValidationRuleOptions"

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
        from ..models.take_profit_percent_validation_rule_options import TakeProfitPercentValidationRuleOptions

        d = src_dict.copy()
        id = TakeProfitPercentValidationRuleId(d.pop("id"))

        options = TakeProfitPercentValidationRuleOptions.from_dict(d.pop("options"))

        take_profit_percent_validation_rule = cls(
            id=id,
            options=options,
        )

        return take_profit_percent_validation_rule
