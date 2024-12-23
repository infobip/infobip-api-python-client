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

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    StrictBool,
    StrictFloat,
    StrictInt,
    StrictStr,
)
from typing import Any, ClassVar, Dict, List, Optional, Union
from infobip_api_client.models.number_masking_recording_status import (
    NumberMaskingRecordingStatus,
)
from typing import Optional, Set
from typing_extensions import Self


class NumberMaskingStatusRequest(BaseModel):
    """
    Status request.
    """  # noqa: E501

    action: Optional[StrictStr] = Field(
        default=None, description="Requested action (dial, audio, captureDtmf)."
    )
    var_from: Optional[StrictStr] = Field(
        default=None, description="Caller phone number.", alias="from"
    )
    to: Optional[StrictStr] = Field(default=None, description="Called phone number.")
    transfer_to: Optional[StrictStr] = Field(
        default=None,
        description="Called party phone number that the call is transferred to.",
        alias="transferTo",
    )
    duration: Optional[StrictInt] = Field(
        default=None, description="Duration of the outbound call shown in seconds"
    )
    status: Optional[StrictStr] = Field(
        default=None,
        description="Call status which can be: answered, busy, no answer, failed or congestion",
    )
    nm_correlation_id: Optional[StrictStr] = Field(
        default=None,
        description="Unique identifier for correlation with inbound call, available in Callback and Status requests.",
        alias="nmCorrelationId",
    )
    file_id: Optional[StrictStr] = Field(
        default=None,
        description="Identifier of the file played to the caller.",
        alias="fileID",
    )
    file_url: Optional[StrictStr] = Field(
        default=None,
        description="The URL of the file played to the caller.",
        alias="fileUrl",
    )
    ringing_time: Optional[StrictStr] = Field(
        default=None,
        description="Date and time when ringing started.",
        alias="ringingTime",
    )
    answered_time: Optional[StrictStr] = Field(
        default=None,
        description="Date and time when the call was answered.",
        alias="answeredTime",
    )
    correlation_id: Optional[StrictStr] = Field(
        default=None,
        description="Unique identifier of the call record, available for both Callback and Status requests.",
        alias="correlationId",
    )
    inbound_duration: Optional[StrictInt] = Field(
        default=None,
        description="Duration of the inbound call shown in seconds.",
        alias="inboundDuration",
    )
    calculated_duration: Optional[StrictInt] = Field(
        default=None,
        description="The duration of the outbound part of the number masking session, where the voice billing model (1/1, 15/15,...) has been applied to the calculatedDuration.",
        alias="calculatedDuration",
    )
    price_per_second: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None,
        description="This is the price per second for the outbound part of the number masking session, with the price being expressed in cents per second.",
        alias="pricePerSecond",
    )
    currency: Optional[StrictStr] = Field(
        default=None, description="The currency in which the price is expressed."
    )
    recording_file_id: Optional[StrictStr] = Field(
        default=None,
        description="ID of a recording file of a call.",
        alias="recordingFileId",
    )
    record_callee_announcement: Optional[StrictBool] = Field(
        default=None,
        description="Flag that indicates if callee announcement is included in recording file.",
        alias="recordCalleeAnnouncement",
    )
    recording_status: Optional[NumberMaskingRecordingStatus] = Field(
        default=None, alias="recordingStatus"
    )
    client_reference_id: Optional[StrictStr] = Field(
        default=None,
        description="Client-defined ID of a valid file name. Used to correlate a call with this reference. If recording is enabled and files are stored in the SFTP server, that ID will be used as a file name instead.",
        alias="clientReferenceId",
    )
    __properties: ClassVar[List[str]] = [
        "action",
        "from",
        "to",
        "transferTo",
        "duration",
        "status",
        "nmCorrelationId",
        "fileID",
        "fileUrl",
        "ringingTime",
        "answeredTime",
        "correlationId",
        "inboundDuration",
        "calculatedDuration",
        "pricePerSecond",
        "currency",
        "recordingFileId",
        "recordCalleeAnnouncement",
        "recordingStatus",
        "clientReferenceId",
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
        """Create an instance of NumberMaskingStatusRequest from a JSON string"""
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
        """Create an instance of NumberMaskingStatusRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "action": obj.get("action"),
                "from": obj.get("from"),
                "to": obj.get("to"),
                "transferTo": obj.get("transferTo"),
                "duration": obj.get("duration"),
                "status": obj.get("status"),
                "nmCorrelationId": obj.get("nmCorrelationId"),
                "fileID": obj.get("fileID"),
                "fileUrl": obj.get("fileUrl"),
                "ringingTime": obj.get("ringingTime"),
                "answeredTime": obj.get("answeredTime"),
                "correlationId": obj.get("correlationId"),
                "inboundDuration": obj.get("inboundDuration"),
                "calculatedDuration": obj.get("calculatedDuration"),
                "pricePerSecond": obj.get("pricePerSecond"),
                "currency": obj.get("currency"),
                "recordingFileId": obj.get("recordingFileId"),
                "recordCalleeAnnouncement": obj.get("recordCalleeAnnouncement"),
                "recordingStatus": obj.get("recordingStatus"),
                "clientReferenceId": obj.get("clientReferenceId"),
            }
        )
        return _obj
