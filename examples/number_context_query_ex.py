from infobip.clients import number_context_query
from infobip.api.model.nc.query.NumberContextRequest import NumberContextRequest
from .__init__ import configuration

number_context_client = number_context_query(configuration)

request = NumberContextRequest()
request.to = "number1aaa"
response = number_context_client.execute(request)

print(response)
