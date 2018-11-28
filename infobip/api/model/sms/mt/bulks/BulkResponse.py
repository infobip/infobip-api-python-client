# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
"""


from datetime import datetime
from infobip.util.models import DefaultObject, serializable

class BulkResponse(DefaultObject):
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
    @serializable(name="sendAt", type=datetime)
    def send_at(self):
        """
        Property is of type: datetime
        """
        return self.get_field_value("send_at")

    @send_at.setter
    def send_at(self, send_at):
        """
        Property is of type: datetime
        """
        self.set_field_value("send_at", send_at)

    def set_send_at(self, send_at):
        self.send_at = send_at
        return self