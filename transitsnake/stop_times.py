import datetime
from enum import Enum

from . import BaseDatasetType
from .common import ContinuousPickupDropOff


class PickupDropOffType(Enum):
    ALLOWED = 0
    NOT_AVAILABLE = 1
    MUST_PHONE = 2
    ON_REQUEST_TO_DRIVER = 3


class Timepoint(Enum):
    APPROXIMATE = 0
    EXACT = 1


class StopTime(BaseDatasetType):
    filename = 'stop_times.txt'

    def __init__(
            self,
            trip_id: str,
            stop_id: str,
            stop_sequence: int,
            arrival_time: datetime.time | None = None,
            departure_time: datetime.time | None = None,
            stop_headsign: str | None = None,
            pickup_type: PickupDropOffType | None = None,
            drop_off_type: PickupDropOffType | None = None,
            continuous_pickup: ContinuousPickupDropOff | None = None,
            continuous_drop_off: ContinuousPickupDropOff | None = None,
            shape_dist_traveled: float | None = None,
            timepoint: Timepoint | None = None
    ):
        self.trip_id = trip_id
        self.stop_id = stop_id
        self.stop_sequence = stop_sequence
        self.arrival_time = arrival_time
        self.departure_time = departure_time
        self.stop_headsign = stop_headsign
        self.pickup_type = pickup_type
        self.drop_off_type = drop_off_type
        self.continuous_pickup = continuous_pickup
        self.continuous_drop_off = continuous_drop_off
        self.shape_dist_traveled = shape_dist_traveled
        self.timepoint = timepoint
