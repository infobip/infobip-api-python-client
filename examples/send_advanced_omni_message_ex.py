# -*- coding: utf-8 -*-

from infobip.api.model.omni.Destination import Destination
from infobip.api.model.omni.To import To
from infobip.api.model.omni.send.Language import Language
from infobip.api.model.omni.send.OmniAdvancedRequest import OmniAdvancedRequest
from infobip.api.model.omni.send.SmsData import SmsData
from infobip.api.model.omni.send.ViberData import ViberData
from infobip.clients import send_advanced_omni_message
from .__init__ import configuration


def get_destinations():
    to = To()
    to.phone_number = "41793026731"
    destination = Destination()
    destination.to = to

    return [destination]


def get_sms_data():
    sms_data = SmsData()
    sms_data.text = "Artık Ulusal Dil Tanımlayıcısı ile Türkçe karakterli smslerinizi rahatlıkla iletebilirsiniz."
    language = Language()
    language.language_code = "TR"
    sms_data.language = language
    sms_data.transliteration = "TURKISH"

    return sms_data


def get_viber_data():
    viber_data = ViberData()
    viber_data.text = "Luke, I'm your father!"

    return viber_data


request = OmniAdvancedRequest()
request.destinations = get_destinations()
request.scenario_key = "6EDEA8BF17983A97C42BCA702F0A673D"
request.sms = get_sms_data()
request.viber = get_viber_data()

client = send_advanced_omni_message(configuration)
response = client.execute(request)

print(response)
