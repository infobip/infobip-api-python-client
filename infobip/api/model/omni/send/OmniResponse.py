# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
"""


from datetime import datetime
from infobip.util.models import DefaultObject, serializable
from infobip.api.model.omni.send.OmniResponseDetails import OmniResponseDetails


class OmniResponse(DefaultObject):
    @property
    @serializable(name="bulkId", type=str)
    def bulk_id(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("bulk_id")

    @bulk_id.setter
    def bulk_id(self, bulk_id):
        """
        Property is of type: unicode
        """
        self.set_field_value("bulk_id", bulk_id)

    def set_bulk_id(self, bulk_id):
        self.bulk_id = bulk_id
        return self

    @property
    @serializable(name="messages", type=OmniResponseDetails)
    def messages(self):
        """
        Property is a list of: OmniResponseDetails
        """
        return self.get_field_value("messages")

    @messages.setter
    def messages(self, messages):
        """
        Property is a list of: OmniResponseDetails
        """
        self.set_field_value("messages", messages)

    def set_messages(self, messages):
        self.messages = messages
        return self