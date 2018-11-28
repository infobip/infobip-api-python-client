from infobip.clients import get_number_context_logs
from .__init__ import configuration

get_delivery_reports_client = get_number_context_logs(configuration)
response = get_delivery_reports_client.execute({"limit": 1})
print((str(response)))
