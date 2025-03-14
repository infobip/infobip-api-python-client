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
import pprint
import re  # noqa: F401
import json

from pydantic import ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from infobip_api_client.models.call_routing_destination import CallRoutingDestination
from infobip_api_client.models.security_config import SecurityConfig
from typing import Optional, Set
from typing_extensions import Self


class CallRoutingUrlDestination(CallRoutingDestination):
    """
    CallRoutingUrlDestination
    """  # noqa: E501

    url: StrictStr = Field(
        description="URL endpoint which provides next destination to be tried in a route as a response to `POST` HTTP request sent by the Infobip Platform. Returned destination must be of `ENDPOINT_DESTINATION` type."
    )
    security_config: Optional[SecurityConfig] = Field(
        default=None, alias="securityConfig"
    )
    __properties: ClassVar[List[str]] = [
        "priority",
        "type",
        "weight",
        "url",
        "securityConfig",
    ]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of CallRoutingUrlDestination from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of security_config
        if self.security_config:
            _dict["securityConfig"] = self.security_config.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CallRoutingUrlDestination from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "priority": obj.get("priority"),
                "type": obj.get("type"),
                "weight": obj.get("weight"),
                "url": obj.get("url"),
                "securityConfig": SecurityConfig.from_dict(obj["securityConfig"])
                if obj.get("securityConfig") is not None
                else None,
            }
        )
        return _obj
