# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
"""


from enum import Enum


class BulkStatus(Enum):
    PENDING = "PENDING"
    PAUSED = "PAUSED"
    PROCESSING = "PROCESSING"
    CANCELED = "CANCELED"
    FINISHED = "FINISHED"
    FAILED = "FAILED"

    def __init__(self, value):
        if value not in BulkStatus.values():
            raise NotImplementedError('Constructing a BulkStatus is not supported!')

    @staticmethod
    def get_by_name(name):
        return BulkStatus.values().intersection({name}).pop()

    @staticmethod
    def values():
        return {
            BulkStatus.PENDING,
            BulkStatus.PAUSED,
            BulkStatus.PROCESSING,
            BulkStatus.CANCELED,
            BulkStatus.FINISHED,
            BulkStatus.FAILED
        }
