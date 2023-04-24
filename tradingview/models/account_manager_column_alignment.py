from enum import Enum


class AccountManagerColumnAlignment(str, Enum):
    LEFT = "left"
    RIGHT = "right"

    def __str__(self) -> str:
        return str(self.value)
