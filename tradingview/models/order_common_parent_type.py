from enum import Enum


class OrderCommonParentType(str, Enum):
    ORDER = "order"
    POSITION = "position"

    def __str__(self) -> str:
        return str(self.value)
