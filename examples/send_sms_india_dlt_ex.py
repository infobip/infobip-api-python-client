from infobip.clients import send_multiple_textual_sms_advanced
from infobip.api.model.sms.mt.send.textual.SMSAdvancedTextualRequest import SMSAdvancedTextualRequest
from infobip.api.model.sms.mt.send.Message import Message
from infobip.api.model.sms.mt.send.IndiaDltOptions import IndiaDltOptions
from infobip.api.model.sms.mt.send.RegionalOptions import RegionalOptions
from infobip.api.model.Destination import Destination
from __init__ import configuration

send_sms_client = send_multiple_textual_sms_advanced(configuration)

indiaDlt = IndiaDltOptions()
indiaDlt.content_template_id = "content template id"
indiaDlt.principal_entity_id = "principal entity id"

regional = RegionalOptions()
regional.india_dlt = indiaDlt

dest = Destination()
dest.message_id = "message_123"
dest.to = "number1aaa"

message = Message()
message.text = "This is an example message."
message.destinations = [dest]
message.regional = regional

request = SMSAdvancedTextualRequest()
request.messages = [message]

response = send_sms_client.execute(request)

print(response)
