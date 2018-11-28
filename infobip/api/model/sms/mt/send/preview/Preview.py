# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
"""


from datetime import datetime
from infobip.util.models import DefaultObject, serializable
from infobip.api.model.sms.mt.send.preview.Configuration import Configuration


class Preview(DefaultObject):
    @property
    @serializable(name="textPreview", type=str)
    def text_preview(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("text_preview")

    @text_preview.setter
    def text_preview(self, text_preview):
        """
        Property is of type: unicode
        """
        self.set_field_value("text_preview", text_preview)

    def set_text_preview(self, text_preview):
        self.text_preview = text_preview
        return self

    @property
    @serializable(name="messageCount", type=int)
    def message_count(self):
        """
        Property is of type: int
        """
        return self.get_field_value("message_count")

    @message_count.setter
    def message_count(self, message_count):
        """
        Property is of type: int
        """
        self.set_field_value("message_count", message_count)

    def set_message_count(self, message_count):
        self.message_count = message_count
        return self

    @property
    @serializable(name="charactersRemaining", type=int)
    def characters_remaining(self):
        """
        Property is of type: int
        """
        return self.get_field_value("characters_remaining")

    @characters_remaining.setter
    def characters_remaining(self, characters_remaining):
        """
        Property is of type: int
        """
        self.set_field_value("characters_remaining", characters_remaining)

    def set_characters_remaining(self, characters_remaining):
        self.characters_remaining = characters_remaining
        return self

    @property
    @serializable(name="configuration", type=Configuration)
    def configuration(self):
        """
        Property is of type: Configuration
        """
        return self.get_field_value("configuration")

    @configuration.setter
    def configuration(self, configuration):
        """
        Property is of type: Configuration
        """
        self.set_field_value("configuration", configuration)

    def set_configuration(self, configuration):
        self.configuration = configuration
        return self