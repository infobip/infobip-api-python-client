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


class CallRoutingUrlDestinationHttpRequest(BaseModel):
    """
    CallRoutingUrlDestinationHttpRequest
    """  # noqa: E501

    application_id: Optional[StrictStr] = Field(
        default="CALL_ROUTING",
        description="Identifier of the application that originated the call.",
        alias="applicationId",
    )
    route_id: Optional[StrictStr] = Field(
        default=None,
        description="Identifier of the route that is used to process the call.",
        alias="routeId",
    )
    call_id: Optional[StrictStr] = Field(
        default=None,
        description="Identifier of the call that is being processed.",
        alias="callId",
    )
    var_from: Optional[StrictStr] = Field(
        default=None,
        description="Phone number from which the call originated from.",
        alias="from",
    )
    to: Optional[StrictStr] = Field(
        default=None, description="Destination phone number of the call."
    )
    start_time: Optional[datetime] = Field(
        default=None,
        description="Timestamp representing start time of the call.",
        alias="startTime",
    )
    __properties: ClassVar[List[str]] = [
        "applicationId",
        "routeId",
        "callId",
        "from",
        "to",
        "startTime",
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
        """Create an instance of CallRoutingUrlDestinationHttpRequest from a JSON string"""
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
        """Create an instance of CallRoutingUrlDestinationHttpRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "applicationId": obj.get("applicationId")
                if obj.get("applicationId") is not None
                else "CALL_ROUTING",
                "routeId": obj.get("routeId"),
                "callId": obj.get("callId"),
                "from": obj.get("from"),
                "to": obj.get("to"),
                "startTime": obj.get("startTime"),
            }
        )
        return _obj