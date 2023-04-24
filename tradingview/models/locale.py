from enum import Enum


class Locale(str, Enum):
    AR_AE = "ar_AE"
    BR = "br"
    CS = "cs"
    DE_DE = "de_DE"
    EL = "el"
    EN = "en"
    ES = "es"
    FA_IR = "fa_IR"
    FR = "fr"
    HE_IL = "he_IL"
    HU_HU = "hu_HU"
    ID = "id"
    IN = "in"
    IT = "it"
    JA = "ja"
    KR = "kr"
    MS_MY = "ms_MY"
    NL_NL = "nl_NL"
    PL = "pl"
    RO = "ro"
    RU = "ru"
    SV_SE = "sv_SE"
    TH_TH = "th_TH"
    TR = "tr"
    UK = "uk"
    VI_VN = "vi_VN"
    ZH_CN = "zh_CN"
    ZH_TW = "zh_TW"

    def __str__(self) -> str:
        return str(self.value)
