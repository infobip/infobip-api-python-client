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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from infobip_api_client.models.call_direction import CallDirection
from infobip_api_client.models.call_endpoint import CallEndpoint
from infobip_api_client.models.call_state import CallState
from infobip_api_client.models.calls_error_code_info import CallsErrorCodeInfo
from infobip_api_client.models.calls_machine_detection_properties import (
    CallsMachineDetectionProperties,
)
from typing import Optional, Set
from typing_extensions import Self


class CallLog(BaseModel):
    """
    CallLog
    """  # noqa: E501

    call_id: Optional[Annotated[str, Field(strict=True, max_length=128)]] = Field(
        default=None, description="Unique call ID.", alias="callId"
    )
    endpoint: CallEndpoint
    var_from: Optional[StrictStr] = Field(
        default=None, description="Caller ID.", alias="from"
    )
    to: Optional[StrictStr] = Field(default=None, description="Callee ID.")
    direction: Optional[CallDirection] = None
    state: Optional[CallState] = None
    start_time: Optional[datetime] = Field(
        default=None,
        description="Date and time for when the call has been created.",
        alias="startTime",
    )
    answer_time: Optional[datetime] = Field(
        default=None,
        description="Date and time for when the call has been answered.",
        alias="answerTime",
    )
    end_time: Optional[datetime] = Field(
        default=None,
        description="Date and time for when the call has been finished.",
        alias="endTime",
    )
    parent_call_id: Optional[
        Annotated[str, Field(strict=True, max_length=128)]
    ] = Field(default=None, description="Parent call ID.", alias="parentCallId")
    machine_detection: Optional[CallsMachineDetectionProperties] = Field(
        default=None, alias="machineDetection"
    )
    ring_duration: Optional[StrictInt] = Field(
        default=None, description="Ringing duration in seconds.", alias="ringDuration"
    )
    calls_configuration_ids: Optional[List[StrictStr]] = Field(
        default=None,
        description="IDs of the calls configurations used during the call.",
        alias="callsConfigurationIds",
    )
    application_ids: Optional[List[StrictStr]] = Field(
        default=None,
        description="IDs of the applications used during the call.",
        alias="applicationIds",
    )
    conference_ids: Optional[List[StrictStr]] = Field(
        default=None,
        description="IDs of the conferences where the call was a participant.",
        alias="conferenceIds",
    )
    duration: Optional[StrictInt] = Field(
        default=None, description="Call duration in seconds."
    )
    has_camera_video: Optional[StrictBool] = Field(
        default=None,
        description="Indicates if camera was enabled during the call.",
        alias="hasCameraVideo",
    )
    has_screenshare_video: Optional[StrictBool] = Field(
        default=None,
        description="Indicates if screen sharing was enabled during the call.",
        alias="hasScreenshareVideo",
    )
    error_code: Optional[CallsErrorCodeInfo] = Field(default=None, alias="errorCode")
    custom_data: Optional[Dict[str, StrictStr]] = Field(
        default=None, description="Custom data.", alias="customData"
    )
    dialog_id: Optional[Annotated[str, Field(strict=True, max_length=128)]] = Field(
        default=None, description="Dialog ID.", alias="dialogId"
    )
    sender: Optional[StrictStr] = Field(default=None, description="Sender.")
    __properties: ClassVar[List[str]] = [
        "callId",
        "endpoint",
        "from",
        "to",
        "direction",
        "state",
        "startTime",
        "answerTime",
        "endTime",
        "parentCallId",
        "machineDetection",
        "ringDuration",
        "callsConfigurationIds",
        "applicationIds",
        "conferenceIds",
        "duration",
        "hasCameraVideo",
        "hasScreenshareVideo",
        "errorCode",
        "customData",
        "dialogId",
        "sender",
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
        """Create an instance of CallLog from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of machine_detection
        if self.machine_detection:
            _dict["machineDetection"] = self.machine_detection.to_dict()
        # override the default output from pydantic by calling `to_dict()` of error_code
        if self.error_code:
            _dict["errorCode"] = self.error_code.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CallLog from a dict"""
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
                "from": obj.get("from"),
                "to": obj.get("to"),
                "direction": obj.get("direction"),
                "state": obj.get("state"),
                "startTime": obj.get("startTime"),
                "answerTime": obj.get("answerTime"),
                "endTime": obj.get("endTime"),
                "parentCallId": obj.get("parentCallId"),
                "machineDetection": CallsMachineDetectionProperties.from_dict(
                    obj["machineDetection"]
                )
                if obj.get("machineDetection") is not None
                else None,
                "ringDuration": obj.get("ringDuration"),
                "callsConfigurationIds": obj.get("callsConfigurationIds"),
                "applicationIds": obj.get("applicationIds"),
                "conferenceIds": obj.get("conferenceIds"),
                "duration": obj.get("duration"),
                "hasCameraVideo": obj.get("hasCameraVideo"),
                "hasScreenshareVideo": obj.get("hasScreenshareVideo"),
                "errorCode": CallsErrorCodeInfo.from_dict(obj["errorCode"])
                if obj.get("errorCode") is not None
                else None,
                "customData": obj.get("customData"),
                "dialogId": obj.get("dialogId"),
                "sender": obj.get("sender"),
            }
        )
        return _obj
