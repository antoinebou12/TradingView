from enum import Enum


class TrackLatencyDataTransactionType(str, Enum):
    CANCEL_ORDER = "cancel_order"
    CLOSE_POSITION = "close_position"
    MODIFY_ORDER = "modify_order"
    MODIFY_POSITION = "modify_position"
    PLACE_ORDER = "place_order"

    def __str__(self) -> str:
        return str(self.value)
