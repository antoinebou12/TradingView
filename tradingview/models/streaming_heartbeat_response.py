from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="StreamingHeartbeatResponse")


@attr.s(auto_attribs=True)
class StreamingHeartbeatResponse:
    """
    Example:
        {'heartbeat': 1609255644}

    Attributes:
        heartbeat (Union[Unset, int]): Current Unix timestamp in seconds.
    """

    heartbeat: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        heartbeat = self.heartbeat

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if heartbeat is not UNSET:
            field_dict["heartbeat"] = heartbeat

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        heartbeat = d.pop("heartbeat", UNSET)

        streaming_heartbeat_response = cls(
            heartbeat=heartbeat,
        )

        streaming_heartbeat_response.additional_properties = d
        return streaming_heartbeat_response

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
