# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
"""


from datetime import datetime
from infobip.util.models import DefaultObject, serializable
from infobip.api.model.sms.mt.bulks.status.BulkStatus import BulkStatus


class UpdateStatusRequest(DefaultObject):
    @property
    @serializable(name="status", type=BulkStatus)
    def status(self):
        """
        Property is of type: BulkStatus
        """
        return self.get_field_value("status")

    @status.setter
    def status(self, status):
        """
        Property is of type: BulkStatus
        """
        self.set_field_value("status", status)

    def set_status(self, status):
        self.status = status
        return self