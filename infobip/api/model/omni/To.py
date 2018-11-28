# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
"""


from datetime import datetime
from infobip.util.models import DefaultObject, serializable

class To(DefaultObject):
    @property
    @serializable(name="phoneNumber", type=str)
    def phone_number(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("phone_number")

    @phone_number.setter
    def phone_number(self, phone_number):
        """
        Property is of type: unicode
        """
        self.set_field_value("phone_number", phone_number)

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number
        return self

    @property
    @serializable(name="emailAddress", type=str)
    def email_address(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("email_address")

    @email_address.setter
    def email_address(self, email_address):
        """
        Property is of type: unicode
        """
        self.set_field_value("email_address", email_address)

    def set_email_address(self, email_address):
        self.email_address = email_address
        return self

    @property
    @serializable(name="pushRegistrationId", type=str)
    def push_registration_id(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("push_registration_id")

    @push_registration_id.setter
    def push_registration_id(self, push_registration_id):
        """
        Property is of type: unicode
        """
        self.set_field_value("push_registration_id", push_registration_id)

    def set_push_registration_id(self, push_registration_id):
        self.push_registration_id = push_registration_id
        return self

    @property
    @serializable(name="facebookUserKey", type=str)
    def facebook_user_key(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("facebook_user_key")

    @facebook_user_key.setter
    def facebook_user_key(self, facebook_user_key):
        """
        Property is of type: unicode
        """
        self.set_field_value("facebook_user_key", facebook_user_key)

    def set_facebook_user_key(self, facebook_user_key):
        self.facebook_user_key = facebook_user_key
        return self

    @property
    @serializable(name="lineUserKey", type=str)
    def line_user_key(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("line_user_key")

    @line_user_key.setter
    def line_user_key(self, line_user_key):
        """
        Property is of type: unicode
        """
        self.set_field_value("line_user_key", line_user_key)

    def set_line_user_key(self, line_user_key):
        self.line_user_key = line_user_key
        return self