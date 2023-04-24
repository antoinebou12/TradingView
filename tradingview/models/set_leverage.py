from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="SetLeverage")


@attr.s(auto_attribs=True)
class SetLeverage:
    """
    Example:
        {'leverage': 25}

    Attributes:
        leverage (float): Leverage value confirmed by broker.
    """

    leverage: float

    def to_dict(self) -> Dict[str, Any]:
        leverage = self.leverage

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "leverage": leverage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        leverage = d.pop("leverage")

        set_leverage = cls(
            leverage=leverage,
        )

        return set_leverage
