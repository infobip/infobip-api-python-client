__author__ = 'mmatosevic'

from infobip_api_python_client.clients import get_sent_sms_logs
from __init__ import configuration

get_logs_client = get_sent_sms_logs(configuration)
response = get_logs_client.execute({"limit": 10})
print(response)
