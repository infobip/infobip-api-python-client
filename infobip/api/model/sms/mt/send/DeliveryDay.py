# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
"""


from enum import Enum


class DeliveryDay(Enum):
    MONDAY = "MONDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"
    THURSDAY = "THURSDAY"
    FRIDAY = "FRIDAY"
    SATURDAY = "SATURDAY"
    SUNDAY = "SUNDAY"

    def __init__(self, value):
        if value not in DeliveryDay.values():
            raise NotImplementedError('Constructing a DeliveryDay is not supported!')

    @staticmethod
    def get_by_name(name):
        return DeliveryDay.values().intersection({name}).pop()

    @staticmethod
    def values():
        return {
            DeliveryDay.MONDAY,
            DeliveryDay.TUESDAY,
            DeliveryDay.WEDNESDAY,
            DeliveryDay.THURSDAY,
            DeliveryDay.FRIDAY,
            DeliveryDay.SATURDAY,
            DeliveryDay.SUNDAY
        }
