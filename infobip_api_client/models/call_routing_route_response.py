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
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from infobip_api_client.models.call_routing_destination import CallRoutingDestination
from infobip_api_client.models.call_routing_search_criteria import (
    CallRoutingSearchCriteria,
)
from typing import Optional, Set
from typing_extensions import Self


class CallRoutingRouteResponse(BaseModel):
    """
    Route response object.
    """  # noqa: E501

    id: StrictStr = Field(description="Unique identifier of a route.")
    name: StrictStr = Field(description="Route name.")
    criteria: Optional[List[CallRoutingSearchCriteria]] = Field(
        default=None,
        description="List of criteria that should match route. For a route to match, any criterion should be met.",
    )
    destinations: Annotated[
        List[CallRoutingDestination], Field(min_length=1, max_length=10)
    ] = Field(
        description="List of destinations. First destination in the list is the first one to be executed. Subsequent destinations are executed only if the previous one fails."
    )
    __properties: ClassVar[List[str]] = ["id", "name", "criteria", "destinations"]

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
        """Create an instance of CallRoutingRouteResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in criteria (list)
        _items = []
        if self.criteria:
            for _item in self.criteria:
                if _item:
                    _items.append(_item.to_dict())
            _dict["criteria"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in destinations (list)
        _items = []
        if self.destinations:
            for _item in self.destinations:
                if _item:
                    _items.append(_item.to_dict())
            _dict["destinations"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CallRoutingRouteResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "id": obj.get("id"),
                "name": obj.get("name"),
                "criteria": [
                    CallRoutingSearchCriteria.from_dict(_item)
                    for _item in obj["criteria"]
                ]
                if obj.get("criteria") is not None
                else None,
                "destinations": [
                    CallRoutingDestination.from_dict(_item)
                    for _item in obj["destinations"]
                ]
                if obj.get("destinations") is not None
                else None,
            }
        )
        return _obj
