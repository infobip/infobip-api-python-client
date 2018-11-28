# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
"""


from datetime import datetime
from infobip.util.models import DefaultObject, serializable
from infobip.api.model.omni.Destination import Destination


class OmniSimpleRequest(DefaultObject):
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

    @property
    @serializable(name="bulkId", type=str)
    def bulk_id(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("bulk_id")

    @bulk_id.setter
    def bulk_id(self, bulk_id):
        """
        Property is of type: unicode
        """
        self.set_field_value("bulk_id", bulk_id)

    def set_bulk_id(self, bulk_id):
        self.bulk_id = bulk_id
        return self

    @property
    @serializable(name="scenarioKey", type=str)
    def scenario_key(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("scenario_key")

    @scenario_key.setter
    def scenario_key(self, scenario_key):
        """
        Property is of type: unicode
        """
        self.set_field_value("scenario_key", scenario_key)

    def set_scenario_key(self, scenario_key):
        self.scenario_key = scenario_key
        return self

    @property
    @serializable(name="text", type=str)
    def text(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("text")

    @text.setter
    def text(self, text):
        """
        Property is of type: unicode
        """
        self.set_field_value("text", text)

    def set_text(self, text):
        self.text = text
        return self

    @property
    @serializable(name="mailSubject", type=str)
    def mail_subject(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("mail_subject")

    @mail_subject.setter
    def mail_subject(self, mail_subject):
        """
        Property is of type: unicode
        """
        self.set_field_value("mail_subject", mail_subject)

    def set_mail_subject(self, mail_subject):
        self.mail_subject = mail_subject
        return self