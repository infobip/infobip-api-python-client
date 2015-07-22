__author__ = 'mstipanov'


class Configuration:
    def __init__(self, base_url, username = None, password = None, api_key = None, token = None):
        self.base_url = base_url
        self.username = username
        self.password = password
        self.api_key = api_key
        self.token = token
