from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.execution_side import ExecutionSide
from ..types import UNSET, Unset

T = TypeVar("T", bound="Execution")


@attr.s(auto_attribs=True)
class Execution:
    """
    Attributes:
        id (str): Unique identifier. Example: EX34567.
        instrument (str): Instrument id. Example: EURUSD.
        price (float): Execution price. Example: 1.23564.
        time (float): Execution time, Unix timestamp (UTC). Example: 1548406235.
        qty (float): Execution quantity. Example: 1.
        side (ExecutionSide): Side. Example: buy.
        order_id (str): Identifier of the order that has been filled. Example: 1263159154.
        is_close (bool): Whether the execution reduces the position.
        position_id (Union[Unset, str]): Identifier of the position that has been opened, modified or closed. Example:
            10098.
        commission (Union[Unset, float]): Commission charged for the fill. Example: 0.004.
    """

    id: str
    instrument: str
    price: float
    time: float
    qty: float
    side: ExecutionSide
    order_id: str
    is_close: bool
    position_id: Union[Unset, str] = UNSET
    commission: Union[Unset, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        instrument = self.instrument
        price = self.price
        time = self.time
        qty = self.qty
        side = self.side.value

        order_id = self.order_id
        is_close = self.is_close
        position_id = self.position_id
        commission = self.commission

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "instrument": instrument,
                "price": price,
                "time": time,
                "qty": qty,
                "side": side,
                "orderId": order_id,
                "isClose": is_close,
            }
        )
        if position_id is not UNSET:
            field_dict["positionId"] = position_id
        if commission is not UNSET:
            field_dict["commission"] = commission

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        instrument = d.pop("instrument")

        price = d.pop("price")

        time = d.pop("time")

        qty = d.pop("qty")

        side = ExecutionSide(d.pop("side"))

        order_id = d.pop("orderId")

        is_close = d.pop("isClose")

        position_id = d.pop("positionId", UNSET)

        commission = d.pop("commission", UNSET)

        execution = cls(
            id=id,
            instrument=instrument,
            price=price,
            time=time,
            qty=qty,
            side=side,
            order_id=order_id,
            is_close=is_close,
            position_id=position_id,
            commission=commission,
        )

        return execution
