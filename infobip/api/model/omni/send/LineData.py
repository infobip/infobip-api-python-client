# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
"""


from datetime import datetime
from infobip.util.models import DefaultObject, serializable
from infobip.util.TimeUnit import TimeUnit
from infobip.api.model.omni.send.LineDataType import LineDataType


class LineData(DefaultObject):
    @property
    @serializable(name="type", type=LineDataType)
    def type(self):
        """
        Property is of type: LineDataType
        """
        return self.get_field_value("type")

    @type.setter
    def type(self, type):
        """
        Property is of type: LineDataType
        """
        self.set_field_value("type", type)

    def set_type(self, type):
        self.type = type
        return self

    @property
    @serializable(name="url", type=str)
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
    @serializable(name="thumbnailUrl", type=str)
    def thumbnail_url(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("thumbnail_url")

    @thumbnail_url.setter
    def thumbnail_url(self, thumbnail_url):
        """
        Property is of type: unicode
        """
        self.set_field_value("thumbnail_url", thumbnail_url)

    def set_thumbnail_url(self, thumbnail_url):
        self.thumbnail_url = thumbnail_url
        return self

    @property
    @serializable(name="duration", type=str)
    def duration(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("duration")

    @duration.setter
    def duration(self, duration):
        """
        Property is of type: unicode
        """
        self.set_field_value("duration", duration)

    def set_duration(self, duration):
        self.duration = duration
        return self

    @property
    @serializable(name="packageId", type=str)
    def package_id(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("package_id")

    @package_id.setter
    def package_id(self, package_id):
        """
        Property is of type: unicode
        """
        self.set_field_value("package_id", package_id)

    def set_package_id(self, package_id):
        self.package_id = package_id
        return self

    @property
    @serializable(name="stickerId", type=str)
    def sticker_id(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("sticker_id")

    @sticker_id.setter
    def sticker_id(self, sticker_id):
        """
        Property is of type: unicode
        """
        self.set_field_value("sticker_id", sticker_id)

    def set_sticker_id(self, sticker_id):
        self.sticker_id = sticker_id
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