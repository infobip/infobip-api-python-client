# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
"""


from datetime import datetime
from infobip.util.models import DefaultObject, serializable
class AccountBalance(DefaultObject):
    @property
    @serializable(name="balance", type=float)
    def balance(self):
        return self.get_field_value("balance")

    @balance.setter
    def balance(self, balance):
        self.set_field_value("balance", balance)

    def set_balance(self, balance):
        self.balance = balance
        return self

    @property
    @serializable(name="currency", type=unicode)
    def currency(self):
        return self.get_field_value("currency")

    @currency.setter
    def currency(self, currency):
        self.set_field_value("currency", currency)

    def set_currency(self, currency):
        self.currency = currency
        return self