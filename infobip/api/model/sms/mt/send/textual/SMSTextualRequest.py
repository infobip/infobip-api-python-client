# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
"""


from datetime import datetime
from infobip.util.models import DefaultObject, serializable
from infobip.api.model.sms.mt.send.RegionalOptions import RegionalOptions


class SMSTextualRequest(DefaultObject):
    @property
    @serializable(name="from", type=unicode)
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
    @serializable(name="to", type=unicode)
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
    @serializable(name="text", type=unicode)
    def text(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("text")

    @text.setter
    def text(self, text):
        """
        Property is of type: unicode
        """
        self.set_field_value("text", text)

    def set_text(self, text):
        self.text = text
        return self

    @property
    @serializable(name="campaignId", type=unicode)
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
    @serializable(name="operatorClientId", type=unicode)
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

    @property
    @serializable(name="transliteration", type=unicode)
    def transliteration(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("transliteration")

    @transliteration.setter
    def transliteration(self, transliteration):
        """
        Property is of type: unicode
        """
        self.set_field_value("transliteration", transliteration)

    def set_transliteration(self, transliteration):
        self.transliteration = transliteration
        return self
    @property
    @serializable(name="regional", type=RegionalOptions)
    def regional(self):
        """
        Property is of type: RegionalOptions
        """
        return self.get_field_value("regional")

    @regional.setter
    def regional(self, regional):
        """
        Property is of type: RegionalOptions
        """
        self.set_field_value("regional", regional)

    def set_regional(self, regional):
        self.regional = regional
        return self