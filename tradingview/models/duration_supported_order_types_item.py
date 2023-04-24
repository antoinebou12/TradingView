from enum import Enum


class DurationSupportedOrderTypesItem(str, Enum):
    LIMIT = "limit"
    MARKET = "market"
    STOP = "stop"
    STOPLIMIT = "stoplimit"

    def __str__(self) -> str:
        return str(self.value)
