# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
"""


from datetime import datetime
from infobip.util.models import DefaultObject, serializable
from infobip.api.model.omni.campaign.Destination import Destination


class Destinations(DefaultObject):
    @property
    @serializable(name="destinations", type=Destination)
    def destinations(self):
        """
        Property is a list of: Destination
        """
        return self.get_field_value("destinations")

    @destinations.setter
    def destinations(self, destinations):
        """
        Property is a list of: Destination
        """
        self.set_field_value("destinations", destinations)

    def set_destinations(self, destinations):
        self.destinations = destinations
        return self