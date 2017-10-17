# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
"""


from datetime import datetime
from infobip.util.models import DefaultObject, serializable
class DeliveryTime(DefaultObject):
    @property
    @serializable(name="hour", type=int)
    def hour(self):
        return self.get_field_value("hour")

    @hour.setter
    def hour(self, hour):
        self.set_field_value("hour", hour)

    def set_hour(self, hour):
        self.hour = hour
        return self

    @property
    @serializable(name="minute", type=int)
    def minute(self):
        return self.get_field_value("minute")

    @minute.setter
    def minute(self, minute):
        self.set_field_value("minute", minute)

    def set_minute(self, minute):
        self.minute = minute
        return self