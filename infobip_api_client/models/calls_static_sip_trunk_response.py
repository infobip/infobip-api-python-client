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

from pydantic import ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from infobip_api_client.models.calls_anonymization_type import CallsAnonymizationType
from infobip_api_client.models.calls_audio_codec import CallsAudioCodec
from infobip_api_client.models.calls_billing_package import CallsBillingPackage
from infobip_api_client.models.calls_dtmf_type import CallsDtmfType
from infobip_api_client.models.calls_fax_type import CallsFaxType
from infobip_api_client.models.calls_number_presentation_format import (
    CallsNumberPresentationFormat,
)
from infobip_api_client.models.calls_sbc_hosts import CallsSbcHosts
from infobip_api_client.models.calls_selection_strategy import CallsSelectionStrategy
from infobip_api_client.models.calls_sip_options import CallsSipOptions
from infobip_api_client.models.calls_sip_trunk_location import CallsSipTrunkLocation
from infobip_api_client.models.calls_sip_trunk_response import CallsSipTrunkResponse
from infobip_api_client.models.calls_sip_trunk_type import CallsSipTrunkType
from typing import Optional, Set
from typing_extensions import Self


class CallsStaticSipTrunkResponse(CallsSipTrunkResponse):
    """
    CallsStaticSipTrunkResponse
    """  # noqa: E501

    source_hosts: Optional[List[StrictStr]] = Field(
        default=None, description="List of source hosts.", alias="sourceHosts"
    )
    destination_hosts: Optional[List[StrictStr]] = Field(
        default=None, description="List of destination hosts.", alias="destinationHosts"
    )
    strategy: Optional[CallsSelectionStrategy] = None
    __properties: ClassVar[List[str]] = [
        "id",
        "type",
        "name",
        "location",
        "tls",
        "codecs",
        "dtmf",
        "fax",
        "numberFormat",
        "internationalCallsAllowed",
        "channelLimit",
        "anonymization",
        "billingPackage",
        "sbcHosts",
        "sipOptions",
        "sourceHosts",
        "destinationHosts",
        "strategy",
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
        """Create an instance of CallsStaticSipTrunkResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of sbc_hosts
        if self.sbc_hosts:
            _dict["sbcHosts"] = self.sbc_hosts.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sip_options
        if self.sip_options:
            _dict["sipOptions"] = self.sip_options.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CallsStaticSipTrunkResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "id": obj.get("id"),
                "type": obj.get("type"),
                "name": obj.get("name"),
                "location": obj.get("location"),
                "tls": obj.get("tls"),
                "codecs": obj.get("codecs"),
                "dtmf": obj.get("dtmf"),
                "fax": obj.get("fax"),
                "numberFormat": obj.get("numberFormat"),
                "internationalCallsAllowed": obj.get("internationalCallsAllowed"),
                "channelLimit": obj.get("channelLimit"),
                "anonymization": obj.get("anonymization"),
                "billingPackage": CallsBillingPackage.from_dict(obj["billingPackage"])
                if obj.get("billingPackage") is not None
                else None,
                "sbcHosts": CallsSbcHosts.from_dict(obj["sbcHosts"])
                if obj.get("sbcHosts") is not None
                else None,
                "sipOptions": CallsSipOptions.from_dict(obj["sipOptions"])
                if obj.get("sipOptions") is not None
                else None,
                "sourceHosts": obj.get("sourceHosts"),
                "destinationHosts": obj.get("destinationHosts"),
                "strategy": obj.get("strategy"),
            }
        )
        return _obj
