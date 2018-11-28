# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
"""


from datetime import datetime
from infobip.util.models import DefaultObject, serializable

class Language(DefaultObject):
    @property
    @serializable(name="singleShift", type=bool)
    def single_shift(self):
        """
        Property is of type: bool
        """
        return self.get_field_value("single_shift")

    @single_shift.setter
    def single_shift(self, single_shift):
        """
        Property is of type: bool
        """
        self.set_field_value("single_shift", single_shift)

    def set_single_shift(self, single_shift):
        self.single_shift = single_shift
        return self

    @property
    @serializable(name="lockingShift", type=bool)
    def locking_shift(self):
        """
        Property is of type: bool
        """
        return self.get_field_value("locking_shift")

    @locking_shift.setter
    def locking_shift(self, locking_shift):
        """
        Property is of type: bool
        """
        self.set_field_value("locking_shift", locking_shift)

    def set_locking_shift(self, locking_shift):
        self.locking_shift = locking_shift
        return self

    @property
    @serializable(name="languageCode", type=str)
    def language_code(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("language_code")

    @language_code.setter
    def language_code(self, language_code):
        """
        Property is of type: unicode
        """
        self.set_field_value("language_code", language_code)

    def set_language_code(self, language_code):
        self.language_code = language_code
        return self