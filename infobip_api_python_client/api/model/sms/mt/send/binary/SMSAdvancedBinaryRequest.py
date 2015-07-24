# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
TODO: Point to Github contribution instructions
"""


from datetime import datetime
from infobip_api_python_client.util.models import DefaultObject, serializable
from infobip_api_python_client.api.model.sms.mt.send.SMSData import SMSData

class SMSAdvancedBinaryRequest(DefaultObject):
    @property
    @serializable(name="messages", type=SMSData, list=True)
    def messages(self):
        return self.get_field_value("messages")

    @messages.setter
    def messages(self, messages):
        self.set_field_value("messages", messages)

    def set_messages(self, messages):
        self.messages = messages
        return self

    def add_messages(self, *messages):
        if not self.messages:
            self.messages = []

        self.messages.extend(messages)
        return self

    def remove_messages(self, *messages):
        if not self.messages:
            return self

        for i in messages:
            self.messages.remove(i)

        return self