from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar

import attr

from ..models.stop_percent_validation_rule_id import StopPercentValidationRuleId

if TYPE_CHECKING:
    from ..models.stop_percent_validation_rule_options import StopPercentValidationRuleOptions


T = TypeVar("T", bound="StopPercentValidationRule")


@attr.s(auto_attribs=True)
class StopPercentValidationRule:
    """Stop Percent Price Range Rule applied to the order price field validation in the Order dialog.

    Attributes:
        id (StopPercentValidationRuleId):
        options (StopPercentValidationRuleOptions):
    """

    id: StopPercentValidationRuleId
    options: "StopPercentValidationRuleOptions"

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
        from ..models.stop_percent_validation_rule_options import StopPercentValidationRuleOptions

        d = src_dict.copy()
        id = StopPercentValidationRuleId(d.pop("id"))

        options = StopPercentValidationRuleOptions.from_dict(d.pop("options"))

        stop_percent_validation_rule = cls(
            id=id,
            options=options,
        )

        return stop_percent_validation_rule
