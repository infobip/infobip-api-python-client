# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
"""


from datetime import datetime
from infobip.util.models import DefaultObject, serializable
from infobip.api.model.Error import Error
from infobip.api.model.Status import Status
from infobip.api.model.Price import Price


class SMSReport(DefaultObject):
    @property
    @serializable(name="bulkId", type=str)
    def bulk_id(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("bulk_id")

    @bulk_id.setter
    def bulk_id(self, bulk_id):
        """
        Property is of type: unicode
        """
        self.set_field_value("bulk_id", bulk_id)

    def set_bulk_id(self, bulk_id):
        self.bulk_id = bulk_id
        return self

    @property
    @serializable(name="messageId", type=str)
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
    @serializable(name="to", type=str)
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
    @serializable(name="from", type=str)
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
    @serializable(name="sentAt", type=datetime)
    def sent_at(self):
        """
        Property is of type: datetime
        """
        return self.get_field_value("sent_at")

    @sent_at.setter
    def sent_at(self, sent_at):
        """
        Property is of type: datetime
        """
        self.set_field_value("sent_at", sent_at)

    def set_sent_at(self, sent_at):
        self.sent_at = sent_at
        return self

    @property
    @serializable(name="doneAt", type=datetime)
    def done_at(self):
        """
        Property is of type: datetime
        """
        return self.get_field_value("done_at")

    @done_at.setter
    def done_at(self, done_at):
        """
        Property is of type: datetime
        """
        self.set_field_value("done_at", done_at)

    def set_done_at(self, done_at):
        self.done_at = done_at
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

    @property
    @serializable(name="mccMnc", type=str)
    def mcc_mnc(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("mcc_mnc")

    @mcc_mnc.setter
    def mcc_mnc(self, mcc_mnc):
        """
        Property is of type: unicode
        """
        self.set_field_value("mcc_mnc", mcc_mnc)

    def set_mcc_mnc(self, mcc_mnc):
        self.mcc_mnc = mcc_mnc
        return self

    @property
    @serializable(name="price", type=Price)
    def price(self):
        """
        Property is of type: Price
        """
        return self.get_field_value("price")

    @price.setter
    def price(self, price):
        """
        Property is of type: Price
        """
        self.set_field_value("price", price)

    def set_price(self, price):
        self.price = price
        return self

    @property
    @serializable(name="status", type=Status)
    def status(self):
        """
        Property is of type: Status
        """
        return self.get_field_value("status")

    @status.setter
    def status(self, status):
        """
        Property is of type: Status
        """
        self.set_field_value("status", status)

    def set_status(self, status):
        self.status = status
        return self

    @property
    @serializable(name="error", type=Error)
    def error(self):
        """
        Property is of type: Error
        """
        return self.get_field_value("error")

    @error.setter
    def error(self, error):
        """
        Property is of type: Error
        """
        self.set_field_value("error", error)

    def set_error(self, error):
        self.error = error
        return self

    @property
    @serializable(name="callbackData", type=str)
    def callback_data(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("callback_data")

    @callback_data.setter
    def callback_data(self, callback_data):
        """
        Property is of type: unicode
        """
        self.set_field_value("callback_data", callback_data)

    def set_callback_data(self, callback_data):
        self.callback_data = callback_data
        return self