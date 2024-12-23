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
from infobip_api_client.models.flow_add_flow_participant_result import (
    FlowAddFlowParticipantResult,
)
from typing import Optional, Set
from typing_extensions import Self


class FlowParticipantsReportResponse(BaseModel):
    """
    Summary of processing status for participants in a given operation.
    """  # noqa: E501

    operation_id: StrictStr = Field(
        description="Unique identifier of the operation.", alias="operationId"
    )
    campaign_id: StrictInt = Field(
        description="Unique identifier of the flow campaign.", alias="campaignId"
    )
    callback_data: Optional[StrictStr] = Field(
        default=None,
        description="Additional data will be passed in the request to your callback server along with the operation results report.",
        alias="callbackData",
    )
    participants: List[FlowAddFlowParticipantResult] = Field(
        description="Array with information about each participant submitted for the operation."
    )
    __properties: ClassVar[List[str]] = [
        "operationId",
        "campaignId",
        "callbackData",
        "participants",
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
        """Create an instance of FlowParticipantsReportResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in participants (list)
        _items = []
        if self.participants:
            for _item in self.participants:
                if _item:
                    _items.append(_item.to_dict())
            _dict["participants"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FlowParticipantsReportResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "operationId": obj.get("operationId"),
                "campaignId": obj.get("campaignId"),
                "callbackData": obj.get("callbackData"),
                "participants": [
                    FlowAddFlowParticipantResult.from_dict(_item)
                    for _item in obj["participants"]
                ]
                if obj.get("participants") is not None
                else None,
            }
        )
        return _obj
