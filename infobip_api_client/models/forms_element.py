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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from infobip_api_client.models.forms_component_type import FormsComponentType
from infobip_api_client.models.forms_element_option import FormsElementOption
from infobip_api_client.models.forms_validation_rules import FormsValidationRules
from typing import Optional, Set
from typing_extensions import Self


class FormsElement(BaseModel):
    """
    List of form fields
    """  # noqa: E501

    component: FormsComponentType
    field_id: Optional[StrictStr] = Field(default=None, alias="fieldId")
    person_field: Optional[StrictStr] = Field(default=None, alias="personField")
    label: Optional[StrictStr] = None
    is_required: Optional[StrictBool] = Field(default=None, alias="isRequired")
    is_hidden: Optional[StrictBool] = Field(default=None, alias="isHidden")
    additional_configuration: Optional[Dict[str, StrictStr]] = Field(
        default=None, alias="additionalConfiguration"
    )
    text_content: Optional[StrictStr] = Field(default=None, alias="textContent")
    options: Optional[List[FormsElementOption]] = None
    validation_rules: Optional[FormsValidationRules] = Field(
        default=None, alias="validationRules"
    )
    placeholder: Optional[StrictStr] = None
    checkbox_text: Optional[StrictStr] = Field(default=None, alias="checkboxText")
    validation_messages: Optional[Dict[str, StrictStr]] = Field(
        default=None, alias="validationMessages"
    )
    __properties: ClassVar[List[str]] = [
        "component",
        "fieldId",
        "personField",
        "label",
        "isRequired",
        "isHidden",
        "additionalConfiguration",
        "textContent",
        "options",
        "validationRules",
        "placeholder",
        "checkboxText",
        "validationMessages",
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
        """Create an instance of FormsElement from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in options (list)
        _items = []
        if self.options:
            for _item in self.options:
                if _item:
                    _items.append(_item.to_dict())
            _dict["options"] = _items
        # override the default output from pydantic by calling `to_dict()` of validation_rules
        if self.validation_rules:
            _dict["validationRules"] = self.validation_rules.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FormsElement from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "component": obj.get("component"),
                "fieldId": obj.get("fieldId"),
                "personField": obj.get("personField"),
                "label": obj.get("label"),
                "isRequired": obj.get("isRequired"),
                "isHidden": obj.get("isHidden"),
                "additionalConfiguration": obj.get("additionalConfiguration"),
                "textContent": obj.get("textContent"),
                "options": [
                    FormsElementOption.from_dict(_item) for _item in obj["options"]
                ]
                if obj.get("options") is not None
                else None,
                "validationRules": FormsValidationRules.from_dict(
                    obj["validationRules"]
                )
                if obj.get("validationRules") is not None
                else None,
                "placeholder": obj.get("placeholder"),
                "checkboxText": obj.get("checkboxText"),
                "validationMessages": obj.get("validationMessages"),
            }
        )
        return _obj
