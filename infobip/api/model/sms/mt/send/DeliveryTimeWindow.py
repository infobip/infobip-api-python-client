# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
"""


from datetime import datetime
from infobip.util.models import DefaultObject, serializable
from infobip.api.model.sms.mt.send.DeliveryDay import DeliveryDay
from infobip.api.model.sms.mt.send.DeliveryTime import DeliveryTime

class DeliveryTimeWindow(DefaultObject):
    @property
    @serializable(name="from", type=DeliveryTime)
    def from_(self):
        return self.get_field_value("from_")

    @from_.setter
    def from_(self, from_):
        self.set_field_value("from_", from_)

    def set_from_(self, from_):
        self.from_ = from_
        return self

    @property
    @serializable(name="days", type=DeliveryDay, list=True)
    def days(self):
        return self.get_field_value("days")

    @days.setter
    def days(self, days):
        self.set_field_value("days", days)

    def set_days(self, days):
        self.days = days
        return self

    def add_days(self, *days):
        if not self.days:
            self.days = []

        self.days.extend(days)
        return self

    def remove_days(self, *days):
        if not self.days:
            return self

        for i in days:
            self.days.remove(i)

        return self

    @property
    @serializable(name="to", type=DeliveryTime)
    def to(self):
        return self.get_field_value("to")

    @to.setter
    def to(self, to):
        self.set_field_value("to", to)

    def set_to(self, to):
        self.to = to
        return self