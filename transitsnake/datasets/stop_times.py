from dataclasses import dataclass
from typing import Optional, ClassVar, List, Dict

from transitsnake.common import BaseDatasetType, NonStrictEnum
from transitsnake.common import ContinuousPickupDropOff
from transitsnake.validation import non_negative, Field


class PickupDropOffType(NonStrictEnum):
    UNSUPPORTED_VALUE = -1  # Not a part of GTFS Specification

    ALLOWED = 0
    NOT_AVAILABLE = 1
    MUST_PHONE = 2
    ON_REQUEST_TO_DRIVER = 3


class Timepoint(NonStrictEnum):
    UNSUPPORTED_VALUE = -1  # Not a part of GTFS Specification

    APPROXIMATE = 0
    EXACT = 1


@dataclass
class StopTime(BaseDatasetType):
    filename: ClassVar[str] = 'stop_times.txt'
    primary_key: ClassVar[tuple] = ('trip_id', 'stop_sequence')
    partial_keys: ClassVar[List[tuple]] = [('trip_id',)]

    trip_id: str
    stop_id: str
    stop_sequence: int
    arrival_time: Optional[str] = None
    departure_time: Optional[str] = None
    stop_headsign: Optional[str] = None
    pickup_type: Optional[PickupDropOffType] = None
    drop_off_type: Optional[PickupDropOffType] = None
    continuous_pickup: Optional[ContinuousPickupDropOff] = None
    continuous_drop_off: Optional[ContinuousPickupDropOff] = None
    shape_dist_traveled: Optional[float] = None
    timepoint: Optional[Timepoint] = None

    meta: ClassVar[Dict[str, Field]] = {
        'shape_dist_traveled': Field(validators=non_negative),
        'arrival_time': Field(conditional_required=lambda full: full.timepoint == Timepoint.EXACT or full.timepoint is None),
        'departure_time': Field(conditional_required=lambda full: full.timepoint == Timepoint.EXACT or full.timepoint is None)
    }
