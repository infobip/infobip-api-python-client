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
from infobip_api_client.models.calls_conference_recording_request import (
    CallsConferenceRecordingRequest,
)
from typing import Optional, Set
from typing_extensions import Self


class CallsConferenceRequest(BaseModel):
    """
    CallsConferenceRequest
    """  # noqa: E501

    name: Optional[StrictStr] = Field(
        default=None,
        description="Conference name, will be auto-generated if not provided.",
    )
    recording: Optional[CallsConferenceRecordingRequest] = None
    max_duration: Optional[StrictInt] = Field(
        default=28800, description="Max duration in seconds.", alias="maxDuration"
    )
    calls_configuration_id: Optional[StrictStr] = Field(
        default=None,
        description="Calls Configuration ID.",
        alias="callsConfigurationId",
    )
    application_id: Optional[StrictStr] = Field(
        default=None, description="Application ID.", alias="applicationId"
    )
    __properties: ClassVar[List[str]] = [
        "name",
        "recording",
        "maxDuration",
        "callsConfigurationId",
        "applicationId",
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
        """Create an instance of CallsConferenceRequest from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CallsConferenceRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "name": obj.get("name"),
                "recording": CallsConferenceRecordingRequest.from_dict(obj["recording"])
                if obj.get("recording") is not None
                else None,
                "maxDuration": obj.get("maxDuration")
                if obj.get("maxDuration") is not None
                else 28800,
                "callsConfigurationId": obj.get("callsConfigurationId"),
                "applicationId": obj.get("applicationId"),
            }
        )
        return _obj
