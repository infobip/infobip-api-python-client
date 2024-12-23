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


class FlowOrigin(str, Enum):
    """
    The information which describes the source of the last modification of record.
    """

    """
    allowed enum values
    """
    API = "API"
    PORTAL = "PORTAL"
    WEB_SDK = "WEB_SDK"
    INTEGRATION = "INTEGRATION"
    PUSH = "PUSH"
    FACEBOOK = "FACEBOOK"
    LINE = "LINE"
    TELEGRAM = "TELEGRAM"
    SALESFORCE = "SALESFORCE"
    DYNAMICS = "DYNAMICS"
    ZAPIER = "ZAPIER"
    FORMS = "FORMS"
    COMPUTED = "COMPUTED"
    ANSWERS = "ANSWERS"
    CONVERSATIONS = "CONVERSATIONS"

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of FlowOrigin from a JSON string"""
        return cls(json.loads(json_str))
