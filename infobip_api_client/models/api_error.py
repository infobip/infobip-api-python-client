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
from typing import Any, ClassVar, Dict, List
from infobip_api_client.models.api_error_resource import ApiErrorResource
from infobip_api_client.models.api_error_violation import ApiErrorViolation
from typing import Optional, Set
from typing_extensions import Self


class ApiError(BaseModel):
    """
    ApiError
    """  # noqa: E501

    error_code: StrictStr = Field(
        description="An error code uniquely identifying the error case.",
        alias="errorCode",
    )
    description: StrictStr = Field(description="A detailed description of an error.")
    action: StrictStr = Field(
        description="An action that should be taken to recover from the error."
    )
    violations: List[ApiErrorViolation] = Field(
        description="List of violations that caused the error."
    )
    resources: List[ApiErrorResource] = Field(
        description="List of available resources to recover from the error."
    )
    __properties: ClassVar[List[str]] = [
        "errorCode",
        "description",
        "action",
        "violations",
        "resources",
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
        """Create an instance of ApiError from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in violations (list)
        _items = []
        if self.violations:
            for _item in self.violations:
                if _item:
                    _items.append(_item.to_dict())
            _dict["violations"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in resources (list)
        _items = []
        if self.resources:
            for _item in self.resources:
                if _item:
                    _items.append(_item.to_dict())
            _dict["resources"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApiError from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "errorCode": obj.get("errorCode"),
                "description": obj.get("description"),
                "action": obj.get("action"),
                "violations": [
                    ApiErrorViolation.from_dict(_item) for _item in obj["violations"]
                ]
                if obj.get("violations") is not None
                else None,
                "resources": [
                    ApiErrorResource.from_dict(_item) for _item in obj["resources"]
                ]
                if obj.get("resources") is not None
                else None,
            }
        )
        return _obj
