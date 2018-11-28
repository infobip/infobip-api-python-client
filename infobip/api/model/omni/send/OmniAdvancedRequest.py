# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
"""


from datetime import datetime
from infobip.util.models import DefaultObject, serializable
from infobip.api.model.omni.Destination import Destination
from infobip.api.model.omni.send.ParsecoData import ParsecoData
from infobip.api.model.omni.send.VoiceData import VoiceData
from infobip.api.model.omni.send.FacebookData import FacebookData
from infobip.api.model.omni.send.ViberData import ViberData
from infobip.api.model.omni.send.LineData import LineData
from infobip.api.model.omni.send.VKontakteData import VKontakteData
from infobip.api.model.omni.send.PushData import PushData
from infobip.api.model.omni.send.SmsData import SmsData
from infobip.api.model.omni.send.EmailData import EmailData


class OmniAdvancedRequest(DefaultObject):
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
    @serializable(name="scenarioKey", type=str)
    def scenario_key(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("scenario_key")

    @scenario_key.setter
    def scenario_key(self, scenario_key):
        """
        Property is of type: unicode
        """
        self.set_field_value("scenario_key", scenario_key)

    def set_scenario_key(self, scenario_key):
        self.scenario_key = scenario_key
        return self

    @property
    @serializable(name="sms", type=SmsData)
    def sms(self):
        """
        Property is of type: SmsData
        """
        return self.get_field_value("sms")

    @sms.setter
    def sms(self, sms):
        """
        Property is of type: SmsData
        """
        self.set_field_value("sms", sms)

    def set_sms(self, sms):
        self.sms = sms
        return self

    @property
    @serializable(name="parseco", type=ParsecoData)
    def parseco(self):
        """
        Property is of type: ParsecoData
        """
        return self.get_field_value("parseco")

    @parseco.setter
    def parseco(self, parseco):
        """
        Property is of type: ParsecoData
        """
        self.set_field_value("parseco", parseco)

    def set_parseco(self, parseco):
        self.parseco = parseco
        return self

    @property
    @serializable(name="viber", type=ViberData)
    def viber(self):
        """
        Property is of type: ViberData
        """
        return self.get_field_value("viber")

    @viber.setter
    def viber(self, viber):
        """
        Property is of type: ViberData
        """
        self.set_field_value("viber", viber)

    def set_viber(self, viber):
        self.viber = viber
        return self

    @property
    @serializable(name="voice", type=VoiceData)
    def voice(self):
        """
        Property is of type: VoiceData
        """
        return self.get_field_value("voice")

    @voice.setter
    def voice(self, voice):
        """
        Property is of type: VoiceData
        """
        self.set_field_value("voice", voice)

    def set_voice(self, voice):
        self.voice = voice
        return self

    @property
    @serializable(name="email", type=EmailData)
    def email(self):
        """
        Property is of type: EmailData
        """
        return self.get_field_value("email")

    @email.setter
    def email(self, email):
        """
        Property is of type: EmailData
        """
        self.set_field_value("email", email)

    def set_email(self, email):
        self.email = email
        return self

    @property
    @serializable(name="push", type=PushData)
    def push(self):
        """
        Property is of type: PushData
        """
        return self.get_field_value("push")

    @push.setter
    def push(self, push):
        """
        Property is of type: PushData
        """
        self.set_field_value("push", push)

    def set_push(self, push):
        self.push = push
        return self

    @property
    @serializable(name="facebook", type=FacebookData)
    def facebook(self):
        """
        Property is of type: FacebookData
        """
        return self.get_field_value("facebook")

    @facebook.setter
    def facebook(self, facebook):
        """
        Property is of type: FacebookData
        """
        self.set_field_value("facebook", facebook)

    def set_facebook(self, facebook):
        self.facebook = facebook
        return self

    @property
    @serializable(name="line", type=LineData)
    def line(self):
        """
        Property is of type: LineData
        """
        return self.get_field_value("line")

    @line.setter
    def line(self, line):
        """
        Property is of type: LineData
        """
        self.set_field_value("line", line)

    def set_line(self, line):
        self.line = line
        return self

    @property
    @serializable(name="vKontakte", type=VKontakteData)
    def v_kontakte(self):
        """
        Property is of type: VKontakteData
        """
        return self.get_field_value("v_kontakte")

    @v_kontakte.setter
    def v_kontakte(self, v_kontakte):
        """
        Property is of type: VKontakteData
        """
        self.set_field_value("v_kontakte", v_kontakte)

    def set_v_kontakte(self, v_kontakte):
        self.v_kontakte = v_kontakte
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