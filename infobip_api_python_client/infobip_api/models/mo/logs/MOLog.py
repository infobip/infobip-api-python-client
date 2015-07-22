# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
TODO: Point to Github contribution instructions
"""


from datetime import datetime
from infobip_api_python_client.util.models import DefaultObject, serializable
class MOLog(DefaultObject):
    @property
    @serializable(name="cleanText", type=unicode)
    def clean_text(self):
        return self.get_field_value("clean_text")

    @clean_text.setter
    def clean_text(self, clean_text):
        self.set_field_value("clean_text", clean_text)

    def set_clean_text(self, clean_text):
        self.clean_text = clean_text
        return self

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
    @serializable(name="from", type=unicode)
    def from_(self):
        return self.get_field_value("from_")

    @from_.setter
    def from_(self, from_):
        self.set_field_value("from_", from_)

    def set_from_(self, from_):
        self.from_ = from_
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
    @serializable(name="text", type=unicode)
    def text(self):
        return self.get_field_value("text")

    @text.setter
    def text(self, text):
        self.set_field_value("text", text)

    def set_text(self, text):
        self.text = text
        return self

    @property
    @serializable(name="keyword", type=unicode)
    def keyword(self):
        return self.get_field_value("keyword")

    @keyword.setter
    def keyword(self, keyword):
        self.set_field_value("keyword", keyword)

    def set_keyword(self, keyword):
        self.keyword = keyword
        return self

    @property
    @serializable(name="receivedAt", type=datetime)
    def received_at(self):
        return self.get_field_value("received_at")

    @received_at.setter
    def received_at(self, received_at):
        self.set_field_value("received_at", received_at)

    def set_received_at(self, received_at):
        self.received_at = received_at
        return self