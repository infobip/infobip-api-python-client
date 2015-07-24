# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
TODO: Point to Github contribution instructions
"""


from datetime import datetime
from infobip.util.models import DefaultObject, serializable
class NCRequestAsync(DefaultObject):
    @property
    @serializable(name="notifyUrl", type=unicode)
    def notify_url(self):
        return self.get_field_value("notify_url")

    @notify_url.setter
    def notify_url(self, notify_url):
        self.set_field_value("notify_url", notify_url)

    def set_notify_url(self, notify_url):
        self.notify_url = notify_url
        return self

    @property
    @serializable(name="to", type=unicode, list=True)
    def to(self):
        return self.get_field_value("to")

    @to.setter
    def to(self, to):
        self.set_field_value("to", to)

    def set_to(self, to):
        self.to = to
        return self

    def add_to(self, *to):
        if not self.to:
            self.to = []

        self.to.extend(to)
        return self

    def remove_to(self, *to):
        if not self.to:
            return self

        for i in to:
            self.to.remove(i)

        return self

    @property
    @serializable(name="notifyContentType", type=unicode)
    def notify_content_type(self):
        return self.get_field_value("notify_content_type")

    @notify_content_type.setter
    def notify_content_type(self, notify_content_type):
        self.set_field_value("notify_content_type", notify_content_type)

    def set_notify_content_type(self, notify_content_type):
        self.notify_content_type = notify_content_type
        return self