# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
"""


from datetime import datetime
from infobip.util.models import DefaultObject, serializable
from infobip.util.TimeUnit import TimeUnit
from infobip.api.model.omni.send.FacebookDataType import FacebookDataType


class FacebookData(DefaultObject):
    @property
    @serializable(name="type", type=FacebookDataType)
    def type(self):
        """
        Property is of type: FacebookDataType
        """
        return self.get_field_value("type")

    @type.setter
    def type(self, type):
        """
        Property is of type: FacebookDataType
        """
        self.set_field_value("type", type)

    def set_type(self, type):
        self.type = type
        return self

    @property
    @serializable(name="url", type=unicode)
    def url(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("url")

    @url.setter
    def url(self, url):
        """
        Property is of type: unicode
        """
        self.set_field_value("url", url)

    def set_url(self, url):
        self.url = url
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
    @serializable(name="validityPeriod", type=long)
    def validity_period(self):
        """
        Property is of type: long
        """
        return self.get_field_value("validity_period")

    @validity_period.setter
    def validity_period(self, validity_period):
        """
        Property is of type: long
        """
        self.set_field_value("validity_period", validity_period)

    def set_validity_period(self, validity_period):
        self.validity_period = validity_period
        return self

    @property
    @serializable(name="validityPeriodTimeUnit", type=TimeUnit)
    def validity_period_time_unit(self):
        """
        Property is of type: TimeUnit
        """
        return self.get_field_value("validity_period_time_unit")

    @validity_period_time_unit.setter
    def validity_period_time_unit(self, validity_period_time_unit):
        """
        Property is of type: TimeUnit
        """
        self.set_field_value("validity_period_time_unit", validity_period_time_unit)

    def set_validity_period_time_unit(self, validity_period_time_unit):
        self.validity_period_time_unit = validity_period_time_unit
        return self