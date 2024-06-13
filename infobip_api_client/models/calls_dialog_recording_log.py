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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from infobip_api_client.models.calls_public_call_recording import (
    CallsPublicCallRecording,
)
from infobip_api_client.models.calls_public_recording_file import (
    CallsPublicRecordingFile,
)
from typing import Optional, Set
from typing_extensions import Self


class CallsDialogRecordingLog(BaseModel):
    """
    Dialog recordings.
    """  # noqa: E501

    composed_files: Optional[List[CallsPublicRecordingFile]] = Field(
        default=None,
        description="File(s) with a recording of both dialog calls.",
        alias="composedFiles",
    )
    call_recordings: Optional[List[CallsPublicCallRecording]] = Field(
        default=None,
        description="File(s) with a recording of individual dialog calls.",
        alias="callRecordings",
    )
    __properties: ClassVar[List[str]] = ["composedFiles", "callRecordings"]

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
        """Create an instance of CallsDialogRecordingLog from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in composed_files (list)
        _items = []
        if self.composed_files:
            for _item in self.composed_files:
                if _item:
                    _items.append(_item.to_dict())
            _dict["composedFiles"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in call_recordings (list)
        _items = []
        if self.call_recordings:
            for _item in self.call_recordings:
                if _item:
                    _items.append(_item.to_dict())
            _dict["callRecordings"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CallsDialogRecordingLog from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "composedFiles": [
                    CallsPublicRecordingFile.from_dict(_item)
                    for _item in obj["composedFiles"]
                ]
                if obj.get("composedFiles") is not None
                else None,
                "callRecordings": [
                    CallsPublicCallRecording.from_dict(_item)
                    for _item in obj["callRecordings"]
                ]
                if obj.get("callRecordings") is not None
                else None,
            }
        )
        return _obj
