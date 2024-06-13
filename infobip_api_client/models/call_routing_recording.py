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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from infobip_api_client.models.call_routing_recording_composition import (
    CallRoutingRecordingComposition,
)
from infobip_api_client.models.call_routing_recording_type import (
    CallRoutingRecordingType,
)
from typing import Optional, Set
from typing_extensions import Self


class CallRoutingRecording(BaseModel):
    """
    If set, captures the call session from an established call to a given destination.
    """  # noqa: E501

    recording_type: CallRoutingRecordingType = Field(alias="recordingType")
    recording_composition: Optional[CallRoutingRecordingComposition] = Field(
        default=None, alias="recordingComposition"
    )
    custom_data: Optional[Dict[str, StrictStr]] = Field(
        default=None,
        description="Client-defined data visible when a recording is downloaded.",
        alias="customData",
    )
    file_prefix: Optional[
        Annotated[str, Field(min_length=1, strict=True, max_length=100)]
    ] = Field(
        default=None,
        description="Custom name for the recording's zip file. Applicable only when SFTP server is enabled on [Voice settings page](https://portal.infobip.com/apps/voice/recording/settings). For recordings without composition, `callId` and `fileId` will be appended to the `filePrefix` value. For recordings with composition, `fileId` will be appended to the `filePrefix` value.",
        alias="filePrefix",
    )
    __properties: ClassVar[List[str]] = [
        "recordingType",
        "recordingComposition",
        "customData",
        "filePrefix",
    ]

    @field_validator("file_prefix")
    def file_prefix_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-zA-Z0-9_\-]*$", value):
            raise ValueError(
                r"must validate the regular expression /^[a-zA-Z0-9_\-]*$/"
            )
        return value

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
        """Create an instance of CallRoutingRecording from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of recording_composition
        if self.recording_composition:
            _dict["recordingComposition"] = self.recording_composition.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CallRoutingRecording from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "recordingType": obj.get("recordingType"),
                "recordingComposition": CallRoutingRecordingComposition.from_dict(
                    obj["recordingComposition"]
                )
                if obj.get("recordingComposition") is not None
                else None,
                "customData": obj.get("customData"),
                "filePrefix": obj.get("filePrefix"),
            }
        )
        return _obj
