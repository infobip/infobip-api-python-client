# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
TODO: Point to Github contribution instructions
"""


from datetime import datetime
from infobip.util.models import DefaultObject, serializable
from infobip.api.model.sms.mt.logs.SMSLog import SMSLog

class SMSLogsResponse(DefaultObject):
    @property
    @serializable(name="results", type=SMSLog, list=True)
    def results(self):
        return self.get_field_value("results")

    @results.setter
    def results(self, results):
        self.set_field_value("results", results)

    def set_results(self, results):
        self.results = results
        return self

    def add_results(self, *results):
        if not self.results:
            self.results = []

        self.results.extend(results)
        return self

    def remove_results(self, *results):
        if not self.results:
            return self

        for i in results:
            self.results.remove(i)

        return self