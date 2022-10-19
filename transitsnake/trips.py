from dataclasses import dataclass
from enum import Enum
from typing import Optional

from . import BaseDatasetType


class TripDirection(Enum):
    ONE = 0
    OPPOSITE = 1


class WheelchairAccessible(Enum):
    NO_INFORMATION = 0
    YES = 1
    NO = 2


class BikesAccessible(Enum):
    NO_INFORMATION = 0
    YES = 1
    NO = 2


@dataclass
class Trip(BaseDatasetType):
    filename = 'trips.txt'

    route_id: str
    service_id: str
    trip_id: Optional[str] = None
    trip_headsign: Optional[str] = None
    trip_short_name: Optional[str] = None
    direction_id: Optional[TripDirection] = None
    block_id: Optional[str] = None
    shape_id: Optional[str] = None
    wheelchair_accessible: Optional[WheelchairAccessible] = None
    bikes_allowed: Optional[BikesAccessible] = None
