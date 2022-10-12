from enum import Enum

from . import BaseDatasetType
from .types import Latitude, Longitude, URL, Timezone


class StopLocationType(Enum):
    STOP = 0
    STATION = 1
    ENTRANCE_EXIT = 2
    GENERIC_NODE = 3
    BOARDING_AREA = 4


class Stop(BaseDatasetType):
    filename = 'stops.txt'

    def __init__(
            self,
            stop_id: str,
            stop_code: str | None = None,
            stop_name: str | None = None,
            tts_stop_name: str | None = None,
            stop_desc: str | None = None,
            stop_lat: Latitude | None = None,
            stop_lon: Longitude | None = None,
            zone_id: str | None = None,
            stop_url: URL | None = None,
            location_type: StopLocationType | None = None,
            parent_station: str | None = None,
            stop_timezone: Timezone | None = None,
            wheelchair_boarding=None,
            level_id: str | None = None,
            platform_code: str | None = None
    ):
        self.stop_id = stop_id
        self.stop_code = stop_code
        self.stop_name = stop_name
        self.tts_stop_name = tts_stop_name
        self.stop_desc = stop_desc
        self.stop_lat = stop_lat
        self.stop_lon = stop_lon
        self.zone_id = zone_id
        self.stop_url = stop_url
        self.location_type = location_type
        self.parent_station = parent_station
        self.stop_timezone = stop_timezone
        self.wheelchair_boarding = wheelchair_boarding
        self.level_id = level_id
        self.platform_code = platform_code
