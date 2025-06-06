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
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self


class SmsDestination(BaseModel):
    """
    An array of destination objects for where messages are being sent. A valid destination is required.
    """  # noqa: E501

    to: Annotated[str, Field(min_length=0, strict=True, max_length=64)] = Field(
        description="The destination address of the message."
    )
    message_id: Optional[StrictStr] = Field(
        default=None,
        description="The ID that uniquely identifies the message sent.",
        alias="messageId",
    )
    network_id: Optional[StrictInt] = Field(
        default=None,
        description="Available in US and Canada only if networkId is known for Network Operator of the destination. Returned in [SMS message delivery reports](https://www.infobip.com/docs/api/channels/sms/sms-messaging/logs-and-status-reports) and [Inbound SMS](https://www.infobip.com/docs/api/channels/sms/sms-messaging/inbound-sms); contact Infobip Support to enable.",
        alias="networkId",
    )
    __properties: ClassVar[List[str]] = ["to", "messageId", "networkId"]

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
        """Create an instance of SmsDestination from a JSON string"""
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
        """Create an instance of SmsDestination from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "to": obj.get("to"),
                "messageId": obj.get("messageId"),
                "networkId": obj.get("networkId"),
            }
        )
        return _obj
