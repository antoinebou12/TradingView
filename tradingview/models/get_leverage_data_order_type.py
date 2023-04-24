from enum import Enum


class GetLeverageDataOrderType(str, Enum):
    LIMIT = "limit"
    MARKET = "market"
    STOP = "stop"
    STOPLIMIT = "stoplimit"

    def __str__(self) -> str:
        return str(self.value)
