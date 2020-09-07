# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
"""

from datetime import datetime
from infobip.util.models import DefaultObject, serializable

class IndiaDltOptions(DefaultObject):
    @property
    @serializable(name="contentTemplateId", type=unicode)
    def content_template_id(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("content_template_id")

    @content_template_id.setter
    def content_template_id(self, content_template_id):
        """
        Property is of type: unicode
        """
        self.set_field_value("content_template_id", content_template_id)

    def set_content_template_id(self, content_template_id):
        self.content_template_id = content_template_id
        return self
    @property
    @serializable(name="principalEntityId", type=unicode)
    def principal_entity_id(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("principal_entity_id")

    @principal_entity_id.setter
    def principal_entity_id(self, principal_entity_id):
        """
        Property is of type: unicode
        """
        self.set_field_value("principal_entity_id", principal_entity_id)

    def set_principal_entity_id(self, principal_entity_id):
        self.principal_entity_id = principal_entity_id
        return self