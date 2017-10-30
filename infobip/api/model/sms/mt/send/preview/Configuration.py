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
        return self.get_field_value("language")

    @language.setter
    def language(self, language):
        self.set_field_value("language", language)

    def set_language(self, language):
        self.language = language
        return self

    @property
    @serializable(name="transliteration", type=unicode)
    def transliteration(self):
        return self.get_field_value("transliteration")

    @transliteration.setter
    def transliteration(self, transliteration):
        self.set_field_value("transliteration", transliteration)

    def set_transliteration(self, transliteration):
        self.transliteration = transliteration
        return self