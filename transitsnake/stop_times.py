import datetime
from dataclasses import dataclass
from enum import Enum
from typing import Optional, ClassVar

from . import BaseDatasetType
from .common import ContinuousPickupDropOff
from .validation import non_negative, Field


class PickupDropOffType(Enum):
    ALLOWED = 0
    NOT_AVAILABLE = 1
    MUST_PHONE = 2
    ON_REQUEST_TO_DRIVER = 3


class Timepoint(Enum):
    APPROXIMATE = 0
    EXACT = 1


@dataclass
class StopTime(BaseDatasetType):
    filename: ClassVar[str] = 'stop_times.txt'
    primary_key: ClassVar[tuple] = ('trip_id', 'stop_sequence')

    trip_id: str
    stop_id: str
    stop_sequence: int
    arrival_time: Optional[datetime.time] = None
    departure_time: Optional[datetime.time] = None
    stop_headsign: Optional[str] = None
    pickup_type: Optional[PickupDropOffType] = None
    drop_off_type: Optional[PickupDropOffType] = None
    continuous_pickup: Optional[ContinuousPickupDropOff] = None
    continuous_drop_off: Optional[ContinuousPickupDropOff] = None
    shape_dist_traveled: Optional[float] = None
    timepoint: Optional[Timepoint] = None

    _meta = {
        'shape_dist_traveled': Field(validators=non_negative),
        'arrival_time': Field(conditional_required=lambda full: full.timepoint == Timepoint.EXACT),
        'departure_time': Field(conditional_required=lambda full: full.timepoint == Timepoint.EXACT)
    }
