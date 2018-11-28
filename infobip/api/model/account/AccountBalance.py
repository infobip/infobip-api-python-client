# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
"""


from datetime import datetime
from infobip.util.models import DefaultObject, serializable
from decimal import Decimal


class AccountBalance(DefaultObject):
    @property
    @serializable(name="balance", type=Decimal)
    def balance(self):
        """
        Property is of type: Decimal
        """
        return self.get_field_value("balance")

    @balance.setter
    def balance(self, balance):
        """
        Property is of type: Decimal
        """
        self.set_field_value("balance", balance)

    def set_balance(self, balance):
        self.balance = balance
        return self

    @property
    @serializable(name="currency", type=str)
    def currency(self):
        """
        Property is of type: unicode
        """
        return self.get_field_value("currency")

    @currency.setter
    def currency(self, currency):
        """
        Property is of type: unicode
        """
        self.set_field_value("currency", currency)

    def set_currency(self, currency):
        self.currency = currency
        return self