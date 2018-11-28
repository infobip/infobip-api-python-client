# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
"""


from datetime import datetime
from infobip.util.models import DefaultObject, serializable
from infobip.api.model.sms.mt.send.Language import Language


class Configuration(DefaultObject):
    @property
    @serializable(name="language", type=Language)
    def language(self):
        """
        Property is of type: Language
        """
        return self.get_field_value("language")

    @language.setter
    def language(self, language):
        """
        Property is of type: Language
        """
        self.set_field_value("language", language)

    def set_language(self, language):
        self.language = language
        return self

    @property
    @serializable(name="transliteration", type=str)
    def transliteration(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("transliteration")

    @transliteration.setter
    def transliteration(self, transliteration):
        """
        Property is of type: unicode
        """
        self.set_field_value("transliteration", transliteration)

    def set_transliteration(self, transliteration):
        self.transliteration = transliteration
        return self