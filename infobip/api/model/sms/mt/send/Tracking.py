# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
"""


from datetime import datetime
from infobip.util.models import DefaultObject, serializable
class Tracking(DefaultObject):
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

    @property
    @serializable(name="track", type=unicode)
    def track(self):
        return self.get_field_value("track")

    @track.setter
    def track(self, track):
        self.set_field_value("track", track)

    def set_track(self, track):
        self.track = track
        return self

    @property
    @serializable(name="type", type=unicode)
    def type(self):
        return self.get_field_value("type")

    @type.setter
    def type(self, type):
        self.set_field_value("type", type)

    def set_type(self, type):
        self.type = type
        return self