__author__ = 'nmaric'

from infobip_api_python_client.clients import get_account_balance
from __init__ import configuration

get_account_balance_client = get_account_balance(configuration)
balance = get_account_balance_client.execute()
print balance
