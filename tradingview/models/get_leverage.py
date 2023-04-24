from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="GetLeverage")


@attr.s(auto_attribs=True)
class GetLeverage:
    """
    Example:
        {'title': 'Adjust Leverage', 'leverage': 5, 'min': 1, 'max': 10, 'step': 1}

    Attributes:
        title (str): Title for leverage adjustment popup.
        leverage (float): Current leverage value.
        min_ (float): Minimum leverage value.
        max_ (float): Maximum leverage value.
        step (float): Leverage value change step.
    """

    title: str
    leverage: float
    min_: float
    max_: float
    step: float

    def to_dict(self) -> Dict[str, Any]:
        title = self.title
        leverage = self.leverage
        min_ = self.min_
        max_ = self.max_
        step = self.step

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "title": title,
                "leverage": leverage,
                "min": min_,
                "max": max_,
                "step": step,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        title = d.pop("title")

        leverage = d.pop("leverage")

        min_ = d.pop("min")

        max_ = d.pop("max")

        step = d.pop("step")

        get_leverage = cls(
            title=title,
            leverage=leverage,
            min_=min_,
            max_=max_,
            step=step,
        )

        return get_leverage
