# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
"""


from datetime import datetime
from infobip.util.models import DefaultObject, serializable
from infobip.api.model.sms.mt.send.SMSResponseDetails import SMSResponseDetails


class SMSResponse(DefaultObject):
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
    @serializable(name="trackingProcessKey", type=str)
    def tracking_process_key(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("tracking_process_key")

    @tracking_process_key.setter
    def tracking_process_key(self, tracking_process_key):
        """
        Property is of type: unicode
        """
        self.set_field_value("tracking_process_key", tracking_process_key)

    def set_tracking_process_key(self, tracking_process_key):
        self.tracking_process_key = tracking_process_key
        return self

    @property
    @serializable(name="messages", type=SMSResponseDetails)
    def messages(self):
        """
        Property is a list of: SMSResponseDetails
        """
        return self.get_field_value("messages")

    @messages.setter
    def messages(self, messages):
        """
        Property is a list of: SMSResponseDetails
        """
        self.set_field_value("messages", messages)

    def set_messages(self, messages):
        self.messages = messages
        return self