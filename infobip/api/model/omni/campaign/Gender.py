# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
"""


from enum import Enum


class Gender(Enum):
    FEMALE = "FEMALE"
    MALE = "MALE"

    def __init__(self, value):
        if value not in Gender.values():
            raise NotImplementedError('Constructing a Gender is not supported!')

    @staticmethod
    def get_by_name(name):
        return Gender.values().intersection({name}).pop()

    @staticmethod
    def values():
        return {
            Gender.FEMALE,
            Gender.MALE
        }
