# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
"""


from datetime import datetime
from infobip.util.models import DefaultObject, serializable

class NumberContextRequest(DefaultObject):
    @property
    @serializable(name="to", type=str)
    def to(self):
        """
        Property is a list of: unicode
        """
        return self.get_field_value("to")

    @to.setter
    def to(self, to):
        """
        Property is a list of: unicode
        """
        self.set_field_value("to", to)

    def set_to(self, to):
        self.to = to
        return self

    @property
    @serializable(name="notifyUrl", type=str)
    def notify_url(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("notify_url")

    @notify_url.setter
    def notify_url(self, notify_url):
        """
        Property is of type: unicode
        """
        self.set_field_value("notify_url", notify_url)

    def set_notify_url(self, notify_url):
        self.notify_url = notify_url
        return self

    @property
    @serializable(name="notifyContentType", type=str)
    def notify_content_type(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("notify_content_type")

    @notify_content_type.setter
    def notify_content_type(self, notify_content_type):
        """
        Property is of type: unicode
        """
        self.set_field_value("notify_content_type", notify_content_type)

    def set_notify_content_type(self, notify_content_type):
        self.notify_content_type = notify_content_type
        return self