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
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self


class CallsDtmfOptions(BaseModel):
    """
    CallsDtmfOptions
    """  # noqa: E501

    max_input_length: Optional[Annotated[int, Field(le=255, strict=True)]] = Field(
        default=None,
        description="Maximum acceptable number of digits. Capturing is stopped after this number of digits has been entered. Max accepted value is 255. If not set, maximum value will be used.",
        alias="maxInputLength",
    )
    mapped_values: Optional[Dict[str, Any]] = Field(
        default=None,
        description='Map of expected collected DTMF values with some real meaning. (Example: if you have multilingual IVR, and option for users to press 1 to enter "English" menu, you can define {"1":"English"}, so the reporting and analysis will be easier). When this option is defined additional variable is present in the scenario. If you set your capture action variable name to myVar, then you will get additional variable myVar_Meaning containing the mapped value for a collected DTMF.',
        alias="mappedValues",
    )
    __properties: ClassVar[List[str]] = ["maxInputLength", "mappedValues"]

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
        """Create an instance of CallsDtmfOptions from a JSON string"""
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
        """Create an instance of CallsDtmfOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "maxInputLength": obj.get("maxInputLength"),
                "mappedValues": obj.get("mappedValues"),
            }
        )
        return _obj
