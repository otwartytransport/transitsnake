from dataclasses import dataclass
from enum import Enum
from typing import Optional, ClassVar, Dict

from . import BaseDatasetType, Field
from .routes import Route
from .stop_times import StopTime


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

    @staticmethod
    def shape_id_required(trip, dataset):
        if (trip.route_id,) in dataset[Route]:
            route = dataset[Route][(trip.route_id,)]
            if route.continuous_pickup is not None or route.continuous_drop_off is not None:
                return True

        if dataset[StopTime].has_by_partial_key(('trip_id',), (trip.trip_id,)):
            stop_times = dataset[StopTime].get_by_partial_key(('trip_id',), (trip.trip_id,))
            for stop_time in stop_times:
                if stop_time.continuous_pickup is not None or stop_time.continuous_drop_off is not None:
                    return True

        return False

    meta: ClassVar[Dict[str, Field]] = {
        'shape_id': Field(global_conditional_required=shape_id_required)
    }
