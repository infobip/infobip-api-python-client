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


class FormsType(str, Enum):
    """
    Form type
    """

    """
    allowed enum values
    """
    OPT_IN = "OPT_IN"
    OPT_OUT = "OPT_OUT"
    FACEBOOK = "FACEBOOK"
    LIVECHAT = "LIVECHAT"
    APPLE = "APPLE"
    CSAT = "CSAT"
    WA_FLOW = "WA_FLOW"

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of FormsType from a JSON string"""
        return cls(json.loads(json_str))
