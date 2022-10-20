from dataclasses import dataclass
from enum import Enum
from typing import Optional, ClassVar

from . import BaseDatasetType, Field
from .routes import Route


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
    filename: ClassVar[str] = 'trips.txt'
    primary_key: ClassVar[tuple] = ('trip_id',)

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

    _meta = {
        'shape_id': Field(global_conditional_required=lambda trip, dataset: dataset[Route][(trip.route_id,)])
    }
