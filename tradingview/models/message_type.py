from enum import Enum


class MessageType(str, Enum):
    ERROR = "error"
    INFORMATION = "information"
    WARNING = "warning"

    def __str__(self) -> str:
        return str(self.value)
