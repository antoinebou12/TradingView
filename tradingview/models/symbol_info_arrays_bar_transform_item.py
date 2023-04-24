from enum import Enum


class SymbolInfoArraysBarTransformItem(str, Enum):
    NONE = "none"
    OPENPREV = "openprev"
    PREVOPEN = "prevopen"

    def __str__(self) -> str:
        return str(self.value)
