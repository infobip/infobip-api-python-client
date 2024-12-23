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
from typing import Optional, Set
from typing_extensions import Self


class CallsRecordedIvrFile(BaseModel):
    """
    Array of recorded files metadata, one for each recorded file.
    """  # noqa: E501

    message_id: Optional[StrictStr] = Field(
        default=None,
        description="The ID that uniquely identifies the sent message.",
        alias="messageId",
    )
    var_from: Optional[StrictStr] = Field(
        default=None, description="Numeric sender ID.", alias="from"
    )
    to: Optional[StrictStr] = Field(default=None, description="Destination address.")
    scenario_id: Optional[StrictStr] = Field(
        default=None, description="Scenario key.", alias="scenarioId"
    )
    group_id: Optional[StrictStr] = Field(
        default=None,
        description="Differentiates recordings made by separate Record actions.",
        alias="groupId",
    )
    url: Optional[StrictStr] = Field(
        default=None,
        description="Relative URL path to the recorded file. To download the audio, just perform a GET request using the relative URL of a specific file. The returned audio data is encoded as PCM 16bit 8kHz WAVE audio. The files are available on Infobip servers for 2 months.",
    )
    recorded_at: Optional[datetime] = Field(
        default=None,
        description="The time the recording took place.",
        alias="recordedAt",
    )
    __properties: ClassVar[List[str]] = [
        "messageId",
        "from",
        "to",
        "scenarioId",
        "groupId",
        "url",
        "recordedAt",
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
        """Create an instance of CallsRecordedIvrFile from a JSON string"""
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
        """Create an instance of CallsRecordedIvrFile from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "messageId": obj.get("messageId"),
                "from": obj.get("from"),
                "to": obj.get("to"),
                "scenarioId": obj.get("scenarioId"),
                "groupId": obj.get("groupId"),
                "url": obj.get("url"),
                "recordedAt": obj.get("recordedAt"),
            }
        )
        return _obj
