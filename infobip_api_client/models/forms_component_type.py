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


class FormsComponentType(str, Enum):
    """
    FormsComponentType
    """

    """
    allowed enum values
    """
    TEXT = "TEXT"
    TEXTAREA = "TEXTAREA"
    NUMBER = "NUMBER"
    DROPDOWN = "DROPDOWN"
    CHECKBOX = "CHECKBOX"
    CHECKBOX_GROUP = "CHECKBOX_GROUP"
    RADIOBUTTON = "RADIOBUTTON"
    DATE = "DATE"
    DATETIME = "DATETIME"
    EMAIL = "EMAIL"
    MSISDN = "MSISDN"
    SUBMIT_BUTTON = "SUBMIT_BUTTON"
    TITLE = "TITLE"
    DESCRIPTION = "DESCRIPTION"
    APPLE_SPLASH = "APPLE_SPLASH"
    APPLE_BOOLEAN = "APPLE_BOOLEAN"
    WHATSAPP_SCREEN = "WHATSAPP_SCREEN"
    WHATSAPP_HEADING = "WHATSAPP_HEADING"
    WHATSAPP_SUBHEADING = "WHATSAPP_SUBHEADING"
    WHATSAPP_BODY = "WHATSAPP_BODY"

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of FormsComponentType from a JSON string"""
        return cls(json.loads(json_str))
