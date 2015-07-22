__author__ = 'mmatosevic'

from infobip_api_python_client.clients import get_sent_sms_delivery_reports
from __init__ import configuration

get_delivery_reports_client = get_sent_sms_delivery_reports(configuration)
response = get_delivery_reports_client.execute({"limit": 1})
print(response)
