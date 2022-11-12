from dataclasses import dataclass
from typing import Optional, ClassVar, Dict

from transitsnake.common import BaseDatasetType, Field, NonStrictEnum
from transitsnake.validation import latitude, longitude, url


class StopLocationType(NonStrictEnum):
    UNSUPPORTED_VALUE = -1  # Not a part of GTFS Specification

    STOP = 0
    STATION = 1
    ENTRANCE_EXIT = 2
    GENERIC_NODE = 3
    BOARDING_AREA = 4


@dataclass
class Stop(BaseDatasetType):
    filename: ClassVar[str] = 'stops.txt'
    primary_key: ClassVar[tuple] = ('stop_id',)

    stop_id: str
    stop_code: Optional[str] = None
    stop_name: Optional[str] = None
    tts_stop_name: Optional[str] = None
    stop_desc: Optional[str] = None
    stop_lat: Optional[float] = None
    stop_lon: Optional[float] = None
    zone_id: Optional[str] = None
    stop_url: Optional[str] = None
    location_type: Optional[StopLocationType] = None
    parent_station: Optional[str] = None
    stop_timezone: Optional[str] = None
    wheelchair_boarding = None
    level_id: Optional[str] = None
    platform_code: Optional[str] = None

    def _coords_required(self):
        return self.location_type in [StopLocationType.STOP, StopLocationType.STATION, StopLocationType.ENTRANCE_EXIT]

    def _parent_required(self):
        return self.location_type in [StopLocationType.ENTRANCE_EXIT, StopLocationType.GENERIC_NODE, StopLocationType.BOARDING_AREA]

    meta: ClassVar[Dict[str, Field]] = {
        'stop_name': Field(conditional_required=_coords_required),
        'parent_station': Field(conditional_required=_parent_required),
        'stop_lat': Field(validators=latitude, conditional_required=_coords_required),
        'stop_lon': Field(validators=longitude, conditional_required=_coords_required),
        'stop_url': Field(validators=url),
    }
