from enum import Enum

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


class Translation(BaseDatasetType):
    filename = 'translations.txt'

    def __init__(
            self,
            table_name: TableName,
            field_name: str,
            language: str,
            translation: str,
            record_id: str | None = None,
            record_sub_id: str | None = None,
            field_value: str | None = None
    ):
        self.table_name = table_name
        self.field_name = field_name
        self.language = language
        self.translation = translation
        self.record_id = record_id
        self.record_sub_id = record_sub_id
        self.field_value = field_value
