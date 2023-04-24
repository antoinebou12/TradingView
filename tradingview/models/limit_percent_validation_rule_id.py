from enum import Enum


class LimitPercentValidationRuleId(str, Enum):
    LIMITPERCENT = "limitPercent"

    def __str__(self) -> str:
        return str(self.value)
