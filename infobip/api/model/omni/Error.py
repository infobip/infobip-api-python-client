# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
"""


from datetime import datetime
from infobip.util.models import DefaultObject, serializable

class Error(DefaultObject):
    @property
    @serializable(name="groupId", type=int)
    def group_id(self):
        """
        Property is of type: int
        """
        return self.get_field_value("group_id")

    @group_id.setter
    def group_id(self, group_id):
        """
        Property is of type: int
        """
        self.set_field_value("group_id", group_id)

    def set_group_id(self, group_id):
        self.group_id = group_id
        return self

    @property
    @serializable(name="groupName", type=str)
    def group_name(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("group_name")

    @group_name.setter
    def group_name(self, group_name):
        """
        Property is of type: unicode
        """
        self.set_field_value("group_name", group_name)

    def set_group_name(self, group_name):
        self.group_name = group_name
        return self

    @property
    @serializable(name="id", type=int)
    def id(self):
        """
        Property is of type: int
        """
        return self.get_field_value("id")

    @id.setter
    def id(self, id):
        """
        Property is of type: int
        """
        self.set_field_value("id", id)

    def set_id(self, id):
        self.id = id
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
    @serializable(name="description", type=str)
    def description(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("description")

    @description.setter
    def description(self, description):
        """
        Property is of type: unicode
        """
        self.set_field_value("description", description)

    def set_description(self, description):
        self.description = description
        return self

    @property
    @serializable(name="permanent", type=bool)
    def permanent(self):
        """
        Property is of type: bool
        """
        return self.get_field_value("permanent")

    @permanent.setter
    def permanent(self, permanent):
        """
        Property is of type: bool
        """
        self.set_field_value("permanent", permanent)

    def set_permanent(self, permanent):
        self.permanent = permanent
        return self