# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
TODO: Point to Github contribution instructions
"""


from datetime import datetime
from infobip_api_python_client.util.models import DefaultObject, serializable
from infobip_api_python_client.api.model.sms.mt.send.binary.BinaryContent import BinaryContent
from infobip_api_python_client.api.model.sms.mt.send.Language import Language
from infobip_api_python_client.api.model.sms.mt.send.IsFlash import IsFlash
from infobip_api_python_client.api.model.sms.Destination import Destination

class SMSData(DefaultObject):
    @property
    @serializable(name="campaignId", type=unicode)
    def campaign_id(self):
        return self.get_field_value("campaign_id")

    @campaign_id.setter
    def campaign_id(self, campaign_id):
        self.set_field_value("campaign_id", campaign_id)

    def set_campaign_id(self, campaign_id):
        self.campaign_id = campaign_id
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
    @serializable(name="destinations", type=Destination, list=True)
    def destinations(self):
        return self.get_field_value("destinations")

    @destinations.setter
    def destinations(self, destinations):
        self.set_field_value("destinations", destinations)

    def set_destinations(self, destinations):
        self.destinations = destinations
        return self

    def add_destinations(self, *destinations):
        if not self.destinations:
            self.destinations = []

        self.destinations.extend(destinations)
        return self

    def remove_destinations(self, *destinations):
        if not self.destinations:
            return self

        for i in destinations:
            self.destinations.remove(i)

        return self

    @property
    @serializable(name="language", type=Language)
    def language(self):
        return self.get_field_value("language")

    @language.setter
    def language(self, language):
        self.set_field_value("language", language)

    def set_language(self, language):
        self.language = language
        return self

    @property
    @serializable(name="notify", type=bool)
    def notify(self):
        return self.get_field_value("notify")

    @notify.setter
    def notify(self, notify):
        self.set_field_value("notify", notify)

    def set_notify(self, notify):
        self.notify = notify
        return self

    @property
    @serializable(name="notifyContentType", type=unicode)
    def notify_content_type(self):
        return self.get_field_value("notify_content_type")

    @notify_content_type.setter
    def notify_content_type(self, notify_content_type):
        self.set_field_value("notify_content_type", notify_content_type)

    def set_notify_content_type(self, notify_content_type):
        self.notify_content_type = notify_content_type
        return self

    @property
    @serializable(name="validityPeriod", type=long)
    def validity_period(self):
        return self.get_field_value("validity_period")

    @validity_period.setter
    def validity_period(self, validity_period):
        self.set_field_value("validity_period", validity_period)

    def set_validity_period(self, validity_period):
        self.validity_period = validity_period
        return self

    @property
    @serializable(name="binary", type=BinaryContent)
    def binary(self):
        return self.get_field_value("binary")

    @binary.setter
    def binary(self, binary):
        self.set_field_value("binary", binary)

    def set_binary(self, binary):
        self.binary = binary
        return self

    @property
    @serializable(name="callbackData", type=unicode)
    def callback_data(self):
        return self.get_field_value("callback_data")

    @callback_data.setter
    def callback_data(self, callback_data):
        self.set_field_value("callback_data", callback_data)

    def set_callback_data(self, callback_data):
        self.callback_data = callback_data
        return self

    @property
    @serializable(name="notifyUrl", type=unicode)
    def notify_url(self):
        return self.get_field_value("notify_url")

    @notify_url.setter
    def notify_url(self, notify_url):
        self.set_field_value("notify_url", notify_url)

    def set_notify_url(self, notify_url):
        self.notify_url = notify_url
        return self

    @property
    @serializable(name="to", type=unicode, list=True)
    def to(self):
        return self.get_field_value("to")

    @to.setter
    def to(self, to):
        self.set_field_value("to", to)

    def set_to(self, to):
        self.to = to
        return self

    def add_to(self, *to):
        if not self.to:
            self.to = []

        self.to.extend(to)
        return self

    def remove_to(self, *to):
        if not self.to:
            return self

        for i in to:
            self.to.remove(i)

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
    @serializable(name="sendAt", type=datetime)
    def send_at(self):
        return self.get_field_value("send_at")

    @send_at.setter
    def send_at(self, send_at):
        self.set_field_value("send_at", send_at)

    def set_send_at(self, send_at):
        self.send_at = send_at
        return self

    @property
    @serializable(name="transliteration", type=unicode)
    def transliteration(self):
        return self.get_field_value("transliteration")

    @transliteration.setter
    def transliteration(self, transliteration):
        self.set_field_value("transliteration", transliteration)

    def set_transliteration(self, transliteration):
        self.transliteration = transliteration
        return self

    @property
    @serializable(name="flash", type=IsFlash)
    def flash(self):
        return self.get_field_value("flash")

    @flash.setter
    def flash(self, flash):
        self.set_field_value("flash", flash)

    def set_flash(self, flash):
        self.flash = flash
        return self