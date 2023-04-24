from enum import Enum


class OrderHistoryStatusStatus(str, Enum):
    CANCELLED = "cancelled"
    FILLED = "filled"
    REJECTED = "rejected"

    def __str__(self) -> str:
        return str(self.value)
