# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
"""


from datetime import datetime
from infobip.util.models import DefaultObject, serializable

class Network(DefaultObject):
    @property
    @serializable(name="networkName", type=str)
    def network_name(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("network_name")

    @network_name.setter
    def network_name(self, network_name):
        """
        Property is of type: unicode
        """
        self.set_field_value("network_name", network_name)

    def set_network_name(self, network_name):
        self.network_name = network_name
        return self

    @property
    @serializable(name="networkPrefix", type=str)
    def network_prefix(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("network_prefix")

    @network_prefix.setter
    def network_prefix(self, network_prefix):
        """
        Property is of type: unicode
        """
        self.set_field_value("network_prefix", network_prefix)

    def set_network_prefix(self, network_prefix):
        self.network_prefix = network_prefix
        return self

    @property
    @serializable(name="countryName", type=str)
    def country_name(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("country_name")

    @country_name.setter
    def country_name(self, country_name):
        """
        Property is of type: unicode
        """
        self.set_field_value("country_name", country_name)

    def set_country_name(self, country_name):
        self.country_name = country_name
        return self

    @property
    @serializable(name="countryPrefix", type=str)
    def country_prefix(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("country_prefix")

    @country_prefix.setter
    def country_prefix(self, country_prefix):
        """
        Property is of type: unicode
        """
        self.set_field_value("country_prefix", country_prefix)

    def set_country_prefix(self, country_prefix):
        self.country_prefix = country_prefix
        return self