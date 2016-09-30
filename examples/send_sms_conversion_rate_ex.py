# -*- coding: utf-8 -*-

from infobip.api.model.sms.mt.send.Tracking import Tracking
from infobip.clients import send_multiple_textual_sms_advanced
from infobip.clients import log_end_tag
from infobip.api.model.sms.mt.send.textual.SMSAdvancedTextualRequest import SMSAdvancedTextualRequest
from infobip.api.model.sms.mt.send.Message import Message
from infobip.api.model.Destination import Destination
from __init__ import configuration

send_sms_client = send_multiple_textual_sms_advanced(configuration)

dest = Destination()
dest.to = "number1aaa"

message = Message()
message.text = "This is an example message."
message.destinations = [dest]

request = SMSAdvancedTextualRequest()
request.messages = [message]

tracking = Tracking()
tracking.set_track("SMS")
request.set_tracking(tracking)

response = send_sms_client.execute(request)

print(response)

end_log_client = log_end_tag(configuration)
end_tag_response = end_log_client.execute(response.messages[0].message_id)

print(end_tag_response)
