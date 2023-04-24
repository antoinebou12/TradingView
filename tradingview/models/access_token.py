from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="AccessToken")


@attr.s(auto_attribs=True)
class AccessToken:
    """Access token.

    Attributes:
        access_token (str): Access token acts as a session ID that the application uses for making
            requests. This token should be protected as if it were user
            credentials.
             Example: 7133au-cba5a72-842029c.
        expiration (float): The time when the token is expired is represented as the number of
            seconds since the Unix epoch (00:00:00 UTC on 1 January 1970).
             Example: 1548661401.
    """

    access_token: str
    expiration: float

    def to_dict(self) -> Dict[str, Any]:
        access_token = self.access_token
        expiration = self.expiration

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "access_token": access_token,
                "expiration": expiration,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        access_token = d.pop("access_token")

        expiration = d.pop("expiration")

        access_token = cls(
            access_token=access_token,
            expiration=expiration,
        )

        return access_token
