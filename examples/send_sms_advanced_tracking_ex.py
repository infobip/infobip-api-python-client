# -*- coding: utf-8 -*-

from infobip.api.model.sms.mt.send.Tracking import Tracking
from infobip.clients import send_multiple_textual_sms_advanced
from infobip.api.model.sms.mt.send.textual.SMSAdvancedTextualRequest import SMSAdvancedTextualRequest
from infobip.api.model.sms.mt.send.SMSData import SMSData
from infobip.api.model.sms.Destination import Destination
from __init__ import configuration

send_sms_client = send_multiple_textual_sms_advanced(configuration)

dest = Destination()
dest.message_id = "message_111"
dest.to = "number1aaa"

message = SMSData()
message.from_ = "sender1"
message.text = "This is an example message. More information you can find on: http://dev.infobip.com/docs/fully-featured-textual-message"
message.destinations = [dest]

request = SMSAdvancedTextualRequest()
request.messages = [message]

tracking = Tracking()
tracking.set_track("URL")
request.set_tracking(tracking)

response = send_sms_client.execute(request)

print(response)
