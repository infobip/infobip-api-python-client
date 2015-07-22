# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
TODO: Point to Github contribution instructions
"""


from datetime import datetime
from infobip_api_python_client.util.models import DefaultObject, serializable
from infobip_api_python_client.infobip_api.models.Status import Status

class SMSResponseDetails(DefaultObject):
    @property
    @serializable(name="smsCount", type=int)
    def sms_count(self):
        return self.get_field_value("sms_count")

    @sms_count.setter
    def sms_count(self, sms_count):
        self.set_field_value("sms_count", sms_count)

    def set_sms_count(self, sms_count):
        self.sms_count = sms_count
        return self

    @property
    @serializable(name="messageId", type=unicode)
    def message_id(self):
        return self.get_field_value("message_id")

    @message_id.setter
    def message_id(self, message_id):
        self.set_field_value("message_id", message_id)

    def set_message_id(self, message_id):
        self.message_id = message_id
        return self

    @property
    @serializable(name="to", type=unicode)
    def to(self):
        return self.get_field_value("to")

    @to.setter
    def to(self, to):
        self.set_field_value("to", to)

    def set_to(self, to):
        self.to = to
        return self

    @property
    @serializable(name="status", type=Status)
    def status(self):
        return self.get_field_value("status")

    @status.setter
    def status(self, status):
        self.set_field_value("status", status)

    def set_status(self, status):
        self.status = status
        return self