# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
"""


from datetime import datetime
from infobip.util.models import DefaultObject, serializable
from infobip.util.TimeUnit import TimeUnit


class ViberData(DefaultObject):
    @property
    @serializable(name="imageURL", type=str)
    def image_u_r_l(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("image_u_r_l")

    @image_u_r_l.setter
    def image_u_r_l(self, image_u_r_l):
        """
        Property is of type: unicode
        """
        self.set_field_value("image_u_r_l", image_u_r_l)

    def set_image_u_r_l(self, image_u_r_l):
        self.image_u_r_l = image_u_r_l
        return self

    @property
    @serializable(name="buttonText", type=str)
    def button_text(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("button_text")

    @button_text.setter
    def button_text(self, button_text):
        """
        Property is of type: unicode
        """
        self.set_field_value("button_text", button_text)

    def set_button_text(self, button_text):
        self.button_text = button_text
        return self

    @property
    @serializable(name="buttonURL", type=str)
    def button_u_r_l(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("button_u_r_l")

    @button_u_r_l.setter
    def button_u_r_l(self, button_u_r_l):
        """
        Property is of type: unicode
        """
        self.set_field_value("button_u_r_l", button_u_r_l)

    def set_button_u_r_l(self, button_u_r_l):
        self.button_u_r_l = button_u_r_l
        return self

    @property
    @serializable(name="isPromotional", type=bool)
    def is_promotional(self):
        """
        Property is of type: bool
        """
        return self.get_field_value("is_promotional")

    @is_promotional.setter
    def is_promotional(self, is_promotional):
        """
        Property is of type: bool
        """
        self.set_field_value("is_promotional", is_promotional)

    def set_is_promotional(self, is_promotional):
        self.is_promotional = is_promotional
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