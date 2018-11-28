# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
"""


from datetime import datetime
from infobip.util.models import DefaultObject, serializable
from infobip.api.model.nc.notify.NumberContextResponseDetails import NumberContextResponseDetails


class NumberContextResponse(DefaultObject):
    @property
    @serializable(name="results", type=NumberContextResponseDetails)
    def results(self):
        """
        Property is a list of: NumberContextResponseDetails
        """
        return self.get_field_value("results")

    @results.setter
    def results(self, results):
        """
        Property is a list of: NumberContextResponseDetails
        """
        self.set_field_value("results", results)

    def set_results(self, results):
        self.results = results
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