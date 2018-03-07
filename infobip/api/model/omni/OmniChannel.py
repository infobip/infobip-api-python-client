# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
"""


from enum import Enum


class OmniChannel(Enum):
    SMS = "SMS"
    EMAIL = "EMAIL"
    VOICE = "VOICE"
    PARSECO = "PARSECO"
    PUSH = "PUSH"
    VIBER = "VIBER"
    FACEBOOK = "FACEBOOK"
    LINE = "LINE"
    VKONTAKTE = "VKONTAKTE"

    def __init__(self, value):
        if value not in OmniChannel.values():
            raise NotImplementedError('Constructing a OmniChannel is not supported!')

    @staticmethod
    def get_by_name(name):
        return OmniChannel.values().intersection({name}).pop()

    @staticmethod
    def values():
        return {
            OmniChannel.SMS,
            OmniChannel.EMAIL,
            OmniChannel.VOICE,
            OmniChannel.PARSECO,
            OmniChannel.PUSH,
            OmniChannel.VIBER,
            OmniChannel.FACEBOOK,
            OmniChannel.LINE,
            OmniChannel.VKONTAKTE
        }
