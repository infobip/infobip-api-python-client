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
from typing import Optional, Set
from typing_extensions import Self


class FormsValidationRules(BaseModel):
    """
    FormsValidationRules
    """  # noqa: E501

    date_pattern: Optional[StrictStr] = Field(default=None, alias="datePattern")
    max_length: Optional[StrictInt] = Field(default=None, alias="maxLength")
    max_value: Optional[StrictStr] = Field(default=None, alias="maxValue")
    min_value: Optional[StrictStr] = Field(default=None, alias="minValue")
    pattern: Optional[StrictStr] = None
    sample: Optional[StrictStr] = None
    forbidden_symbols: Optional[List[StrictStr]] = Field(
        default=None, alias="forbiddenSymbols"
    )
    __properties: ClassVar[List[str]] = [
        "datePattern",
        "maxLength",
        "maxValue",
        "minValue",
        "pattern",
        "sample",
        "forbiddenSymbols",
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
        """Create an instance of FormsValidationRules from a JSON string"""
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
        """Create an instance of FormsValidationRules from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "datePattern": obj.get("datePattern"),
                "maxLength": obj.get("maxLength"),
                "maxValue": obj.get("maxValue"),
                "minValue": obj.get("minValue"),
                "pattern": obj.get("pattern"),
                "sample": obj.get("sample"),
                "forbiddenSymbols": obj.get("forbiddenSymbols"),
            }
        )
        return _obj
