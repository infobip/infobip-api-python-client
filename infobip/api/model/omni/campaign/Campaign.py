# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
"""


from datetime import datetime
from infobip.util.models import DefaultObject, serializable

class Campaign(DefaultObject):
    @property
    @serializable(name="key", type=str)
    def key(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("key")

    @key.setter
    def key(self, key):
        """
        Property is of type: unicode
        """
        self.set_field_value("key", key)

    def set_key(self, key):
        self.key = key
        return self

    @property
    @serializable(name="name", type=str)
    def name(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("name")

    @name.setter
    def name(self, name):
        """
        Property is of type: unicode
        """
        self.set_field_value("name", name)

    def set_name(self, name):
        self.name = name
        return self