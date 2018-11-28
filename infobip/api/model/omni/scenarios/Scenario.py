# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
"""


from datetime import datetime
from infobip.util.models import DefaultObject, serializable
from infobip.api.model.omni.scenarios.Step import Step


class Scenario(DefaultObject):
    @property
    @serializable(name="key", type=str)
    def key(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("key")

    @key.setter
    def key(self, key):
        """
        Property is of type: unicode
        """
        self.set_field_value("key", key)

    def set_key(self, key):
        self.key = key
        return self

    @property
    @serializable(name="name", type=str)
    def name(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("name")

    @name.setter
    def name(self, name):
        """
        Property is of type: unicode
        """
        self.set_field_value("name", name)

    def set_name(self, name):
        self.name = name
        return self

    @property
    @serializable(name="flow", type=Step)
    def flow(self):
        """
        Property is a list of: Step
        """
        return self.get_field_value("flow")

    @flow.setter
    def flow(self, flow):
        """
        Property is a list of: Step
        """
        self.set_field_value("flow", flow)

    def set_flow(self, flow):
        self.flow = flow
        return self

    @property
    @serializable(name="defaultScenario", type=bool)
    def default_scenario(self):
        """
        Property is of type: bool
        """
        return self.get_field_value("default_scenario")

    @default_scenario.setter
    def default_scenario(self, default_scenario):
        """
        Property is of type: bool
        """
        self.set_field_value("default_scenario", default_scenario)

    def set_default_scenario(self, default_scenario):
        self.default_scenario = default_scenario
        return self