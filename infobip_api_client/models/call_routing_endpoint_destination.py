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

from pydantic import ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from infobip_api_client.models.call_routing_destination import CallRoutingDestination
from infobip_api_client.models.call_routing_endpoint import CallRoutingEndpoint
from infobip_api_client.models.call_routing_recording import CallRoutingRecording
from infobip_api_client.models.delivery_time_window import DeliveryTimeWindow
from typing import Optional, Set
from typing_extensions import Self


class CallRoutingEndpointDestination(CallRoutingDestination):
    """
    CallRoutingEndpointDestination
    """  # noqa: E501

    value: CallRoutingEndpoint
    connect_timeout: Optional[StrictInt] = Field(
        default=None,
        description="Time to wait, in seconds, to establish a call toward the destination endpoint. The call will be terminated if it is not answered within the specified time.",
        alias="connectTimeout",
    )
    recording: Optional[CallRoutingRecording] = None
    allowed_time_windows: Optional[List[DeliveryTimeWindow]] = Field(
        default=None,
        description="Sets specific delivery windows outside of which calls won't be forwarded to the destination. If defined, call forwarding is allowed only if any time window in array is satisfied. ",
        alias="allowedTimeWindows",
    )
    __properties: ClassVar[List[str]] = [
        "priority",
        "type",
        "weight",
        "value",
        "connectTimeout",
        "recording",
        "allowedTimeWindows",
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
        """Create an instance of CallRoutingEndpointDestination from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of value
        if self.value:
            _dict["value"] = self.value.to_dict()
        # override the default output from pydantic by calling `to_dict()` of recording
        if self.recording:
            _dict["recording"] = self.recording.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in allowed_time_windows (list)
        _items = []
        if self.allowed_time_windows:
            for _item in self.allowed_time_windows:
                if _item:
                    _items.append(_item.to_dict())
            _dict["allowedTimeWindows"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CallRoutingEndpointDestination from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "priority": obj.get("priority"),
                "type": obj.get("type"),
                "weight": obj.get("weight"),
                "value": CallRoutingEndpoint.from_dict(obj["value"])
                if obj.get("value") is not None
                else None,
                "connectTimeout": obj.get("connectTimeout"),
                "recording": CallRoutingRecording.from_dict(obj["recording"])
                if obj.get("recording") is not None
                else None,
                "allowedTimeWindows": [
                    DeliveryTimeWindow.from_dict(_item)
                    for _item in obj["allowedTimeWindows"]
                ]
                if obj.get("allowedTimeWindows") is not None
                else None,
            }
        )
        return _obj
