# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
"""

from datetime import datetime
from infobip.util.models import DefaultObject, serializable
from infobip.api.model.sms.mt.send.IndiaDltOptions import IndiaDltOptions


class RegionalOptions(DefaultObject):
    @property
    @serializable(name="indiaDlt", type=IndiaDltOptions)
    def india_dlt(self):
        """
        Property is of type: IndiaDltOptions
        """
        return self.get_field_value("india_dlt")

    @india_dlt.setter
    def india_dlt(self, india_dlt):
        """
        Property is of type: IndiaDltOptions
        """
        self.set_field_value("india_dlt", india_dlt)

    def set_india_dlt(self, india_dlt):
        self.india_dlt = india_dlt
        return self