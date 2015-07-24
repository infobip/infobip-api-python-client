# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
TODO: Point to Github contribution instructions
"""


from datetime import datetime
from infobip.util.models import DefaultObject, serializable
class NCRequest(DefaultObject):
    @property
    @serializable(name="to", type=unicode, list=True)
    def to(self):
        return self.get_field_value("to")

    @to.setter
    def to(self, to):
        self.set_field_value("to", to)

    def set_to(self, to):
        self.to = to
        return self

    def add_to(self, *to):
        if not self.to:
            self.to = []

        self.to.extend(to)
        return self

    def remove_to(self, *to):
        if not self.to:
            return self

        for i in to:
            self.to.remove(i)

        return self