from enum import Enum

from . import BaseDatasetType
from .common import ContinuousPickupDropOff
from .types import URL, Color


class RouteType(Enum):
    LIGHT_RAIL = 0
    SUBWAY = 1
    RAIL = 2
    BUS = 3
    FERRY = 4
    CABLE_TRAM = 5
    AERIAL_LIFT = 6
    FUNICULAR = 7
    TROLLEYBUS = 11
    MONORAIL = 12


class Route(BaseDatasetType):
    filename = 'routes.txt'

    def __init__(
            self,
            route_id: str,
            route_type: RouteType,
            agency_id: str | None = None,
            route_short_name: str | None = None,
            route_long_name: str | None = None,
            route_desc: str | None = None,
            route_url: URL | None = None,
            route_color: Color | None = None,
            route_text_color: Color | None = None,
            route_sort_order: int | None = None,
            continuous_pickup: ContinuousPickupDropOff | None = None,
            continuous_drop_off: ContinuousPickupDropOff | None = None,
            network_id: str | None = None
    ):
        self.route_id = route_id
        self.route_type = route_type
        self.agency_id = agency_id
        self.route_short_name = route_short_name
        self.route_long_name = route_long_name
        self.route_desc = route_desc
        self.route_url = route_url
        self.route_color = route_color
        self.route_text_color = route_text_color
        self.route_sort_order = route_sort_order
        self.continuous_pickup = continuous_pickup
        self.continuous_drop_off = continuous_drop_off
        self.network_id = network_id
