from enum import Enum


class OrderStatusStatus(str, Enum):
    CANCELLED = "cancelled"
    FILLED = "filled"
    INACTIVE = "inactive"
    PLACING = "placing"
    REJECTED = "rejected"
    WORKING = "working"

    def __str__(self) -> str:
        return str(self.value)
