from enum import Enum


class StopLossPercentValidationRuleId(str, Enum):
    SLPERCENT = "slPercent"

    def __str__(self) -> str:
        return str(self.value)
