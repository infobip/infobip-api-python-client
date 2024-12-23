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
from infobip_api_client.models.flow_common_ott_contact import FlowCommonOttContact
from infobip_api_client.models.flow_common_push_contact import FlowCommonPushContact
from infobip_api_client.models.flow_email_contact import FlowEmailContact
from infobip_api_client.models.flow_phone_contact import FlowPhoneContact
from infobip_api_client.models.flow_push_contact import FlowPushContact
from typing import Optional, Set
from typing_extensions import Self


class FlowPersonContacts(BaseModel):
    """
    List of phones, emails and other information how a person can be contacted.
    """  # noqa: E501

    phone: Optional[List[FlowPhoneContact]] = Field(
        default=None,
        description="A list of person's phone numbers. Max 100 numbers per person.",
    )
    email: Optional[List[FlowEmailContact]] = Field(
        default=None,
        description="A list of person's email addresses. Max 100 emails per person.",
    )
    push: Optional[List[FlowPushContact]] = Field(
        default=None, description="List of person's push registrations."
    )
    facebook: Optional[List[FlowCommonOttContact]] = Field(
        default=None, description="A list of person's Messenger destinations."
    )
    line: Optional[List[FlowCommonOttContact]] = Field(
        default=None, description="A list of person's Line destinations."
    )
    viber_bots: Optional[List[FlowCommonOttContact]] = Field(
        default=None,
        description="A list of person's Viber Bots destinations.",
        alias="viberBots",
    )
    live_chat: Optional[List[FlowCommonOttContact]] = Field(
        default=None,
        description="A list of person's Live Chat destinations.",
        alias="liveChat",
    )
    instagram: Optional[List[FlowCommonOttContact]] = Field(
        default=None, description="A list of person's Instagram destinations."
    )
    telegram: Optional[List[FlowCommonOttContact]] = Field(
        default=None, description="A list of person's Telegram destinations."
    )
    apple_business_chat: Optional[List[FlowCommonOttContact]] = Field(
        default=None,
        description="A list of person's Apple Business Chat destinations.",
        alias="appleBusinessChat",
    )
    webpush: Optional[List[FlowCommonPushContact]] = Field(
        default=None, description="A list of person's web push destinations."
    )
    instagram_dm: Optional[List[FlowCommonOttContact]] = Field(
        default=None,
        description="A list of person's Instagram DM destinations.",
        alias="instagramDm",
    )
    kakao_sangdam: Optional[List[FlowCommonOttContact]] = Field(
        default=None,
        description="A list of person's Kakao Sangdam destinations.",
        alias="kakaoSangdam",
    )
    __properties: ClassVar[List[str]] = [
        "phone",
        "email",
        "push",
        "facebook",
        "line",
        "viberBots",
        "liveChat",
        "instagram",
        "telegram",
        "appleBusinessChat",
        "webpush",
        "instagramDm",
        "kakaoSangdam",
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
        """Create an instance of FlowPersonContacts from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in phone (list)
        _items = []
        if self.phone:
            for _item in self.phone:
                if _item:
                    _items.append(_item.to_dict())
            _dict["phone"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in email (list)
        _items = []
        if self.email:
            for _item in self.email:
                if _item:
                    _items.append(_item.to_dict())
            _dict["email"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in push (list)
        _items = []
        if self.push:
            for _item in self.push:
                if _item:
                    _items.append(_item.to_dict())
            _dict["push"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in facebook (list)
        _items = []
        if self.facebook:
            for _item in self.facebook:
                if _item:
                    _items.append(_item.to_dict())
            _dict["facebook"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in line (list)
        _items = []
        if self.line:
            for _item in self.line:
                if _item:
                    _items.append(_item.to_dict())
            _dict["line"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in viber_bots (list)
        _items = []
        if self.viber_bots:
            for _item in self.viber_bots:
                if _item:
                    _items.append(_item.to_dict())
            _dict["viberBots"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in live_chat (list)
        _items = []
        if self.live_chat:
            for _item in self.live_chat:
                if _item:
                    _items.append(_item.to_dict())
            _dict["liveChat"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in instagram (list)
        _items = []
        if self.instagram:
            for _item in self.instagram:
                if _item:
                    _items.append(_item.to_dict())
            _dict["instagram"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in telegram (list)
        _items = []
        if self.telegram:
            for _item in self.telegram:
                if _item:
                    _items.append(_item.to_dict())
            _dict["telegram"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in apple_business_chat (list)
        _items = []
        if self.apple_business_chat:
            for _item in self.apple_business_chat:
                if _item:
                    _items.append(_item.to_dict())
            _dict["appleBusinessChat"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in webpush (list)
        _items = []
        if self.webpush:
            for _item in self.webpush:
                if _item:
                    _items.append(_item.to_dict())
            _dict["webpush"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in instagram_dm (list)
        _items = []
        if self.instagram_dm:
            for _item in self.instagram_dm:
                if _item:
                    _items.append(_item.to_dict())
            _dict["instagramDm"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in kakao_sangdam (list)
        _items = []
        if self.kakao_sangdam:
            for _item in self.kakao_sangdam:
                if _item:
                    _items.append(_item.to_dict())
            _dict["kakaoSangdam"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FlowPersonContacts from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "phone": [FlowPhoneContact.from_dict(_item) for _item in obj["phone"]]
                if obj.get("phone") is not None
                else None,
                "email": [FlowEmailContact.from_dict(_item) for _item in obj["email"]]
                if obj.get("email") is not None
                else None,
                "push": [FlowPushContact.from_dict(_item) for _item in obj["push"]]
                if obj.get("push") is not None
                else None,
                "facebook": [
                    FlowCommonOttContact.from_dict(_item) for _item in obj["facebook"]
                ]
                if obj.get("facebook") is not None
                else None,
                "line": [FlowCommonOttContact.from_dict(_item) for _item in obj["line"]]
                if obj.get("line") is not None
                else None,
                "viberBots": [
                    FlowCommonOttContact.from_dict(_item) for _item in obj["viberBots"]
                ]
                if obj.get("viberBots") is not None
                else None,
                "liveChat": [
                    FlowCommonOttContact.from_dict(_item) for _item in obj["liveChat"]
                ]
                if obj.get("liveChat") is not None
                else None,
                "instagram": [
                    FlowCommonOttContact.from_dict(_item) for _item in obj["instagram"]
                ]
                if obj.get("instagram") is not None
                else None,
                "telegram": [
                    FlowCommonOttContact.from_dict(_item) for _item in obj["telegram"]
                ]
                if obj.get("telegram") is not None
                else None,
                "appleBusinessChat": [
                    FlowCommonOttContact.from_dict(_item)
                    for _item in obj["appleBusinessChat"]
                ]
                if obj.get("appleBusinessChat") is not None
                else None,
                "webpush": [
                    FlowCommonPushContact.from_dict(_item) for _item in obj["webpush"]
                ]
                if obj.get("webpush") is not None
                else None,
                "instagramDm": [
                    FlowCommonOttContact.from_dict(_item)
                    for _item in obj["instagramDm"]
                ]
                if obj.get("instagramDm") is not None
                else None,
                "kakaoSangdam": [
                    FlowCommonOttContact.from_dict(_item)
                    for _item in obj["kakaoSangdam"]
                ]
                if obj.get("kakaoSangdam") is not None
                else None,
            }
        )
        return _obj