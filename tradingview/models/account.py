from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.account_type import AccountType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_flags import AccountFlags
    from ..models.account_ui import AccountUi
    from ..models.duration import Duration


T = TypeVar("T", bound="Account")


@attr.s(auto_attribs=True)
class Account:
    """
    Attributes:
        id (str): Unique account identifier. Example: ACC-001.
        name (str): Account title that is displayed to a user. Example: Demo trading account.
        type (AccountType): Account type Example: demo.
        config (AccountFlags):
        currency (Union[Unset, str]): Abbreviation of account currency. Example: JPY.
        currency_sign (Union[Unset, str]): Account currency symbol. Example: ¥.
        ui (Union[Unset, AccountUi]): Account manager and Order dialog configuration for the account.
            The Account manager configuration will override configuration, specified in the
            [/config](#operation/getConfiguration) endpoint.
        durations (Union[Unset, List['Duration']]): Localized array of durations displayed in Order Ticket.
            It will override values, specified in the [/config](#operation/getConfiguration) endpoint.
        prefix (Union[Unset, str]): Prefix for instruments. Example: NASDAQ.
        is_verified (Union[Unset, bool]): Used to confirm that the account has been verified (for example, KYC is
            passed). Only verified account users can leave reviews in the broker profile. Example: True.
    """

    id: str
    name: str
    type: AccountType
    config: "AccountFlags"
    currency: Union[Unset, str] = UNSET
    currency_sign: Union[Unset, str] = UNSET
    ui: Union[Unset, "AccountUi"] = UNSET
    durations: Union[Unset, List["Duration"]] = UNSET
    prefix: Union[Unset, str] = UNSET
    is_verified: Union[Unset, bool] = False

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        type = self.type.value

        config = self.config.to_dict()

        currency = self.currency
        currency_sign = self.currency_sign
        ui: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ui, Unset):
            ui = self.ui.to_dict()

        durations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.durations, Unset):
            durations = []
            for componentsschemas_account_durations_item_data in self.durations:
                componentsschemas_account_durations_item = componentsschemas_account_durations_item_data.to_dict()

                durations.append(componentsschemas_account_durations_item)

        prefix = self.prefix
        is_verified = self.is_verified

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "name": name,
                "type": type,
                "config": config,
            }
        )
        if currency is not UNSET:
            field_dict["currency"] = currency
        if currency_sign is not UNSET:
            field_dict["currencySign"] = currency_sign
        if ui is not UNSET:
            field_dict["ui"] = ui
        if durations is not UNSET:
            field_dict["durations"] = durations
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if is_verified is not UNSET:
            field_dict["isVerified"] = is_verified

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.account_flags import AccountFlags
        from ..models.account_ui import AccountUi
        from ..models.duration import Duration

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        type = AccountType(d.pop("type"))

        config = AccountFlags.from_dict(d.pop("config"))

        currency = d.pop("currency", UNSET)

        currency_sign = d.pop("currencySign", UNSET)

        _ui = d.pop("ui", UNSET)
        ui: Union[Unset, AccountUi]
        if isinstance(_ui, Unset):
            ui = UNSET
        else:
            ui = AccountUi.from_dict(_ui)

        durations = []
        _durations = d.pop("durations", UNSET)
        for componentsschemas_account_durations_item_data in _durations or []:
            componentsschemas_account_durations_item = Duration.from_dict(componentsschemas_account_durations_item_data)

            durations.append(componentsschemas_account_durations_item)

        prefix = d.pop("prefix", UNSET)

        is_verified = d.pop("isVerified", UNSET)

        account = cls(
            id=id,
            name=name,
            type=type,
            config=config,
            currency=currency,
            currency_sign=currency_sign,
            ui=ui,
            durations=durations,
            prefix=prefix,
            is_verified=is_verified,
        )

        return account
