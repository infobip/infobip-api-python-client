# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
TODO: Point to Github contribution instructions
"""


from datetime import datetime
from infobip_api_python_client.util.models import DefaultObject, serializable
class Language(DefaultObject):
    @property
    @serializable(name="lockingShift", type=bool)
    def locking_shift(self):
        return self.get_field_value("locking_shift")

    @locking_shift.setter
    def locking_shift(self, locking_shift):
        self.set_field_value("locking_shift", locking_shift)

    def set_locking_shift(self, locking_shift):
        self.locking_shift = locking_shift
        return self

    @property
    @serializable(name="singleShift", type=bool)
    def single_shift(self):
        return self.get_field_value("single_shift")

    @single_shift.setter
    def single_shift(self, single_shift):
        self.set_field_value("single_shift", single_shift)

    def set_single_shift(self, single_shift):
        self.single_shift = single_shift
        return self

    @property
    @serializable(name="languageCode", type=unicode)
    def language_code(self):
        return self.get_field_value("language_code")

    @language_code.setter
    def language_code(self, language_code):
        self.set_field_value("language_code", language_code)

    def set_language_code(self, language_code):
        self.language_code = language_code
        return self