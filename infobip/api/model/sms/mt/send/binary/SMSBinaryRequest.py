# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
"""


from datetime import datetime
from infobip.util.models import DefaultObject, serializable
from infobip.api.model.sms.mt.send.binary.BinaryContent import BinaryContent


class SMSBinaryRequest(DefaultObject):
    @property
    @serializable(name="from", type=str)
    def from_(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("from_")

    @from_.setter
    def from_(self, from_):
        """
        Property is of type: unicode
        """
        self.set_field_value("from_", from_)

    def set_from_(self, from_):
        self.from_ = from_
        return self

    @property
    @serializable(name="to", type=str)
    def to(self):
        """
        Property is a list of: unicode
        """
        return self.get_field_value("to")

    @to.setter
    def to(self, to):
        """
        Property is a list of: unicode
        """
        self.set_field_value("to", to)

    def set_to(self, to):
        self.to = to
        return self

    @property
    @serializable(name="binary", type=BinaryContent)
    def binary(self):
        """
        Property is of type: BinaryContent
        """
        return self.get_field_value("binary")

    @binary.setter
    def binary(self, binary):
        """
        Property is of type: BinaryContent
        """
        self.set_field_value("binary", binary)

    def set_binary(self, binary):
        self.binary = binary
        return self

    @property
    @serializable(name="campaignId", type=str)
    def campaign_id(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("campaign_id")

    @campaign_id.setter
    def campaign_id(self, campaign_id):
        """
        Property is of type: unicode
        """
        self.set_field_value("campaign_id", campaign_id)

    def set_campaign_id(self, campaign_id):
        self.campaign_id = campaign_id
        return self

    @property
    @serializable(name="operatorClientId", type=str)
    def operator_client_id(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("operator_client_id")

    @operator_client_id.setter
    def operator_client_id(self, operator_client_id):
        """
        Property is of type: unicode
        """
        self.set_field_value("operator_client_id", operator_client_id)

    def set_operator_client_id(self, operator_client_id):
        self.operator_client_id = operator_client_id
        return self