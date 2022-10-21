from dataclasses import dataclass
from enum import Enum
from typing import ClassVar, Optional, Dict

from .common import BaseDatasetType, Field
from .agency import Agency
from .common import ContinuousPickupDropOff
from .validation import url, non_negative, color


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


@dataclass
class Route(BaseDatasetType):
    filename: ClassVar[str] = 'routes.txt'
    primary_key: ClassVar[tuple] = ('route_id',)

    route_id: str
    route_type: RouteType
    agency_id: Optional[str] = None
    route_short_name: Optional[str] = None
    route_long_name: Optional[str] = None
    route_desc: Optional[str] = None
    route_url: Optional[str] = None
    route_color: Optional[str] = None
    route_text_color: Optional[str] = None
    route_sort_order: Optional[int] = None
    continuous_pickup: Optional[ContinuousPickupDropOff] = None
    continuous_drop_off: Optional[ContinuousPickupDropOff] = None
    network_id: Optional[str] = None

    meta: ClassVar[Dict[str, Field]] = {
        'agency_id': Field(global_conditional_required=lambda full, dataset: len(dataset[Agency]) > 1),
        'route_url': Field(validators=url),
        'route_color': Field(validators=color),
        'route_text_color': Field(validators=color),
        'route_sort_order': Field(validators=non_negative),
        'route_short_name': Field(conditional_required=lambda full: not full.route_long_name),
        'route_long_name': Field(conditional_required=lambda full: not full.route_short_name),
    }
