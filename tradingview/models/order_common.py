from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.order_common_parent_type import OrderCommonParentType
from ..models.order_common_side import OrderCommonSide
from ..models.order_common_type import OrderCommonType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_fields_value_item import CustomFieldsValueItem
    from ..models.message import Message
    from ..models.order_common_duration import OrderCommonDuration


T = TypeVar("T", bound="OrderCommon")


@attr.s(auto_attribs=True)
class OrderCommon:
    """
    Attributes:
        id (str): Unique identifier.
        instrument (str): Instrument name that is used on a broker's side.
        qty (float): Quantity.
        side (OrderCommonSide): Side.
        type (OrderCommonType): Type.
        filled_qty (Union[Unset, float]): Filled quantity.
        avg_price (Union[Unset, float]): Average price of order fills. It should be provided for filled / partly filled
            orders.
        limit_price (Union[Unset, float]): Limit Price for Limit or StopLimit orders only. You should not send this
            field for other order types.
        stop_price (Union[Unset, float]): Stop Price for Stop or StopLimit orders only. You should not send this field
            for other order types.
        trailing_stop_pips (Union[Unset, float]): Distance from the stop loss level to the current market price in pips
            for a position or to the order price if the parent is a stop or limit order.
        is_trailing_stop (Union[Unset, bool]): If this flag is set to `true`, then the stop order is a trailing stop.
        parent_id (Union[Unset, str]): Identifier of a parent order or a parent position (for position brackets)
            depending on `parentType`.
            Should be set only for bracket orders.
        parent_type (Union[Unset, OrderCommonParentType]): Type of order's parent. Should be set only for bracket
            orders.
        duration (Union[Unset, OrderCommonDuration]): Expiration type and Unix timestamp date/time.
        last_modified (Union[Unset, float]): Indicates the time when the order was last modified, Unix timestamp (UTC).
        custom_fields (Union[Unset, List['CustomFieldsValueItem']]): Localized order custom fields values data.
            Custom fields are configured in the [/config](#operation/getConfiguration) endpoint response.
            Custom `Order dialog` fields are to be sent along with the standard fields in the order object.
        message (Union[Unset, Message]): Informational message description, that will be displayed for the order or
            position in the Account manager. The message will be marked
            with a color, corresponding to a message type.
            Also, the message text will be displayed in the notification pop-up in case that order type is set to
            `rejected`.
    """

    id: str
    instrument: str
    qty: float
    side: OrderCommonSide
    type: OrderCommonType
    filled_qty: Union[Unset, float] = UNSET
    avg_price: Union[Unset, float] = UNSET
    limit_price: Union[Unset, float] = UNSET
    stop_price: Union[Unset, float] = UNSET
    trailing_stop_pips: Union[Unset, float] = UNSET
    is_trailing_stop: Union[Unset, bool] = UNSET
    parent_id: Union[Unset, str] = UNSET
    parent_type: Union[Unset, OrderCommonParentType] = UNSET
    duration: Union[Unset, "OrderCommonDuration"] = UNSET
    last_modified: Union[Unset, float] = UNSET
    custom_fields: Union[Unset, List["CustomFieldsValueItem"]] = UNSET
    message: Union[Unset, "Message"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        instrument = self.instrument
        qty = self.qty
        side = self.side.value

        type = self.type.value

        filled_qty = self.filled_qty
        avg_price = self.avg_price
        limit_price = self.limit_price
        stop_price = self.stop_price
        trailing_stop_pips = self.trailing_stop_pips
        is_trailing_stop = self.is_trailing_stop
        parent_id = self.parent_id
        parent_type: Union[Unset, str] = UNSET
        if not isinstance(self.parent_type, Unset):
            parent_type = self.parent_type.value

        duration: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.duration, Unset):
            duration = self.duration.to_dict()

        last_modified = self.last_modified
        custom_fields: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = []
            for custom_fields_item_data in self.custom_fields:
                custom_fields_item = custom_fields_item_data.to_dict()

                custom_fields.append(custom_fields_item)

        message: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.message, Unset):
            message = self.message.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "instrument": instrument,
                "qty": qty,
                "side": side,
                "type": type,
            }
        )
        if filled_qty is not UNSET:
            field_dict["filledQty"] = filled_qty
        if avg_price is not UNSET:
            field_dict["avgPrice"] = avg_price
        if limit_price is not UNSET:
            field_dict["limitPrice"] = limit_price
        if stop_price is not UNSET:
            field_dict["stopPrice"] = stop_price
        if trailing_stop_pips is not UNSET:
            field_dict["trailingStopPips"] = trailing_stop_pips
        if is_trailing_stop is not UNSET:
            field_dict["isTrailingStop"] = is_trailing_stop
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if parent_type is not UNSET:
            field_dict["parentType"] = parent_type
        if duration is not UNSET:
            field_dict["duration"] = duration
        if last_modified is not UNSET:
            field_dict["lastModified"] = last_modified
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.custom_fields_value_item import CustomFieldsValueItem
        from ..models.message import Message
        from ..models.order_common_duration import OrderCommonDuration

        d = src_dict.copy()
        id = d.pop("id")

        instrument = d.pop("instrument")

        qty = d.pop("qty")

        side = OrderCommonSide(d.pop("side"))

        type = OrderCommonType(d.pop("type"))

        filled_qty = d.pop("filledQty", UNSET)

        avg_price = d.pop("avgPrice", UNSET)

        limit_price = d.pop("limitPrice", UNSET)

        stop_price = d.pop("stopPrice", UNSET)

        trailing_stop_pips = d.pop("trailingStopPips", UNSET)

        is_trailing_stop = d.pop("isTrailingStop", UNSET)

        parent_id = d.pop("parentId", UNSET)

        _parent_type = d.pop("parentType", UNSET)
        parent_type: Union[Unset, OrderCommonParentType]
        if isinstance(_parent_type, Unset):
            parent_type = UNSET
        else:
            parent_type = OrderCommonParentType(_parent_type)

        _duration = d.pop("duration", UNSET)
        duration: Union[Unset, OrderCommonDuration]
        if isinstance(_duration, Unset):
            duration = UNSET
        else:
            duration = OrderCommonDuration.from_dict(_duration)

        last_modified = d.pop("lastModified", UNSET)

        custom_fields = []
        _custom_fields = d.pop("customFields", UNSET)
        for custom_fields_item_data in _custom_fields or []:
            custom_fields_item = CustomFieldsValueItem.from_dict(custom_fields_item_data)

            custom_fields.append(custom_fields_item)

        _message = d.pop("message", UNSET)
        message: Union[Unset, Message]
        if isinstance(_message, Unset):
            message = UNSET
        else:
            message = Message.from_dict(_message)

        order_common = cls(
            id=id,
            instrument=instrument,
            qty=qty,
            side=side,
            type=type,
            filled_qty=filled_qty,
            avg_price=avg_price,
            limit_price=limit_price,
            stop_price=stop_price,
            trailing_stop_pips=trailing_stop_pips,
            is_trailing_stop=is_trailing_stop,
            parent_id=parent_id,
            parent_type=parent_type,
            duration=duration,
            last_modified=last_modified,
            custom_fields=custom_fields,
            message=message,
        )

        order_common.additional_properties = d
        return order_common

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
