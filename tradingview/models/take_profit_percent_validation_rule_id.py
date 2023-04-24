from enum import Enum


class TakeProfitPercentValidationRuleId(str, Enum):
    TPPERCENT = "tpPercent"

    def __str__(self) -> str:
        return str(self.value)
