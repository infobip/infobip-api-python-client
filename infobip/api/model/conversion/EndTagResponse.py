# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
"""


from datetime import datetime
from infobip.util.models import DefaultObject, serializable
class EndTagResponse(DefaultObject):
    @property
    @serializable(name="processKey", type=unicode)
    def process_key(self):
        return self.get_field_value("process_key")

    @process_key.setter
    def process_key(self, process_key):
        self.set_field_value("process_key", process_key)

    def set_process_key(self, process_key):
        self.process_key = process_key
        return self