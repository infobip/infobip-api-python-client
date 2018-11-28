# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
"""


from datetime import datetime
from infobip.util.models import DefaultObject, serializable
from infobip.util.TimeUnit import TimeUnit
from infobip.api.model.omni.send.NotificationOptions import NotificationOptions


class PushData(DefaultObject):
    @property
    @serializable(name="customPayload", type=dict)
    def custom_payload(self):
        """
        Property is a dictionary with values of type: object
        """
        return self.get_field_value("custom_payload")

    @custom_payload.setter
    def custom_payload(self, custom_payload):
        """
        Property is a dictionary with values of type: object
        """
        self.set_field_value("custom_payload", custom_payload)

    def set_custom_payload(self, custom_payload):
        self.custom_payload = custom_payload
        return self

    @property
    @serializable(name="notificationOptions", type=NotificationOptions)
    def notification_options(self):
        """
        Property is of type: NotificationOptions
        """
        return self.get_field_value("notification_options")

    @notification_options.setter
    def notification_options(self, notification_options):
        """
        Property is of type: NotificationOptions
        """
        self.set_field_value("notification_options", notification_options)

    def set_notification_options(self, notification_options):
        self.notification_options = notification_options
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