__author__ = 'mmatosevic'

from infobip.clients import get_received_messages
from __init__ import configuration

get_delivery_reports_client = get_received_messages(configuration)
response = get_delivery_reports_client.execute({"limit": 1})
print(unicode(response))
