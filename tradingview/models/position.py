from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.position_side import PositionSide
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_fields_value_item import CustomFieldsValueItem
    from ..models.message import Message


T = TypeVar("T", bound="Position")


@attr.s(auto_attribs=True)
class Position:
    """
    Attributes:
        id (str): Unique identifier. Example: 1.
        instrument (str): Instrument name that is used on a broker's side. Example: EURUSD.
        qty (float): Quantity. Example: 1.
        side (PositionSide): Side. Example: buy.
        avg_price (float): Average price of position trades. Example: 1.1347091.
        unrealized_pl (Union[Unset, float]): Unrealized (open) profit/loss. Example: 19.4739.
        message (Union[Unset, Message]): Informational message description, that will be displayed for the order or
            position in the Account manager. The message will be marked
            with a color, corresponding to a message type.
            Also, the message text will be displayed in the notification pop-up in case that order type is set to
            `rejected`.
        custom_fields (Union[Unset, List['CustomFieldsValueItem']]): Localized position custom fields values data.
            Custom fields are configured in the [/config](#operation/getConfiguration) endpoint response.
    """

    id: str
    instrument: str
    qty: float
    side: PositionSide
    avg_price: float
    unrealized_pl: Union[Unset, float] = UNSET
    message: Union[Unset, "Message"] = UNSET
    custom_fields: Union[Unset, List["CustomFieldsValueItem"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        instrument = self.instrument
        qty = self.qty
        side = self.side.value

        avg_price = self.avg_price
        unrealized_pl = self.unrealized_pl
        message: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.message, Unset):
            message = self.message.to_dict()

        custom_fields: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = []
            for custom_fields_item_data in self.custom_fields:
                custom_fields_item = custom_fields_item_data.to_dict()

                custom_fields.append(custom_fields_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "instrument": instrument,
                "qty": qty,
                "side": side,
                "avgPrice": avg_price,
            }
        )
        if unrealized_pl is not UNSET:
            field_dict["unrealizedPl"] = unrealized_pl
        if message is not UNSET:
            field_dict["message"] = message
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.custom_fields_value_item import CustomFieldsValueItem
        from ..models.message import Message

        d = src_dict.copy()
        id = d.pop("id")

        instrument = d.pop("instrument")

        qty = d.pop("qty")

        side = PositionSide(d.pop("side"))

        avg_price = d.pop("avgPrice")

        unrealized_pl = d.pop("unrealizedPl", UNSET)

        _message = d.pop("message", UNSET)
        message: Union[Unset, Message]
        if isinstance(_message, Unset):
            message = UNSET
        else:
            message = Message.from_dict(_message)

        custom_fields = []
        _custom_fields = d.pop("customFields", UNSET)
        for custom_fields_item_data in _custom_fields or []:
            custom_fields_item = CustomFieldsValueItem.from_dict(custom_fields_item_data)

            custom_fields.append(custom_fields_item)

        position = cls(
            id=id,
            instrument=instrument,
            qty=qty,
            side=side,
            avg_price=avg_price,
            unrealized_pl=unrealized_pl,
            message=message,
            custom_fields=custom_fields,
        )

        return position
