# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
TODO: Point to Github contribution instructions
"""


from datetime import datetime
from infobip_api_python_client.util.models import DefaultObject, serializable
from infobip_api_python_client.api.model.sms.nc.lookup.async.NCResponseDetailsAsync import NCResponseDetailsAsync

class NCResponseAsync(DefaultObject):
    @property
    @serializable(name="bulkId", type=unicode)
    def bulk_id(self):
        return self.get_field_value("bulk_id")

    @bulk_id.setter
    def bulk_id(self, bulk_id):
        self.set_field_value("bulk_id", bulk_id)

    def set_bulk_id(self, bulk_id):
        self.bulk_id = bulk_id
        return self

    @property
    @serializable(name="results", type=NCResponseDetailsAsync, list=True)
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