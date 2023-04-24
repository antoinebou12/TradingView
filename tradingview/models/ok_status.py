from enum import Enum


class OkStatus(str, Enum):
    OK = "ok"

    def __str__(self) -> str:
        return str(self.value)
