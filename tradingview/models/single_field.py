from enum import Enum


class SingleField(str, Enum):
    BROKERSYMBOL = "brokerSymbol"

    def __str__(self) -> str:
        return str(self.value)
