from enum import Enum


class SymbolInfoArraysBarSourceItem(str, Enum):
    ASK = "ask"
    BID = "bid"
    MID = "mid"
    TRADE = "trade"

    def __str__(self) -> str:
        return str(self.value)
