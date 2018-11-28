# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
"""


from datetime import datetime
from infobip.util.models import DefaultObject, serializable

class Tracking(DefaultObject):
    @property
    @serializable(name="track", type=str)
    def track(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("track")

    @track.setter
    def track(self, track):
        """
        Property is of type: unicode
        """
        self.set_field_value("track", track)

    def set_track(self, track):
        self.track = track
        return self

    @property
    @serializable(name="processKey", type=str)
    def process_key(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("process_key")

    @process_key.setter
    def process_key(self, process_key):
        """
        Property is of type: unicode
        """
        self.set_field_value("process_key", process_key)

    def set_process_key(self, process_key):
        self.process_key = process_key
        return self

    @property
    @serializable(name="type", type=str)
    def type(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("type")

    @type.setter
    def type(self, type):
        """
        Property is of type: unicode
        """
        self.set_field_value("type", type)

    def set_type(self, type):
        self.type = type
        return self

    @property
    @serializable(name="baseUrl", type=str)
    def base_url(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("base_url")

    @base_url.setter
    def base_url(self, base_url):
        """
        Property is of type: unicode
        """
        self.set_field_value("base_url", base_url)

    def set_base_url(self, base_url):
        self.base_url = base_url
        return self