# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
"""


from datetime import datetime
from infobip.util.models import DefaultObject, serializable
from infobip.util.TimeUnit import TimeUnit
from infobip.api.model.omni.send.Language import Language


class SmsData(DefaultObject):
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
    @serializable(name="language", type=Language)
    def language(self):
        """
        Property is of type: Language
        """
        return self.get_field_value("language")

    @language.setter
    def language(self, language):
        """
        Property is of type: Language
        """
        self.set_field_value("language", language)

    def set_language(self, language):
        self.language = language
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