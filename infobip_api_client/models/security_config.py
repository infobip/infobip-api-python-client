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
from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional, Union
from infobip_api_client.models.url_security_config_type import UrlSecurityConfigType
from typing import Optional, Set
from typing_extensions import Self

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from infobip_api_client.models.basic_security_config import BasicSecurityConfig
    from infobip_api_client.models.hmac_security_config import HmacSecurityConfig


class SecurityConfig(BaseModel):
    """
    Webhook security config.
    """  # noqa: E501

    type: Optional[UrlSecurityConfigType] = None
    __properties: ClassVar[List[str]] = ["type"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    # JSON field name that stores the object type
    __discriminator_property_name: ClassVar[str] = "type"

    # discriminator mappings
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        "BASIC": "BasicSecurityConfig",
        "HMAC": "HmacSecurityConfig",
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
    ) -> Optional[Union[BasicSecurityConfig, HmacSecurityConfig]]:
        """Create an instance of SecurityConfig from a JSON string"""
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
    def from_dict(
        cls, obj: Dict[str, Any]
    ) -> Optional[Union[BasicSecurityConfig, HmacSecurityConfig]]:
        """Create an instance of SecurityConfig from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type == "BasicSecurityConfig":
            return import_module(
                "infobip_api_client.models.basic_security_config"
            ).BasicSecurityConfig.from_dict(obj)
        if object_type == "HmacSecurityConfig":
            return import_module(
                "infobip_api_client.models.hmac_security_config"
            ).HmacSecurityConfig.from_dict(obj)

        raise ValueError(
            "SecurityConfig failed to lookup discriminator value from "
            + json.dumps(obj)
            + ". Discriminator property name: "
            + cls.__discriminator_property_name
            + ", mapping: "
            + json.dumps(cls.__discriminator_value_class_map)
        )
