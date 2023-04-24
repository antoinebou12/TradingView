from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar

import attr

from ..models.limit_percent_validation_rule_id import LimitPercentValidationRuleId

if TYPE_CHECKING:
    from ..models.limit_percent_validation_rule_options import LimitPercentValidationRuleOptions


T = TypeVar("T", bound="LimitPercentValidationRule")


@attr.s(auto_attribs=True)
class LimitPercentValidationRule:
    """Limit Percent Price Range Rule applied to the order price field validation in the Order dialog.

    Attributes:
        id (LimitPercentValidationRuleId):
        options (LimitPercentValidationRuleOptions):
    """

    id: LimitPercentValidationRuleId
    options: "LimitPercentValidationRuleOptions"

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
        from ..models.limit_percent_validation_rule_options import LimitPercentValidationRuleOptions

        d = src_dict.copy()
        id = LimitPercentValidationRuleId(d.pop("id"))

        options = LimitPercentValidationRuleOptions.from_dict(d.pop("options"))

        limit_percent_validation_rule = cls(
            id=id,
            options=options,
        )

        return limit_percent_validation_rule
