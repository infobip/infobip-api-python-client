# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
TODO: Point to Github contribution instructions
"""


from datetime import datetime
from infobip_api_python_client.util.models import DefaultObject, serializable
from decimal import Decimal

class Price(DefaultObject):
    @property
    @serializable(name="pricePerLookup", type=Decimal)
    def price_per_lookup(self):
        return self.get_field_value("price_per_lookup")

    @price_per_lookup.setter
    def price_per_lookup(self, price_per_lookup):
        self.set_field_value("price_per_lookup", price_per_lookup)

    def set_price_per_lookup(self, price_per_lookup):
        self.price_per_lookup = price_per_lookup
        return self

    @property
    @serializable(name="pricePerMessage", type=Decimal)
    def price_per_message(self):
        return self.get_field_value("price_per_message")

    @price_per_message.setter
    def price_per_message(self, price_per_message):
        self.set_field_value("price_per_message", price_per_message)

    def set_price_per_message(self, price_per_message):
        self.price_per_message = price_per_message
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