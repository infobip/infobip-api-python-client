# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
"""


from datetime import datetime
from infobip.util.models import DefaultObject, serializable
from infobip.api.model.sms.mt.send.preview.Preview import Preview

class PreviewResponse(DefaultObject):
    @property
    @serializable(name="originalText", type=unicode)
    def original_text(self):
        return self.get_field_value("original_text")

    @original_text.setter
    def original_text(self, original_text):
        self.set_field_value("original_text", original_text)

    def set_original_text(self, original_text):
        self.original_text = original_text
        return self

    @property
    @serializable(name="previews", type=Preview, list=True)
    def previews(self):
        return self.get_field_value("previews")

    @previews.setter
    def previews(self, previews):
        self.set_field_value("previews", previews)

    def set_previews(self, previews):
        self.previews = previews
        return self

    def add_previews(self, *previews):
        if not self.previews:
            self.previews = []

        self.previews.extend(previews)
        return self

    def remove_previews(self, *previews):
        if not self.previews:
            return self

        for i in previews:
            self.previews.remove(i)

        return self