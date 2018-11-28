# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
"""


from datetime import datetime
from infobip.util.models import DefaultObject, serializable
from infobip.api.model.sms.mt.send.Message import Message
from infobip.api.model.sms.mt.send.Tracking import Tracking


class SMSAdvancedTextualRequest(DefaultObject):
    @property
    @serializable(name="tracking", type=Tracking)
    def tracking(self):
        """
        Property is of type: Tracking
        """
        return self.get_field_value("tracking")

    @tracking.setter
    def tracking(self, tracking):
        """
        Property is of type: Tracking
        """
        self.set_field_value("tracking", tracking)

    def set_tracking(self, tracking):
        self.tracking = tracking
        return self

    @property
    @serializable(name="messages", type=Message)
    def messages(self):
        """
        Property is a list of: Message
        """
        return self.get_field_value("messages")

    @messages.setter
    def messages(self, messages):
        """
        Property is a list of: Message
        """
        self.set_field_value("messages", messages)

    def set_messages(self, messages):
        self.messages = messages
        return self

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