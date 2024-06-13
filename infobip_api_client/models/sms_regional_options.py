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
from infobip_api_client.models.sms_india_dlt_options import SmsIndiaDltOptions
from infobip_api_client.models.sms_south_korea_options import SmsSouthKoreaOptions
from infobip_api_client.models.sms_turkey_iys_options import SmsTurkeyIysOptions
from typing import Optional, Set
from typing_extensions import Self


class SmsRegionalOptions(BaseModel):
    """
    Region-specific parameters, often imposed by local laws. Use this, if country or region that you are sending an SMS to requires additional information.
    """  # noqa: E501

    india_dlt: Optional[SmsIndiaDltOptions] = Field(default=None, alias="indiaDlt")
    turkey_iys: Optional[SmsTurkeyIysOptions] = Field(default=None, alias="turkeyIys")
    south_korea: Optional[SmsSouthKoreaOptions] = Field(
        default=None, alias="southKorea"
    )
    __properties: ClassVar[List[str]] = ["indiaDlt", "turkeyIys", "southKorea"]

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
        """Create an instance of SmsRegionalOptions from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of india_dlt
        if self.india_dlt:
            _dict["indiaDlt"] = self.india_dlt.to_dict()
        # override the default output from pydantic by calling `to_dict()` of turkey_iys
        if self.turkey_iys:
            _dict["turkeyIys"] = self.turkey_iys.to_dict()
        # override the default output from pydantic by calling `to_dict()` of south_korea
        if self.south_korea:
            _dict["southKorea"] = self.south_korea.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SmsRegionalOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "indiaDlt": SmsIndiaDltOptions.from_dict(obj["indiaDlt"])
                if obj.get("indiaDlt") is not None
                else None,
                "turkeyIys": SmsTurkeyIysOptions.from_dict(obj["turkeyIys"])
                if obj.get("turkeyIys") is not None
                else None,
                "southKorea": SmsSouthKoreaOptions.from_dict(obj["southKorea"])
                if obj.get("southKorea") is not None
                else None,
            }
        )
        return _obj
