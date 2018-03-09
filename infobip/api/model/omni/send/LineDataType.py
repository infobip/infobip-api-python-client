# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
"""


from enum import Enum


class LineDataType(Enum):
    TEXT = "TEXT"
    IMAGE = "IMAGE"
    VIDEO = "VIDEO"
    AUDIO = "AUDIO"
    STICKER = "STICKER"

    def __init__(self, value):
        if value not in LineDataType.values():
            raise NotImplementedError('Constructing a LineDataType is not supported!')

    @staticmethod
    def get_by_name(name):
        return LineDataType.values().intersection({name}).pop()

    @staticmethod
    def values():
        return {
            LineDataType.TEXT,
            LineDataType.IMAGE,
            LineDataType.VIDEO,
            LineDataType.AUDIO,
            LineDataType.STICKER
        }
