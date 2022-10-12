import datetime
from enum import Enum

from . import BaseDatasetType


class ExactTimes(Enum):
    FREQUENCY_BASED = 0
    SCHEDULE_BASED = 1


class Frequency(BaseDatasetType):
    filename = 'frequencies.txt'

    def __init__(
            self,
            trip_id: str,
            start_time: datetime.time,
            end_time: datetime.time,
            headway_secs: int,
            exact_times: ExactTimes | None = None
    ):
        self.trip_id = trip_id
        self.start_time = start_time
        self.end_time = end_time
        self.headway_secs = headway_secs
        self.exact_times = exact_times
