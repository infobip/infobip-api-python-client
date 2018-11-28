# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
"""


from datetime import datetime
from infobip.util.models import DefaultObject, serializable
from infobip.api.model.omni.OmniChannel import OmniChannel


class Step(DefaultObject):
    @property
    @serializable(name="from", type=str)
    def from_(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("from_")

    @from_.setter
    def from_(self, from_):
        """
        Property is of type: unicode
        """
        self.set_field_value("from_", from_)

    def set_from_(self, from_):
        self.from_ = from_
        return self

    @property
    @serializable(name="channel", type=OmniChannel)
    def channel(self):
        """
        Property is of type: OmniChannel
        """
        return self.get_field_value("channel")

    @channel.setter
    def channel(self, channel):
        """
        Property is of type: OmniChannel
        """
        self.set_field_value("channel", channel)

    def set_channel(self, channel):
        self.channel = channel
        return self