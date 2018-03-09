# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
"""


from datetime import datetime
from infobip.util.models import DefaultObject, serializable
from infobip.api.model.omni.scenarios.Scenario import Scenario


class ScenariosResponse(DefaultObject):
    @property
    @serializable(name="scenarios", type=Scenario)
    def scenarios(self):
        """
        Property is a list of: Scenario
        """
        return self.get_field_value("scenarios")

    @scenarios.setter
    def scenarios(self, scenarios):
        """
        Property is a list of: Scenario
        """
        self.set_field_value("scenarios", scenarios)

    def set_scenarios(self, scenarios):
        self.scenarios = scenarios
        return self