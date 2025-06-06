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
from typing import Optional, Set
from typing_extensions import Self


class EmailValidationResponse(BaseModel):
    """
    EmailValidationResponse
    """  # noqa: E501

    to: Optional[StrictStr] = Field(
        default=None, description="Email address of the recipient."
    )
    valid_mailbox: Optional[StrictStr] = Field(
        default=None,
        description="Represents status of recipient email address.",
        alias="validMailbox",
    )
    valid_syntax: Optional[StrictBool] = Field(
        default=None,
        description="Represents syntax of recipient email address.",
        alias="validSyntax",
    )
    catch_all: Optional[StrictBool] = Field(
        default=None,
        description="Denotes catch all status of recipient email address.",
        alias="catchAll",
    )
    did_you_mean: Optional[StrictStr] = Field(
        default=None,
        description="Suggests alternate addresses that maybe valid.",
        alias="didYouMean",
    )
    disposable: Optional[StrictBool] = None
    role_based: Optional[StrictBool] = Field(default=None, alias="roleBased")
    reason: Optional[StrictStr] = Field(
        default=None,
        description="Reason is provided when validMailbox status is unknown. 1. INBOX_FULL - The user quota exceeded / The user inbox is full / The user doesn't accept any more requests.  2. UNEXPECTED_FAILURE - The mail Server returned a temporary error. 3. THROTTLED - The mail server is not allowing us momentarily because of too many requests. 4. TIMED_OUT - The Mail Server took a longer time to respond / there was a delay in the network. 5. TEMP_REJECTION - Mail server temporarily rejected. 6. UNABLE_TO_CONNECT - Unable to connect to the Mail Server.",
    )
    detailed_reasons: Optional[StrictStr] = Field(
        default=None,
        description="Is provided when validMailbox is 'unknown' or 'false' and lists reasons clarifying why validMailbox has that status.",
        alias="detailedReasons",
    )
    risk: Optional[StrictStr] = Field(
        default=None,
        description="Returns one of the following values: 'High', 'Medium', 'Low' or 'Unknown'. High risk addresses have very high chances of bouncing (and potentially damaging the sender's reputation), whereas low risk addresses have very low chances of bouncing and damaging the sender's reputation.",
    )
    __properties: ClassVar[List[str]] = [
        "to",
        "validMailbox",
        "validSyntax",
        "catchAll",
        "didYouMean",
        "disposable",
        "roleBased",
        "reason",
        "detailedReasons",
        "risk",
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
        """Create an instance of EmailValidationResponse from a JSON string"""
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
        """Create an instance of EmailValidationResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "to": obj.get("to"),
                "validMailbox": obj.get("validMailbox"),
                "validSyntax": obj.get("validSyntax"),
                "catchAll": obj.get("catchAll"),
                "didYouMean": obj.get("didYouMean"),
                "disposable": obj.get("disposable"),
                "roleBased": obj.get("roleBased"),
                "reason": obj.get("reason"),
                "detailedReasons": obj.get("detailedReasons"),
                "risk": obj.get("risk"),
            }
        )
        return _obj
