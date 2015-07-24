from infobip.clients import send_multiple_textual_sms_advanced
from infobip.api.model.sms.mt.send.textual.SMSAdvancedTextualRequest import SMSAdvancedTextualRequest
from infobip.api.model.sms.mt.send.SMSData import SMSData
from infobip.api.model.sms.mt.send.IsFlash import IsFlash
from infobip.api.model.sms.Destination import Destination
from __init__ import configuration

send_sms_client = send_multiple_textual_sms_advanced(configuration)

dest = Destination()
dest.message_id = "message_123"
dest.to = "number1aaa"

message = SMSData()
message.flash = IsFlash(true)
message.text = "This is an example message."
message.destinations = [dest]

request = SMSAdvancedTextualRequest()
request.messages = [message]

response = send_sms_client.execute(request)

print(response)
