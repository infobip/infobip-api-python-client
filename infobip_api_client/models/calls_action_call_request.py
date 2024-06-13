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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from infobip_api_client.models.call_endpoint import CallEndpoint
from infobip_api_client.models.call_recording_request import CallRecordingRequest
from infobip_api_client.models.calls_machine_detection_request import (
    CallsMachineDetectionRequest,
)
from typing import Optional, Set
from typing_extensions import Self


class CallsActionCallRequest(BaseModel):
    """
    CallsActionCallRequest
    """  # noqa: E501

    endpoint: CallEndpoint
    var_from: StrictStr = Field(
        description="Caller identifier. Must be a number in the [E.164](https://en.wikipedia.org/wiki/E.164) format for calls to `PHONE`, a string for calls to `WEBRTC` or `SIP`, and a Viber Voice number for calls to `VIBER`.",
        alias="from",
    )
    from_display_name: Optional[StrictStr] = Field(
        default=None,
        description="Display name to show when placing calls towards WEBRTC endpoints. Can be any alphanumeric string.",
        alias="fromDisplayName",
    )
    connect_timeout: Optional[StrictInt] = Field(
        default=None,
        description="Time to wait, in seconds, before the called party answers the call.",
        alias="connectTimeout",
    )
    recording: Optional[CallRecordingRequest] = None
    machine_detection: Optional[CallsMachineDetectionRequest] = Field(
        default=None, alias="machineDetection"
    )
    max_duration: Optional[StrictInt] = Field(
        default=28800, description="Max duration in seconds.", alias="maxDuration"
    )
    custom_data: Optional[Dict[str, StrictStr]] = Field(
        default=None, description="Custom data.", alias="customData"
    )
    __properties: ClassVar[List[str]] = [
        "endpoint",
        "from",
        "fromDisplayName",
        "connectTimeout",
        "recording",
        "machineDetection",
        "maxDuration",
        "customData",
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
        """Create an instance of CallsActionCallRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of endpoint
        if self.endpoint:
            _dict["endpoint"] = self.endpoint.to_dict()
        # override the default output from pydantic by calling `to_dict()` of recording
        if self.recording:
            _dict["recording"] = self.recording.to_dict()
        # override the default output from pydantic by calling `to_dict()` of machine_detection
        if self.machine_detection:
            _dict["machineDetection"] = self.machine_detection.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CallsActionCallRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "endpoint": CallEndpoint.from_dict(obj["endpoint"])
                if obj.get("endpoint") is not None
                else None,
                "from": obj.get("from"),
                "fromDisplayName": obj.get("fromDisplayName"),
                "connectTimeout": obj.get("connectTimeout"),
                "recording": CallRecordingRequest.from_dict(obj["recording"])
                if obj.get("recording") is not None
                else None,
                "machineDetection": CallsMachineDetectionRequest.from_dict(
                    obj["machineDetection"]
                )
                if obj.get("machineDetection") is not None
                else None,
                "maxDuration": obj.get("maxDuration")
                if obj.get("maxDuration") is not None
                else 28800,
                "customData": obj.get("customData"),
            }
        )
        return _obj
