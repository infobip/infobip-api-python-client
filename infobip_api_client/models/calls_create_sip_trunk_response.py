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

from importlib import import_module
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from infobip_api_client.models.calls_billing_package import CallsBillingPackage
from infobip_api_client.models.calls_sbc_hosts import CallsSbcHosts
from infobip_api_client.models.calls_sip_trunk_type import CallsSipTrunkType
from typing import Optional, Set

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from infobip_api_client.models.calls_create_provider_sip_trunk_response import (
        CallsCreateProviderSipTrunkResponse,
    )
    from infobip_api_client.models.calls_create_registered_sip_trunk_response import (
        CallsCreateRegisteredSipTrunkResponse,
    )
    from infobip_api_client.models.calls_create_static_sip_trunk_response import (
        CallsCreateStaticSipTrunkResponse,
    )


class CallsCreateSipTrunkResponse(BaseModel):
    """
    CallsCreateSipTrunkResponse
    """  # noqa: E501

    id: Optional[StrictStr] = Field(default=None, description="SIP trunk ID.")
    type: Optional[CallsSipTrunkType] = None
    name: Optional[StrictStr] = Field(default=None, description="SIP trunk name.")
    location: Optional[StrictStr] = Field(
        default=None, description="SIP trunk location."
    )
    international_calls_allowed: Optional[StrictBool] = Field(
        default=None,
        description="Indicates whether international calls should be allowed. Calls between different countries are considered international.",
        alias="internationalCallsAllowed",
    )
    channel_limit: Optional[StrictInt] = Field(
        default=None,
        description="Maximum number of concurrent channels.",
        alias="channelLimit",
    )
    billing_package: Optional[CallsBillingPackage] = Field(
        default=None, alias="billingPackage"
    )
    sbc_hosts: Optional[CallsSbcHosts] = Field(default=None, alias="sbcHosts")
    __properties: ClassVar[List[str]] = [
        "id",
        "type",
        "name",
        "location",
        "internationalCallsAllowed",
        "channelLimit",
        "billingPackage",
        "sbcHosts",
    ]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    # JSON field name that stores the object type
    __discriminator_property_name: ClassVar[str] = "type"

    # discriminator mappings
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        "PROVIDER": "CallsCreateProviderSipTrunkResponse",
        "REGISTERED": "CallsCreateRegisteredSipTrunkResponse",
        "STATIC": "CallsCreateStaticSipTrunkResponse",
    }

    @classmethod
    def get_discriminator_value(cls, obj: Dict[str, Any]) -> Optional[str]:
        """Returns the discriminator value (object type) of the data"""
        discriminator_value = obj[cls.__discriminator_property_name]
        if discriminator_value:
            return cls.__discriminator_value_class_map.get(discriminator_value)
        else:
            return None

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(
        cls, json_str: str
    ) -> Optional[
        Union[
            CallsCreateProviderSipTrunkResponse,
            CallsCreateRegisteredSipTrunkResponse,
            CallsCreateStaticSipTrunkResponse,
        ]
    ]:
        """Create an instance of CallsCreateSipTrunkResponse from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(
        cls, obj: Dict[str, Any]
    ) -> Optional[
        Union[
            CallsCreateProviderSipTrunkResponse,
            CallsCreateRegisteredSipTrunkResponse,
            CallsCreateStaticSipTrunkResponse,
        ]
    ]:
        """Create an instance of CallsCreateSipTrunkResponse from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type == "CallsCreateProviderSipTrunkResponse":
            return import_module(
                "infobip_api_client.models.calls_create_provider_sip_trunk_response"
            ).CallsCreateProviderSipTrunkResponse.from_dict(obj)
        if object_type == "CallsCreateRegisteredSipTrunkResponse":
            return import_module(
                "infobip_api_client.models.calls_create_registered_sip_trunk_response"
            ).CallsCreateRegisteredSipTrunkResponse.from_dict(obj)
        if object_type == "CallsCreateStaticSipTrunkResponse":
            return import_module(
                "infobip_api_client.models.calls_create_static_sip_trunk_response"
            ).CallsCreateStaticSipTrunkResponse.from_dict(obj)

        raise ValueError(
            "CallsCreateSipTrunkResponse failed to lookup discriminator value from "
            + json.dumps(obj)
            + ". Discriminator property name: "
            + cls.__discriminator_property_name
            + ", mapping: "
            + json.dumps(cls.__discriminator_value_class_map)
        )
