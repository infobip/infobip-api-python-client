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


class TfaStartAuthenticationResponse(BaseModel):
    """
    TfaStartAuthenticationResponse
    """  # noqa: E501

    call_status: Optional[StrictStr] = Field(
        default=None,
        description="Call status, e.g. `PENDING_ACCEPTED`.",
        alias="callStatus",
    )
    nc_status: Optional[StrictStr] = Field(
        default=None,
        description="Status of sent [Number Lookup](https://www.infobip.com/docs/number-lookup). Number Lookup status can have one of the following values: `NC_DESTINATION_UNKNOWN`, `NC_DESTINATION_REACHABLE`, `NC_DESTINATION_NOT_REACHABLE`, `NC_NOT_CONFIGURED`. Contact your Account Manager, if you get the `NC_NOT_CONFIGURED` status. SMS will not be sent only if Number Lookup status is `NC_NOT_REACHABLE`.",
        alias="ncStatus",
    )
    pin_id: Optional[StrictStr] = Field(
        default=None, description="Sent PIN code ID.", alias="pinId"
    )
    sms_status: Optional[StrictStr] = Field(
        default=None,
        description="Sent SMS status. Can have one of the following values: `MESSAGE_SENT`, `MESSAGE_NOT_SENT`.",
        alias="smsStatus",
    )
    to: Optional[StrictStr] = Field(
        default=None,
        description="Phone number to which the 2FA message will be sent. Example: `41793026727`.",
    )
    __properties: ClassVar[List[str]] = [
        "callStatus",
        "ncStatus",
        "pinId",
        "smsStatus",
        "to",
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
        """Create an instance of TfaStartAuthenticationResponse from a JSON string"""
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
        """Create an instance of TfaStartAuthenticationResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "callStatus": obj.get("callStatus"),
                "ncStatus": obj.get("ncStatus"),
                "pinId": obj.get("pinId"),
                "smsStatus": obj.get("smsStatus"),
                "to": obj.get("to"),
            }
        )
        return _obj
