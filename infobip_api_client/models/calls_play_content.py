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
from infobip_api_client.models.calls_play_content_type import CallsPlayContentType
from typing import Optional, Set
from typing_extensions import Self

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from infobip_api_client.models.calls_file_play_content import CallsFilePlayContent
    from infobip_api_client.models.calls_recording_play_content import (
        CallsRecordingPlayContent,
    )
    from infobip_api_client.models.calls_text_play_content import CallsTextPlayContent
    from infobip_api_client.models.calls_url_play_content import CallsUrlPlayContent


class CallsPlayContent(BaseModel):
    """
    Audio content to play. It can either be previously uploaded file or a file from a URL.
    """  # noqa: E501

    type: Optional[CallsPlayContentType] = None
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
        "FILE": "CallsFilePlayContent",
        "RECORDING": "CallsRecordingPlayContent",
        "TEXT": "CallsTextPlayContent",
        "URL": "CallsUrlPlayContent",
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
            CallsFilePlayContent,
            CallsRecordingPlayContent,
            CallsTextPlayContent,
            CallsUrlPlayContent,
        ]
    ]:
        """Create an instance of CallsPlayContent from a JSON string"""
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
    ) -> Optional[
        Union[
            CallsFilePlayContent,
            CallsRecordingPlayContent,
            CallsTextPlayContent,
            CallsUrlPlayContent,
        ]
    ]:
        """Create an instance of CallsPlayContent from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type == "CallsFilePlayContent":
            return import_module(
                "infobip_api_client.models.calls_file_play_content"
            ).CallsFilePlayContent.from_dict(obj)
        if object_type == "CallsRecordingPlayContent":
            return import_module(
                "infobip_api_client.models.calls_recording_play_content"
            ).CallsRecordingPlayContent.from_dict(obj)
        if object_type == "CallsTextPlayContent":
            return import_module(
                "infobip_api_client.models.calls_text_play_content"
            ).CallsTextPlayContent.from_dict(obj)
        if object_type == "CallsUrlPlayContent":
            return import_module(
                "infobip_api_client.models.calls_url_play_content"
            ).CallsUrlPlayContent.from_dict(obj)

        raise ValueError(
            "CallsPlayContent failed to lookup discriminator value from "
            + json.dumps(obj)
            + ". Discriminator property name: "
            + cls.__discriminator_property_name
            + ", mapping: "
            + json.dumps(cls.__discriminator_value_class_map)
        )
