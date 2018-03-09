# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
"""


from enum import Enum


class FacebookDataType(Enum):
    TEXT = "TEXT"
    IMAGE = "IMAGE"
    AUDIO = "AUDIO"
    VIDEO = "VIDEO"
    FILE = "FILE"

    def __init__(self, value):
        if value not in FacebookDataType.values():
            raise NotImplementedError('Constructing a FacebookDataType is not supported!')

    @staticmethod
    def get_by_name(name):
        return FacebookDataType.values().intersection({name}).pop()

    @staticmethod
    def values():
        return {
            FacebookDataType.TEXT,
            FacebookDataType.IMAGE,
            FacebookDataType.AUDIO,
            FacebookDataType.VIDEO,
            FacebookDataType.FILE
        }
