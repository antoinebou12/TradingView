from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.track_latency_data_side import TrackLatencyDataSide
from ..models.track_latency_data_transaction_type import TrackLatencyDataTransactionType
from ..types import UNSET, Unset

T = TypeVar("T", bound="TrackLatencyData")


@attr.s(auto_attribs=True)
class TrackLatencyData:
    """
    Attributes:
        transaction_id (float): Request identifier for which the performance data is being sent.
        transaction_type (TrackLatencyDataTransactionType): Type of the transaction
        instrument (str): Instrument.
        side (TrackLatencyDataSide): Side.
        ask (float): Current ask price for the instrument that the user sees in the order panel. Example: 1.287367.
        bid (float): Current bid price for the instrument that the user sees in the order panel. Example: 1.28554.
        timestamp (float): Timestamp of the price quote user has seen on the UI. In milliseconds. Example: 1548406235.
        round_trip_duration (float): Request duration in milliseconds. Example: 183.
        qty (Union[Unset, float]): Placed or modified orders quantity. Not applied to Cancel order / modify position /
            close position requests.
    """

    transaction_id: float
    transaction_type: TrackLatencyDataTransactionType
    instrument: str
    side: TrackLatencyDataSide
    ask: float
    bid: float
    timestamp: float
    round_trip_duration: float
    qty: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        transaction_id = self.transaction_id
        transaction_type = self.transaction_type.value

        instrument = self.instrument
        side = self.side.value

        ask = self.ask
        bid = self.bid
        timestamp = self.timestamp
        round_trip_duration = self.round_trip_duration
        qty = self.qty

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "transactionId": transaction_id,
                "transactionType": transaction_type,
                "instrument": instrument,
                "side": side,
                "ask": ask,
                "bid": bid,
                "timestamp": timestamp,
                "roundTripDuration": round_trip_duration,
            }
        )
        if qty is not UNSET:
            field_dict["qty"] = qty

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        transaction_id = d.pop("transactionId")

        transaction_type = TrackLatencyDataTransactionType(d.pop("transactionType"))

        instrument = d.pop("instrument")

        side = TrackLatencyDataSide(d.pop("side"))

        ask = d.pop("ask")

        bid = d.pop("bid")

        timestamp = d.pop("timestamp")

        round_trip_duration = d.pop("roundTripDuration")

        qty = d.pop("qty", UNSET)

        track_latency_data = cls(
            transaction_id=transaction_id,
            transaction_type=transaction_type,
            instrument=instrument,
            side=side,
            ask=ask,
            bid=bid,
            timestamp=timestamp,
            round_trip_duration=round_trip_duration,
            qty=qty,
        )

        track_latency_data.additional_properties = d
        return track_latency_data

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
