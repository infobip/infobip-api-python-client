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
from infobip_api_client.models.call_routing_endpoint import CallRoutingEndpoint
from infobip_api_client.models.call_routing_endpoint_type import CallRoutingEndpointType
from typing import Optional, Set
from typing_extensions import Self


class CallRoutingSipEndpoint(CallRoutingEndpoint):
    """
    CallRoutingSipEndpoint
    """  # noqa: E501

    username: Optional[StrictStr] = Field(
        default=None,
        description="Username sent to a selected SIP trunk. When not defined, Infobip DID number is used instead.",
    )
    sip_trunk_id: StrictStr = Field(
        description="Unique identifier of a SIP trunk.", alias="sipTrunkId"
    )
    custom_headers: Optional[Dict[str, StrictStr]] = Field(
        default=None,
        description="Custom headers. Only headers starting with `X-Client-` prefix will be propagated.",
        alias="customHeaders",
    )
    __properties: ClassVar[List[str]] = [
        "type",
        "username",
        "sipTrunkId",
        "customHeaders",
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
        """Create an instance of CallRoutingSipEndpoint from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CallRoutingSipEndpoint from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "type": obj.get("type"),
                "username": obj.get("username"),
                "sipTrunkId": obj.get("sipTrunkId"),
                "customHeaders": obj.get("customHeaders"),
            }
        )
        return _obj
