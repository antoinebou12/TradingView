from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.single_field import SingleField
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.single_mapping import SingleMapping


T = TypeVar("T", bound="SymbolMapping")


@attr.s(auto_attribs=True)
class SymbolMapping:
    """Map of Broker instrument names and TradingView instrument names.

    Example:
        {'symbols': [{'f': ['EURUSD'], 's': 'FX_IDC:EURUSD'}, {'f': ['AAPLE'], 's': 'NASDAQ:AAPLE'}], 'fields':
            ['brokerSymbol']}

    Attributes:
        symbols (Union[Unset, List['SingleMapping']]):
        fields (Union[Unset, List[SingleField]]): Array with the only one element `['brokerSymbol']`.
    """

    symbols: Union[Unset, List["SingleMapping"]] = UNSET
    fields: Union[Unset, List[SingleField]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        symbols: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.symbols, Unset):
            symbols = []
            for symbols_item_data in self.symbols:
                symbols_item = symbols_item_data.to_dict()

                symbols.append(symbols_item)

        fields: Union[Unset, List[str]] = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for fields_item_data in self.fields:
                fields_item = fields_item_data.value

                fields.append(fields_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if symbols is not UNSET:
            field_dict["symbols"] = symbols
        if fields is not UNSET:
            field_dict["fields"] = fields

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.single_mapping import SingleMapping

        d = src_dict.copy()
        symbols = []
        _symbols = d.pop("symbols", UNSET)
        for symbols_item_data in _symbols or []:
            symbols_item = SingleMapping.from_dict(symbols_item_data)

            symbols.append(symbols_item)

        fields = []
        _fields = d.pop("fields", UNSET)
        for fields_item_data in _fields or []:
            fields_item = SingleField(fields_item_data)

            fields.append(fields_item)

        symbol_mapping = cls(
            symbols=symbols,
            fields=fields,
        )

        return symbol_mapping
