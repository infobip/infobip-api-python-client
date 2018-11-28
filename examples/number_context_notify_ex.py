from infobip.clients import number_context_notify
from infobip.api.model.nc.notify.NumberContextRequest import NumberContextRequest
from .__init__ import configuration

number_context_client = number_context_notify(configuration)

request = NumberContextRequest()
request.to = "number1aaa"
request.notify_url = "https://test.com/url_for_number_context_reports"
response = number_context_client.execute(request)

print(response)
