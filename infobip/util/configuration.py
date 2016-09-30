__author__ = 'mstipanov'


class Configuration:
    def __init__(self, username=None, password=None, api_key=None, token=None, base_url="https://api.infobip.com"):
        self.base_url = base_url
        self.username = username
        self.password = password
        self.api_key = api_key
        self.token = token
