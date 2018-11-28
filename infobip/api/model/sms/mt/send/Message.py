# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
"""


from datetime import datetime
from infobip.util.models import DefaultObject, serializable
from infobip.api.model.Destination import Destination
from infobip.api.model.sms.mt.send.Language import Language
from infobip.api.model.sms.mt.send.binary.BinaryContent import BinaryContent
from infobip.api.model.sms.mt.send.DeliveryTimeWindow import DeliveryTimeWindow


class Message(DefaultObject):
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
    @serializable(name="to", type=str)
    def to(self):
        """
        Property is a list of: unicode
        """
        return self.get_field_value("to")

    @to.setter
    def to(self, to):
        """
        Property is a list of: unicode
        """
        self.set_field_value("to", to)

    def set_to(self, to):
        self.to = to
        return self

    @property
    @serializable(name="destinations", type=Destination)
    def destinations(self):
        """
        Property is a list of: Destination
        """
        return self.get_field_value("destinations")

    @destinations.setter
    def destinations(self, destinations):
        """
        Property is a list of: Destination
        """
        self.set_field_value("destinations", destinations)

    def set_destinations(self, destinations):
        self.destinations = destinations
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
    @serializable(name="binary", type=BinaryContent)
    def binary(self):
        """
        Property is of type: BinaryContent
        """
        return self.get_field_value("binary")

    @binary.setter
    def binary(self, binary):
        """
        Property is of type: BinaryContent
        """
        self.set_field_value("binary", binary)

    def set_binary(self, binary):
        self.binary = binary
        return self

    @property
    @serializable(name="flash", type=bool)
    def flash(self):
        """
        Property is of type: bool
        """
        return self.get_field_value("flash")

    @flash.setter
    def flash(self, flash):
        """
        Property is of type: bool
        """
        self.set_field_value("flash", flash)

    def set_flash(self, flash):
        self.flash = flash
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
    @serializable(name="transliteration", type=str)
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
    @serializable(name="notify", type=bool)
    def notify(self):
        """
        Property is of type: bool
        """
        return self.get_field_value("notify")

    @notify.setter
    def notify(self, notify):
        """
        Property is of type: bool
        """
        self.set_field_value("notify", notify)

    def set_notify(self, notify):
        self.notify = notify
        return self

    @property
    @serializable(name="intermediateReport", type=bool)
    def intermediate_report(self):
        """
        Property is of type: bool
        """
        return self.get_field_value("intermediate_report")

    @intermediate_report.setter
    def intermediate_report(self, intermediate_report):
        """
        Property is of type: bool
        """
        self.set_field_value("intermediate_report", intermediate_report)

    def set_intermediate_report(self, intermediate_report):
        self.intermediate_report = intermediate_report
        return self

    @property
    @serializable(name="notifyUrl", type=str)
    def notify_url(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("notify_url")

    @notify_url.setter
    def notify_url(self, notify_url):
        """
        Property is of type: unicode
        """
        self.set_field_value("notify_url", notify_url)

    def set_notify_url(self, notify_url):
        self.notify_url = notify_url
        return self

    @property
    @serializable(name="notifyContentType", type=str)
    def notify_content_type(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("notify_content_type")

    @notify_content_type.setter
    def notify_content_type(self, notify_content_type):
        """
        Property is of type: unicode
        """
        self.set_field_value("notify_content_type", notify_content_type)

    def set_notify_content_type(self, notify_content_type):
        self.notify_content_type = notify_content_type
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
    @serializable(name="sendAt", type=datetime)
    def send_at(self):
        """
        Property is of type: datetime
        """
        return self.get_field_value("send_at")

    @send_at.setter
    def send_at(self, send_at):
        """
        Property is of type: datetime
        """
        self.set_field_value("send_at", send_at)

    def set_send_at(self, send_at):
        self.send_at = send_at
        return self

    @property
    @serializable(name="deliveryTimeWindow", type=DeliveryTimeWindow)
    def delivery_time_window(self):
        """
        Property is of type: DeliveryTimeWindow
        """
        return self.get_field_value("delivery_time_window")

    @delivery_time_window.setter
    def delivery_time_window(self, delivery_time_window):
        """
        Property is of type: DeliveryTimeWindow
        """
        self.set_field_value("delivery_time_window", delivery_time_window)

    def set_delivery_time_window(self, delivery_time_window):
        self.delivery_time_window = delivery_time_window
        return self

    @property
    @serializable(name="campaignId", type=str)
    def campaign_id(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("campaign_id")

    @campaign_id.setter
    def campaign_id(self, campaign_id):
        """
        Property is of type: unicode
        """
        self.set_field_value("campaign_id", campaign_id)

    def set_campaign_id(self, campaign_id):
        self.campaign_id = campaign_id
        return self

    @property
    @serializable(name="operatorClientId", type=str)
    def operator_client_id(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("operator_client_id")

    @operator_client_id.setter
    def operator_client_id(self, operator_client_id):
        """
        Property is of type: unicode
        """
        self.set_field_value("operator_client_id", operator_client_id)

    def set_operator_client_id(self, operator_client_id):
        self.operator_client_id = operator_client_id
        return self