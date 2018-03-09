# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
"""


from datetime import datetime
from infobip.util.models import DefaultObject, serializable
from infobip.api.model.omni.To import To


class Destination(DefaultObject):
    @property
    @serializable(name="messageId", type=unicode)
    def message_id(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("message_id")

    @message_id.setter
    def message_id(self, message_id):
        """
        Property is of type: unicode
        """
        self.set_field_value("message_id", message_id)

    def set_message_id(self, message_id):
        self.message_id = message_id
        return self

    @property
    @serializable(name="to", type=To)
    def to(self):
        """
        Property is of type: To
        """
        return self.get_field_value("to")

    @to.setter
    def to(self, to):
        """
        Property is of type: To
        """
        self.set_field_value("to", to)

    def set_to(self, to):
        self.to = to
        return self