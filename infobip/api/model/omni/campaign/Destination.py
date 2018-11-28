# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
"""


from datetime import datetime
from infobip.util.models import DefaultObject, serializable
from infobip.api.model.omni.campaign.Gender import Gender


class Destination(DefaultObject):
    @property
    @serializable(name="firstName", type=str)
    def first_name(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("first_name")

    @first_name.setter
    def first_name(self, first_name):
        """
        Property is of type: unicode
        """
        self.set_field_value("first_name", first_name)

    def set_first_name(self, first_name):
        self.first_name = first_name
        return self

    @property
    @serializable(name="lastName", type=str)
    def last_name(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("last_name")

    @last_name.setter
    def last_name(self, last_name):
        """
        Property is of type: unicode
        """
        self.set_field_value("last_name", last_name)

    def set_last_name(self, last_name):
        self.last_name = last_name
        return self

    @property
    @serializable(name="middleName", type=str)
    def middle_name(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("middle_name")

    @middle_name.setter
    def middle_name(self, middle_name):
        """
        Property is of type: unicode
        """
        self.set_field_value("middle_name", middle_name)

    def set_middle_name(self, middle_name):
        self.middle_name = middle_name
        return self

    @property
    @serializable(name="gsm", type=str)
    def gsm(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("gsm")

    @gsm.setter
    def gsm(self, gsm):
        """
        Property is of type: unicode
        """
        self.set_field_value("gsm", gsm)

    def set_gsm(self, gsm):
        self.gsm = gsm
        return self

    @property
    @serializable(name="landline", type=str)
    def landline(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("landline")

    @landline.setter
    def landline(self, landline):
        """
        Property is of type: unicode
        """
        self.set_field_value("landline", landline)

    def set_landline(self, landline):
        self.landline = landline
        return self

    @property
    @serializable(name="email", type=str)
    def email(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("email")

    @email.setter
    def email(self, email):
        """
        Property is of type: unicode
        """
        self.set_field_value("email", email)

    def set_email(self, email):
        self.email = email
        return self

    @property
    @serializable(name="address", type=str)
    def address(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("address")

    @address.setter
    def address(self, address):
        """
        Property is of type: unicode
        """
        self.set_field_value("address", address)

    def set_address(self, address):
        self.address = address
        return self

    @property
    @serializable(name="city", type=str)
    def city(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("city")

    @city.setter
    def city(self, city):
        """
        Property is of type: unicode
        """
        self.set_field_value("city", city)

    def set_city(self, city):
        self.city = city
        return self

    @property
    @serializable(name="country", type=str)
    def country(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("country")

    @country.setter
    def country(self, country):
        """
        Property is of type: unicode
        """
        self.set_field_value("country", country)

    def set_country(self, country):
        self.country = country
        return self

    @property
    @serializable(name="gender", type=Gender)
    def gender(self):
        """
        Property is of type: Gender
        """
        return self.get_field_value("gender")

    @gender.setter
    def gender(self, gender):
        """
        Property is of type: Gender
        """
        self.set_field_value("gender", gender)

    def set_gender(self, gender):
        self.gender = gender
        return self

    @property
    @serializable(name="birthday", type=str)
    def birthday(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("birthday")

    @birthday.setter
    def birthday(self, birthday):
        """
        Property is of type: unicode
        """
        self.set_field_value("birthday", birthday)

    def set_birthday(self, birthday):
        self.birthday = birthday
        return self