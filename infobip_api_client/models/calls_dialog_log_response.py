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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from infobip_api_client.models.calls_dialog_recording_log import CallsDialogRecordingLog
from infobip_api_client.models.calls_dialog_state import CallsDialogState
from infobip_api_client.models.calls_error_code_info import CallsErrorCodeInfo
from typing import Optional, Set
from typing_extensions import Self


class CallsDialogLogResponse(BaseModel):
    """
    CallsDialogLogResponse
    """  # noqa: E501

    dialog_id: Optional[Annotated[str, Field(strict=True, max_length=128)]] = Field(
        default=None, description="Unique dialog ID.", alias="dialogId"
    )
    calls_configuration_id: Optional[StrictStr] = Field(
        default=None,
        description="Calls Configuration ID.",
        alias="callsConfigurationId",
    )
    application_id: Optional[StrictStr] = Field(
        default=None, description="Application ID.", alias="applicationId"
    )
    state: Optional[CallsDialogState] = None
    start_time: Optional[datetime] = Field(
        default=None,
        description="Date and time for when the dialog has been created.",
        alias="startTime",
    )
    establish_time: Optional[datetime] = Field(
        default=None,
        description="Date and time for when the dialog has been established.",
        alias="establishTime",
    )
    end_time: Optional[datetime] = Field(
        default=None,
        description="Date and time for when the dialog has been finished.",
        alias="endTime",
    )
    parent_call_id: Optional[
        Annotated[str, Field(strict=True, max_length=128)]
    ] = Field(default=None, description="Unique parent call ID.", alias="parentCallId")
    child_call_id: Optional[Annotated[str, Field(strict=True, max_length=128)]] = Field(
        default=None, description="Unique child call ID.", alias="childCallId"
    )
    duration: Optional[StrictInt] = Field(
        default=None, description="Dialog duration in seconds."
    )
    recording: Optional[CallsDialogRecordingLog] = None
    error_code: Optional[CallsErrorCodeInfo] = Field(default=None, alias="errorCode")
    __properties: ClassVar[List[str]] = [
        "dialogId",
        "callsConfigurationId",
        "applicationId",
        "state",
        "startTime",
        "establishTime",
        "endTime",
        "parentCallId",
        "childCallId",
        "duration",
        "recording",
        "errorCode",
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
        """Create an instance of CallsDialogLogResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of recording
        if self.recording:
            _dict["recording"] = self.recording.to_dict()
        # override the default output from pydantic by calling `to_dict()` of error_code
        if self.error_code:
            _dict["errorCode"] = self.error_code.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CallsDialogLogResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "dialogId": obj.get("dialogId"),
                "callsConfigurationId": obj.get("callsConfigurationId"),
                "applicationId": obj.get("applicationId"),
                "state": obj.get("state"),
                "startTime": obj.get("startTime"),
                "establishTime": obj.get("establishTime"),
                "endTime": obj.get("endTime"),
                "parentCallId": obj.get("parentCallId"),
                "childCallId": obj.get("childCallId"),
                "duration": obj.get("duration"),
                "recording": CallsDialogRecordingLog.from_dict(obj["recording"])
                if obj.get("recording") is not None
                else None,
                "errorCode": CallsErrorCodeInfo.from_dict(obj["errorCode"])
                if obj.get("errorCode") is not None
                else None,
            }
        )
        return _obj