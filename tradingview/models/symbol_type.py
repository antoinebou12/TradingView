from enum import Enum


class SymbolType(str, Enum):
    BOND = "bond"
    CFD = "cfd"
    CRYPTO = "crypto"
    DR = "dr"
    FOREX = "forex"
    FUTURES = "futures"
    INDEX = "index"
    RIGHT = "right"
    STOCK = "stock"
    STRUCTURED = "structured"
    WARRANT = "warrant"

    def __str__(self) -> str:
        return str(self.value)
