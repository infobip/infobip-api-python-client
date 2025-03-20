# coding: utf-8

"""
    Infobip Client API Libraries OpenAPI Specification

    OpenAPI specification containing public endpoints supported in client API libraries.

    The version of the OpenAPI document: 1.0.0
    Contact: support@infobip.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class CallsLanguage(str, Enum):
    """
    Text language. Must be defined for correct pronunciation. For more details on available languages and voices, see our [documentation](https://www.infobip.com/docs/voice-and-video/outbound-calls#text-to-speech-voice-over-broadcast).
    """

    """
    allowed enum values
    """
    AR = "ar"
    BN = "bn"
    BG = "bg"
    CA = "ca"
    ZH_MINUS_CN = "zh-cn"
    ZH_MINUS_TW = "zh-tw"
    HR = "hr"
    CS = "cs"
    DA = "da"
    NL = "nl"
    EN = "en"
    EN_MINUS_AU = "en-au"
    EN_MINUS_GB = "en-gb"
    EN_MINUS_CA = "en-ca"
    EN_MINUS_IN = "en-in"
    EN_MINUS_IE = "en-ie"
    EN_MINUS_GB_MINUS_WLS = "en-gb-wls"
    EPO = "epo"
    FIL_MINUS_PH = "fil-ph"
    FI = "fi"
    FR = "fr"
    FR_MINUS_CA = "fr-ca"
    FR_MINUS_CH = "fr-ch"
    DE = "de"
    DE_MINUS_AT = "de-at"
    DE_MINUS_CH = "de-ch"
    EL = "el"
    GU = "gu"
    HE = "he"
    HI = "hi"
    HU = "hu"
    IS = "is"
    ID = "id"
    IT = "it"
    JA = "ja"
    KN = "kn"
    KO = "ko"
    MS = "ms"
    ML = "ml"
    NO = "no"
    PL = "pl"
    PT_MINUS_PT = "pt-pt"
    PT_MINUS_BR = "pt-br"
    RO = "ro"
    RU = "ru"
    SK = "sk"
    SL = "sl"
    ES = "es"
    ES_MINUS_GL = "es-gl"
    ES_MINUS_MX = "es-mx"
    SV = "sv"
    TA = "ta"
    TE = "te"
    TH = "th"
    TR = "tr"
    UK = "uk"
    VI = "vi"
    WLS = "wls"
    AR_MINUS_MA = "ar-ma"
    UR_MINUS_PK = "ur-pk"
    MR_MINUS_IN = "mr-in"

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of CallsLanguage from a JSON string"""
        return cls(json.loads(json_str))
