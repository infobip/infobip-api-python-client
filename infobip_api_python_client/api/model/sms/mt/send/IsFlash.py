# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
TODO: Point to Github contribution instructions
"""


from datetime import datetime
from infobip_api_python_client.util.models import DefaultObject, serializable
class IsFlash(DefaultObject):
    @property
    @serializable(name="id", type=int)
    def id(self):
        return self.get_field_value("id")

    @id.setter
    def id(self, id):
        self.set_field_value("id", id)

    def set_id(self, id):
        self.id = id
        return self

    @property
    @serializable(name="flash", type=bool)
    def flash(self):
        return self.get_field_value("flash")

    @flash.setter
    def flash(self, flash):
        self.set_field_value("flash", flash)

    def set_flash(self, flash):
        self.flash = flash
        return self