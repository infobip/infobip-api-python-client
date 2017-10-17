# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
"""


from datetime import datetime
from infobip.util.models import DefaultObject, serializable
from infobip.api.model.sms.mo.reports.MOReport import MOReport

class MOReportResponse(DefaultObject):
    @property
    @serializable(name="messageCount", type=int)
    def message_count(self):
        return self.get_field_value("message_count")

    @message_count.setter
    def message_count(self, message_count):
        self.set_field_value("message_count", message_count)

    def set_message_count(self, message_count):
        self.message_count = message_count
        return self

    @property
    @serializable(name="pendingMessageCount", type=int)
    def pending_message_count(self):
        return self.get_field_value("pending_message_count")

    @pending_message_count.setter
    def pending_message_count(self, pending_message_count):
        self.set_field_value("pending_message_count", pending_message_count)

    def set_pending_message_count(self, pending_message_count):
        self.pending_message_count = pending_message_count
        return self

    @property
    @serializable(name="results", type=MOReport, list=True)
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