# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
"""


from datetime import datetime
from infobip.util.models import DefaultObject, serializable
from infobip.util.TimeUnit import TimeUnit


class VKontakteData(DefaultObject):
    @property
    @serializable(name="templateName", type=str)
    def template_name(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("template_name")

    @template_name.setter
    def template_name(self, template_name):
        """
        Property is of type: unicode
        """
        self.set_field_value("template_name", template_name)

    def set_template_name(self, template_name):
        self.template_name = template_name
        return self

    @property
    @serializable(name="templateData", type=dict)
    def template_data(self):
        """
        Property is a dictionary with values of type: object
        """
        return self.get_field_value("template_data")

    @template_data.setter
    def template_data(self, template_data):
        """
        Property is a dictionary with values of type: object
        """
        self.set_field_value("template_data", template_data)

    def set_template_data(self, template_data):
        self.template_data = template_data
        return self

    @property
    @serializable(name="text", type=str)
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
    @serializable(name="validityPeriod", type=int)
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