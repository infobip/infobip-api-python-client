from infobip.clients import send_multiple_textual_sms_advanced
from infobip.api.model.sms.mt.send.textual.SMSAdvancedTextualRequest import SMSAdvancedTextualRequest
from infobip.api.model.sms.mt.send.Message import Message
from infobip.api.model.Destination import Destination
from __init__ import configuration

send_sms_client = send_multiple_textual_sms_advanced(configuration)

dest = Destination()
dest.message_id = "message_111"
dest.to = "number1aaa"

message = Message()
message.from_ = "sender1"
message.text = "This is an example message."
message.notify_url = "https://test.com/url_for_delivery_reports"
message.destinations = [dest]

dest2 = Destination()
dest2.message_id = "message_222"
dest2.to = "number2bbb"

message2 = Message()
message2.from_ = "123412341234"
message2.text = "This is an example message #2."
message2.notify_url = "https://test.com/url_for_delivery_reports_2"
message2.destinations = [dest2]

request = SMSAdvancedTextualRequest()
request.messages = [message, message2]

response = send_sms_client.execute(request)

print(response)
