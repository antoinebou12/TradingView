from enum import Enum


class StopPercentValidationRuleId(str, Enum):
    STOPPERCENT = "stopPercent"

    def __str__(self) -> str:
        return str(self.value)
