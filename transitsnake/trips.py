from enum import Enum

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


class Trip(BaseDatasetType):
    filename = 'trips.txt'

    def __init__(
            self,
            route_id: str,
            service_id: str,
            trip_id: str | None = None,
            trip_headsign: str | None = None,
            trip_short_name: str | None = None,
            direction_id: TripDirection | None = None,
            block_id: str | None = None,
            shape_id: str | None = None,
            wheelchair_accessible: WheelchairAccessible | None = None,
            bikes_allowed: BikesAccessible | None = None
    ):
        self.route_id = route_id
        self.service_id = service_id
        self.trip_id = trip_id
        self.trip_headsign = trip_headsign
        self.trip_short_name = trip_short_name
        self.direction_id = direction_id
        self.block_id = block_id
        self.shape_id = shape_id
        self.wheelchair_accessible = wheelchair_accessible
        self.bikes_allowed = bikes_allowed
