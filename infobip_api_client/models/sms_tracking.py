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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self


class SmsTracking(BaseModel):
    """
    Sets up tracking parameters to track conversion metrics and type.
    """  # noqa: E501

    base_url: Optional[StrictStr] = Field(
        default=None,
        description="Custom base URL for shortened links in messages when tracking URL conversions. Legacy - use `urlOptions` instead.",
        alias="baseUrl",
    )
    process_key: Optional[StrictStr] = Field(
        default=None,
        description="The process key which uniquely identifies conversion tracking.",
        alias="processKey",
    )
    track: Optional[StrictStr] = Field(
        default=None,
        description="Indicates if a message has to be tracked for conversion rates. Values are: `SMS` and `URL`. `URL` is a legacy value. Use `urlOptions` instead. For more details on SMS Conversion, see: [Track Conversion](https://www.infobip.com/docs/sms/api#track-conversion).",
    )
    type: Optional[StrictStr] = Field(
        default=None,
        description="Sets a custom conversion type naming convention, e.g. `ONE_TIME_PIN` or `SOCIAL_INVITES`.",
    )
    __properties: ClassVar[List[str]] = ["baseUrl", "processKey", "track", "type"]

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
        """Create an instance of SmsTracking from a JSON string"""
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
        """Create an instance of SmsTracking from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "baseUrl": obj.get("baseUrl"),
                "processKey": obj.get("processKey"),
                "track": obj.get("track"),
                "type": obj.get("type"),
            }
        )
        return _obj
