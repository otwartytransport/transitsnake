from dataclasses import dataclass
from enum import Enum
from typing import Optional

from . import BaseDatasetType


class TableName(str, Enum):
    AGENCY = 'agency'
    STOPS = 'stops'
    ROUTES = 'routes'
    TRIPS = 'trips'
    STOP_TIMES = 'stop_times'
    PATHWAYS = 'pathways'
    LEVELS = 'levels'
    FEED_INFO = 'feed_info'
    ATTRIBUTIONS = 'attributions'


@dataclass
class Translation(BaseDatasetType):
    filename = 'translations.txt'

    table_name: TableName
    field_name: str
    language: str
    translation: str
    record_id: Optional[str] = None
    record_sub_id: Optional[str] = None
    field_value: Optional[str] = None
