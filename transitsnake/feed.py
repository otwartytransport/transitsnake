from typing import List, Union

from . import BaseDatasetType
from .agency import Agency
from .areas import Area
from .attributions import Attribution
from .calendar import Calendar
from .calendar_dates import CalendarDate
from .feed_info import FeedInfo
from .frequencies import Frequency
from .levels import Level
from .pathways import Pathway
from .routes import Route
from .shapes import Shape
from .stop_areas import StopArea
from .stop_times import StopTime
from .stops import Stop
from .transfers import Transfer
from .translations import Translation
from .trips import Trip


class Repository(dict):
    def __init__(self, cls):
        self.cls = cls
        self.partial_keys = dict()
        super().__init__()

    def append(self, entry: BaseDatasetType):
        primary_value = entry.primary_key_values()
        self[primary_value] = entry

        partial_keys_values = entry.partial_keys_values()
        for partial_key, value in partial_keys_values.items():
            if (partial_key, value) not in self.partial_keys:
                self.partial_keys[(partial_key, value)] = []
            self.partial_keys[(partial_key, value)].append(entry)

    def get_by_partial_key(self, partial_key, value):
        return self.partial_keys[(partial_key, value)]

    def set_by_partial_key(self, partial_key, value, item):
        self.partial_keys[(partial_key, value)] = item

    def has_by_partial_key(self, partial_key, value):
        return (partial_key, value) in self.partial_keys

    def __iter__(self):
        for key, value in self.items():
            if isinstance(value, list):
                for entry in value:
                    yield entry
            else:
                yield value


class Feed:
    def __init__(self):
        self.data = dict(((cls, Repository(cls)) for cls in [
            Agency, Area, Attribution, Calendar, CalendarDate, FeedInfo,
            Frequency, Level, Pathway, Route, Shape, StopArea, StopTime,
            Stop, Transfer, Translation, Trip
        ]))

    def add(self, *args: Union[BaseDatasetType, List[BaseDatasetType]]):
        for arg in args:
            if isinstance(arg, list):
                for subarg in arg:
                    self.data[subarg.__class__].append(subarg)
            else:
                self.data[arg.__class__].append(arg)
