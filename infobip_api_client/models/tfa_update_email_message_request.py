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
from infobip_api_client.models.tfa_pin_type import TfaPinType
from typing import Optional, Set
from typing_extensions import Self


class TfaUpdateEmailMessageRequest(BaseModel):
    """
    TfaUpdateEmailMessageRequest
    """  # noqa: E501

    email_template_id: Optional[StrictInt] = Field(
        default=None,
        description="Email template ID that should reference a previously created Email template.",
        alias="emailTemplateId",
    )
    var_from: Optional[StrictStr] = Field(
        default=None,
        description="The sender of the 2FA message, an email address with an optional sender name (e.g. `company@example.com` or `Jane Smith <jane.smith@somecompany.com>`).",
        alias="from",
    )
    pin_length: Optional[StrictInt] = Field(
        default=None, description="PIN code length.", alias="pinLength"
    )
    pin_type: Optional[TfaPinType] = Field(default=None, alias="pinType")
    __properties: ClassVar[List[str]] = [
        "emailTemplateId",
        "from",
        "pinLength",
        "pinType",
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
        """Create an instance of TfaUpdateEmailMessageRequest from a JSON string"""
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
        """Create an instance of TfaUpdateEmailMessageRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "emailTemplateId": obj.get("emailTemplateId"),
                "from": obj.get("from"),
                "pinLength": obj.get("pinLength"),
                "pinType": obj.get("pinType"),
            }
        )
        return _obj
