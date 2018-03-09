from enum import Enum


class TimeUnit(Enum):
    NANOSECONDS = "NANOSECONDS"
    MICROSECONDS = "MICROSECONDS"
    MILLISECONDS = "MILLISECONDS"
    SECONDS = "SECONDS"
    MINUTES = "MINUTES"
    HOURS = "HOURS"
    DAYS = "DAYS"

    def __init__(self, value):
        if value not in TimeUnit.values():
            raise NotImplementedError('Constructing a FacebookDataType is not supported!')

    @staticmethod
    def get_by_name(name):
        return TimeUnit.values().intersection({name}).pop()

    @staticmethod
    def values():
        return {
            TimeUnit.NANOSECONDS,
            TimeUnit.MICROSECONDS,
            TimeUnit.MILLISECONDS,
            TimeUnit.SECONDS,
            TimeUnit.MINUTES,
            TimeUnit.HOURS,
            TimeUnit.DAYS
        }