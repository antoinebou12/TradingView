from typing import Any, Dict, Type, TypeVar

import attr

from ..models.message_type import MessageType

T = TypeVar("T", bound="Message")


@attr.s(auto_attribs=True)
class Message:
    """Informational message description, that will be displayed for the order or position in the Account manager. The
    message will be marked
    with a color, corresponding to a message type.
    Also, the message text will be displayed in the notification pop-up in case that order type is set to `rejected`.

        Attributes:
            text (str): Message text Example: You can add brackets to this
                position to protect it.
            type (MessageType): Message type Example: Information.
    """

    text: str
    type: MessageType

    def to_dict(self) -> Dict[str, Any]:
        text = self.text
        type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "text": text,
                "type": type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        text = d.pop("text")

        type = MessageType(d.pop("type"))

        message = cls(
            text=text,
            type=type,
        )

        return message
