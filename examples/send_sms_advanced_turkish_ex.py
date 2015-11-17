# -*- coding: utf-8 -*-

from infobip.api.model.sms.mt.send.Language import Language
from infobip.clients import send_multiple_textual_sms_advanced
from infobip.api.model.sms.mt.send.textual.SMSAdvancedTextualRequest import SMSAdvancedTextualRequest
from infobip.api.model.sms.mt.send.SMSData import SMSData
from infobip.api.model.sms.Destination import Destination
from __init__ import configuration

send_sms_client = send_multiple_textual_sms_advanced(configuration)

dest = Destination()
dest.message_id = "message_111"
dest.to = "number1aaa"

language = Language()
language.language_code = "TR"
language.single_shift = True
language.locking_shift = False

message = SMSData()
message.from_ = "sender1"
message.text = "Artık Ulusal Dil Tanımlayıcısı ile Türkçe karakterli smslerinizi rahatlıkla iletebilirsiniz."
message.destinations = [dest]
message.language = language

request = SMSAdvancedTextualRequest()
request.messages = [message]

response = send_sms_client.execute(request)

print(response)
