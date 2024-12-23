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
from infobip_api_client.models.sms_destination import SmsDestination
from infobip_api_client.models.sms_message_content import SmsMessageContent
from infobip_api_client.models.sms_message_options import SmsMessageOptions
from infobip_api_client.models.sms_webhooks import SmsWebhooks
from typing import Optional, Set
from typing_extensions import Self


class SmsMessage(BaseModel):
    """
    An array of message objects of a single message or multiple messages sent under one bulk ID.
    """  # noqa: E501

    sender: Optional[StrictStr] = Field(
        default=None,
        description="The sender ID. It can be alphanumeric or numeric (e.g., `CompanyName`). Make sure you don't exceed [character limit](https://www.infobip.com/docs/sms/get-started#sender-names).",
    )
    destinations: List[SmsDestination] = Field(
        description="An array of destination objects for where messages are being sent. A valid destination is required."
    )
    content: SmsMessageContent
    options: Optional[SmsMessageOptions] = None
    webhooks: Optional[SmsWebhooks] = None
    __properties: ClassVar[List[str]] = [
        "sender",
        "destinations",
        "content",
        "options",
        "webhooks",
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
        """Create an instance of SmsMessage from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in destinations (list)
        _items = []
        if self.destinations:
            for _item in self.destinations:
                if _item:
                    _items.append(_item.to_dict())
            _dict["destinations"] = _items
        # override the default output from pydantic by calling `to_dict()` of content
        if self.content:
            _dict["content"] = self.content.to_dict()
        # override the default output from pydantic by calling `to_dict()` of options
        if self.options:
            _dict["options"] = self.options.to_dict()
        # override the default output from pydantic by calling `to_dict()` of webhooks
        if self.webhooks:
            _dict["webhooks"] = self.webhooks.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SmsMessage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "sender": obj.get("sender"),
                "destinations": [
                    SmsDestination.from_dict(_item) for _item in obj["destinations"]
                ]
                if obj.get("destinations") is not None
                else None,
                "content": SmsMessageContent.from_dict(obj["content"])
                if obj.get("content") is not None
                else None,
                "options": SmsMessageOptions.from_dict(obj["options"])
                if obj.get("options") is not None
                else None,
                "webhooks": SmsWebhooks.from_dict(obj["webhooks"])
                if obj.get("webhooks") is not None
                else None,
            }
        )
        return _obj