from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.locale import Locale
from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthorizeData")


@attr.s(auto_attribs=True)
class AuthorizeData:
    """
    Attributes:
        login (str): User login.
        password (str): User password.
        locale (Union[Unset, Locale]): Locale (language) id. This parameter is required for trading integration only.
    """

    login: str
    password: str
    locale: Union[Unset, Locale] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        login = self.login
        password = self.password
        locale: Union[Unset, str] = UNSET
        if not isinstance(self.locale, Unset):
            locale = self.locale.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "login": login,
                "password": password,
            }
        )
        if locale is not UNSET:
            field_dict["locale"] = locale

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        login = d.pop("login")

        password = d.pop("password")

        _locale = d.pop("locale", UNSET)
        locale: Union[Unset, Locale]
        if isinstance(_locale, Unset):
            locale = UNSET
        else:
            locale = Locale(_locale)

        authorize_data = cls(
            login=login,
            password=password,
            locale=locale,
        )

        authorize_data.additional_properties = d
        return authorize_data

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
