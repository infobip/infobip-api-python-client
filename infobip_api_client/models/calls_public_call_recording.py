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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from infobip_api_client.models.call_direction import CallDirection
from infobip_api_client.models.call_endpoint import CallEndpoint
from infobip_api_client.models.calls_public_recording_file import (
    CallsPublicRecordingFile,
)
from infobip_api_client.models.calls_recording_status import CallsRecordingStatus
from typing import Optional, Set
from typing_extensions import Self


class CallsPublicCallRecording(BaseModel):
    """
    CallsPublicCallRecording
    """  # noqa: E501

    call_id: Optional[Annotated[str, Field(strict=True, max_length=128)]] = Field(
        default=None, description="Call ID.", alias="callId"
    )
    endpoint: CallEndpoint
    direction: Optional[CallDirection] = None
    files: Optional[List[CallsPublicRecordingFile]] = Field(
        default=None, description="Call recording files."
    )
    status: Optional[CallsRecordingStatus] = None
    reason: Optional[StrictStr] = Field(
        default=None, description="Reason for recording failure."
    )
    calls_configuration_id: Optional[StrictStr] = Field(
        default=None,
        description="Calls Configuration ID.",
        alias="callsConfigurationId",
    )
    application_id: Optional[StrictStr] = Field(
        default=None, description="Application ID.", alias="applicationId"
    )
    start_time: Optional[datetime] = Field(
        default=None,
        description="Date and time when the (first) call recording started.",
        alias="startTime",
    )
    end_time: Optional[datetime] = Field(
        default=None,
        description="Date and time when the (last) call recording ended.",
        alias="endTime",
    )
    __properties: ClassVar[List[str]] = [
        "callId",
        "endpoint",
        "direction",
        "files",
        "status",
        "reason",
        "callsConfigurationId",
        "applicationId",
        "startTime",
        "endTime",
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
        """Create an instance of CallsPublicCallRecording from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in files (list)
        _items = []
        if self.files:
            for _item in self.files:
                if _item:
                    _items.append(_item.to_dict())
            _dict["files"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CallsPublicCallRecording from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "callId": obj.get("callId"),
                "endpoint": CallEndpoint.from_dict(obj["endpoint"])
                if obj.get("endpoint") is not None
                else None,
                "direction": obj.get("direction"),
                "files": [
                    CallsPublicRecordingFile.from_dict(_item) for _item in obj["files"]
                ]
                if obj.get("files") is not None
                else None,
                "status": obj.get("status"),
                "reason": obj.get("reason"),
                "callsConfigurationId": obj.get("callsConfigurationId"),
                "applicationId": obj.get("applicationId"),
                "startTime": obj.get("startTime"),
                "endTime": obj.get("endTime"),
            }
        )
        return _obj
