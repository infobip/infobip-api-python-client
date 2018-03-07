# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
"""


from datetime import datetime
from infobip.util.models import DefaultObject, serializable
from infobip.api.model.omni.logs.OmniLog import OmniLog


class OmniLogsResponse(DefaultObject):
    @property
    @serializable(name="results", type=OmniLog)
    def results(self):
        """
        Property is a list of: OmniLog
        """
        return self.get_field_value("results")

    @results.setter
    def results(self, results):
        """
        Property is a list of: OmniLog
        """
        self.set_field_value("results", results)

    def set_results(self, results):
        self.results = results
        return self