from enum import Enum


class ContinuousPickupDropOff(Enum):
    ALLOWED = 0
    NOT_AVAILABLE = 1
    MUST_PHONE = 2
    ON_REQUEST_TO_DRIVER = 3
