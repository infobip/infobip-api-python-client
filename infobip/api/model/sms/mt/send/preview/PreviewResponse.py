# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
"""


from datetime import datetime
from infobip.util.models import DefaultObject, serializable
from infobip.api.model.sms.mt.send.preview.Preview import Preview


class PreviewResponse(DefaultObject):
    @property
    @serializable(name="originalText", type=str)
    def original_text(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("original_text")

    @original_text.setter
    def original_text(self, original_text):
        """
        Property is of type: unicode
        """
        self.set_field_value("original_text", original_text)

    def set_original_text(self, original_text):
        self.original_text = original_text
        return self

    @property
    @serializable(name="previews", type=Preview)
    def previews(self):
        """
        Property is a list of: Preview
        """
        return self.get_field_value("previews")

    @previews.setter
    def previews(self, previews):
        """
        Property is a list of: Preview
        """
        self.set_field_value("previews", previews)

    def set_previews(self, previews):
        self.previews = previews
        return self