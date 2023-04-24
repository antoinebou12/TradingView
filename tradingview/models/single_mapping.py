from typing import Any, Dict, List, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="SingleMapping")


@attr.s(auto_attribs=True)
class SingleMapping:
    """Map of Broker instrument name to TradingView instrument name.

    Attributes:
        f (List[str]): An array with the only one string element &ndash; broker symbol name.
        s (str): TradingView symbol name with a prefix (AA:XXXX). Example: FX_IDC:EURUSD.
    """

    f: List[str]
    s: str

    def to_dict(self) -> Dict[str, Any]:
        f = self.f

        s = self.s

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "f": f,
                "s": s,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        f = cast(List[str], d.pop("f"))

        s = d.pop("s")

        single_mapping = cls(
            f=f,
            s=s,
        )

        return single_mapping
