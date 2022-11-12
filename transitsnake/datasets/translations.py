from dataclasses import dataclass
from enum import Enum
from typing import Optional, ClassVar, Dict

from transitsnake.common import BaseDatasetType, Field


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
    filename: ClassVar[str] = 'translations.txt'
    primary_key: ClassVar[tuple] = ('table_name', 'field_name', 'language', 'record_id', 'record_sub_id', 'field_value')

    table_name: TableName
    field_name: str
    language: str
    translation: str
    record_id: Optional[str] = None
    record_sub_id: Optional[str] = None
    field_value: Optional[str] = None

    meta: ClassVar[Dict[str, Field]] = {
        'record_id': Field(
            conditional_required=lambda trans: not trans.field_value,
            conditional_forbidden=lambda trans: trans.field_value or trans.table_name == TableName.FEED_INFO
        ),
        'record_sub_id': Field(
            conditional_required=lambda trans: trans.table_name == TableName.STOP_TIMES and trans.record_id
        ),
        'field_value': Field(
            conditional_required=lambda trans: not trans.record_id,
            conditional_forbidden=lambda trans: trans.table_name == TableName.FEED_INFO or trans.record_id
        )
    }
