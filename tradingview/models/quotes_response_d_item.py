from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar

import attr

from ..models.status import Status

if TYPE_CHECKING:
    from ..models.single_quote import SingleQuote


T = TypeVar("T", bound="QuotesResponseDItem")


@attr.s(auto_attribs=True)
class QuotesResponseDItem:
    """Price response for an instrument.

    Attributes:
        s (Status):
        n (str): Symbol name. Should be equal to the requested one. Example: EURUSD.
        v (SingleQuote): Price and restriction data for an instrument.
    """

    s: Status
    n: str
    v: "SingleQuote"

    def to_dict(self) -> Dict[str, Any]:
        s = self.s.value

        n = self.n
        v = self.v.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "s": s,
                "n": n,
                "v": v,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.single_quote import SingleQuote

        d = src_dict.copy()
        s = Status(d.pop("s"))

        n = d.pop("n")

        v = SingleQuote.from_dict(d.pop("v"))

        quotes_response_d_item = cls(
            s=s,
            n=n,
            v=v,
        )

        return quotes_response_d_item
