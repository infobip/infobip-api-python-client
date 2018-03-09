# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
"""


from datetime import datetime
from infobip.util.models import DefaultObject, serializable

class MOLog(DefaultObject):
    @property
    @serializable(name="messageId", type=unicode)
    def message_id(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("message_id")

    @message_id.setter
    def message_id(self, message_id):
        """
        Property is of type: unicode
        """
        self.set_field_value("message_id", message_id)

    def set_message_id(self, message_id):
        self.message_id = message_id
        return self

    @property
    @serializable(name="from", type=unicode)
    def from_(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("from_")

    @from_.setter
    def from_(self, from_):
        """
        Property is of type: unicode
        """
        self.set_field_value("from_", from_)

    def set_from_(self, from_):
        self.from_ = from_
        return self

    @property
    @serializable(name="to", type=unicode)
    def to(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("to")

    @to.setter
    def to(self, to):
        """
        Property is of type: unicode
        """
        self.set_field_value("to", to)

    def set_to(self, to):
        self.to = to
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
    @serializable(name="cleanText", type=unicode)
    def clean_text(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("clean_text")

    @clean_text.setter
    def clean_text(self, clean_text):
        """
        Property is of type: unicode
        """
        self.set_field_value("clean_text", clean_text)

    def set_clean_text(self, clean_text):
        self.clean_text = clean_text
        return self

    @property
    @serializable(name="keyword", type=unicode)
    def keyword(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("keyword")

    @keyword.setter
    def keyword(self, keyword):
        """
        Property is of type: unicode
        """
        self.set_field_value("keyword", keyword)

    def set_keyword(self, keyword):
        self.keyword = keyword
        return self

    @property
    @serializable(name="receivedAt", type=datetime)
    def received_at(self):
        """
        Property is of type: datetime
        """
        return self.get_field_value("received_at")

    @received_at.setter
    def received_at(self, received_at):
        """
        Property is of type: datetime
        """
        self.set_field_value("received_at", received_at)

    def set_received_at(self, received_at):
        self.received_at = received_at
        return self

    @property
    @serializable(name="smsCount", type=int)
    def sms_count(self):
        """
        Property is of type: int
        """
        return self.get_field_value("sms_count")

    @sms_count.setter
    def sms_count(self, sms_count):
        """
        Property is of type: int
        """
        self.set_field_value("sms_count", sms_count)

    def set_sms_count(self, sms_count):
        self.sms_count = sms_count
        return self