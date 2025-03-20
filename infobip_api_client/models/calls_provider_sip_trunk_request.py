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

from pydantic import ConfigDict
from typing import Any, ClassVar, Dict, List
from infobip_api_client.models.calls_billing_package import CallsBillingPackage
from infobip_api_client.models.calls_provider import CallsProvider
from infobip_api_client.models.calls_sip_trunk_request import CallsSipTrunkRequest
from typing import Optional, Set
from typing_extensions import Self


class CallsProviderSipTrunkRequest(CallsSipTrunkRequest):
    """
    CallsProviderSipTrunkRequest
    """  # noqa: E501

    provider: CallsProvider
    __properties: ClassVar[List[str]] = [
        "type",
        "name",
        "location",
        "tls",
        "internationalCallsAllowed",
        "channelLimit",
        "billingPackage",
        "provider",
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
        """Create an instance of CallsProviderSipTrunkRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of billing_package
        if self.billing_package:
            _dict["billingPackage"] = self.billing_package.to_dict()
        # override the default output from pydantic by calling `to_dict()` of provider
        if self.provider:
            _dict["provider"] = self.provider.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CallsProviderSipTrunkRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "type": obj.get("type"),
                "name": obj.get("name"),
                "location": obj.get("location"),
                "tls": obj.get("tls") if obj.get("tls") is not None else False,
                "internationalCallsAllowed": obj.get("internationalCallsAllowed")
                if obj.get("internationalCallsAllowed") is not None
                else False,
                "channelLimit": obj.get("channelLimit"),
                "billingPackage": CallsBillingPackage.from_dict(obj["billingPackage"])
                if obj.get("billingPackage") is not None
                else None,
                "provider": CallsProvider.from_dict(obj["provider"])
                if obj.get("provider") is not None
                else None,
            }
        )
        return _obj
