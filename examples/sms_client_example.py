from infobip_api_python_client.clients import send_single_textual_sms
from infobip_api_python_client.infobip_api.models.mt.send.textual.SMSTextualRequest import SMSTextualRequest
from __init__ import configuration

send_sms_client = send_single_textual_sms(configuration)

request = SMSTextualRequest()
request.text = "This is an example message."
request.to = ["number1aaa", "number2bbb"]
response = send_sms_client.execute(request)

print(response)
