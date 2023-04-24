from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="StopLossPercentValidationRuleOptions")


@attr.s(auto_attribs=True)
class StopLossPercentValidationRuleOptions:
    """
    Attributes:
        min_ (float): Minimal value in percentage of the stop loss price relative to the parent order price. Example:
            10.
        max_ (float): Maximum value in percentage of the stop loss price relative to the parent order price. Example:
            90.
    """

    min_: float
    max_: float

    def to_dict(self) -> Dict[str, Any]:
        min_ = self.min_
        max_ = self.max_

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "min": min_,
                "max": max_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        min_ = d.pop("min")

        max_ = d.pop("max")

        stop_loss_percent_validation_rule_options = cls(
            min_=min_,
            max_=max_,
        )

        return stop_loss_percent_validation_rule_options
