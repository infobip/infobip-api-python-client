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


class CallsRequestMediaStreamConfigType(str, Enum):
    """
    Media stream configuration type.
    """

    """
    allowed enum values
    """
    MEDIA_STREAMING = "MEDIA_STREAMING"
    WEBSOCKET_ENDPOINT = "WEBSOCKET_ENDPOINT"

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of CallsRequestMediaStreamConfigType from a JSON string"""
        return cls(json.loads(json_str))
