# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
"""


from datetime import datetime
from infobip.util.models import DefaultObject, serializable

class NotificationOptions(DefaultObject):
    @property
    @serializable(name="vibrationEnabled", type=bool)
    def vibration_enabled(self):
        """
        Property is of type: bool
        """
        return self.get_field_value("vibration_enabled")

    @vibration_enabled.setter
    def vibration_enabled(self, vibration_enabled):
        """
        Property is of type: bool
        """
        self.set_field_value("vibration_enabled", vibration_enabled)

    def set_vibration_enabled(self, vibration_enabled):
        self.vibration_enabled = vibration_enabled
        return self

    @property
    @serializable(name="soundEnabled", type=bool)
    def sound_enabled(self):
        """
        Property is of type: bool
        """
        return self.get_field_value("sound_enabled")

    @sound_enabled.setter
    def sound_enabled(self, sound_enabled):
        """
        Property is of type: bool
        """
        self.set_field_value("sound_enabled", sound_enabled)

    def set_sound_enabled(self, sound_enabled):
        self.sound_enabled = sound_enabled
        return self

    @property
    @serializable(name="soundName", type=str)
    def sound_name(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("sound_name")

    @sound_name.setter
    def sound_name(self, sound_name):
        """
        Property is of type: unicode
        """
        self.set_field_value("sound_name", sound_name)

    def set_sound_name(self, sound_name):
        self.sound_name = sound_name
        return self

    @property
    @serializable(name="badge", type=int)
    def badge(self):
        """
        Property is of type: int
        """
        return self.get_field_value("badge")

    @badge.setter
    def badge(self, badge):
        """
        Property is of type: int
        """
        self.set_field_value("badge", badge)

    def set_badge(self, badge):
        self.badge = badge
        return self

    @property
    @serializable(name="contentUrl", type=str)
    def content_url(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("content_url")

    @content_url.setter
    def content_url(self, content_url):
        """
        Property is of type: unicode
        """
        self.set_field_value("content_url", content_url)

    def set_content_url(self, content_url):
        self.content_url = content_url
        return self

    @property
    @serializable(name="category", type=str)
    def category(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("category")

    @category.setter
    def category(self, category):
        """
        Property is of type: unicode
        """
        self.set_field_value("category", category)

    def set_category(self, category):
        self.category = category
        return self