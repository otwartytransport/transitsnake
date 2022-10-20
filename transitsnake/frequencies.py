import datetime
from dataclasses import dataclass
from enum import Enum
from typing import ClassVar, Optional

from . import BaseDatasetType


class ExactTimes(Enum):
    FREQUENCY_BASED = 0
    SCHEDULE_BASED = 1


@dataclass
class Frequency(BaseDatasetType):
    filename: ClassVar[str] = 'frequencies.txt'
    primary_key: ClassVar[tuple] = ('trip_id', 'start_time')

    trip_id: str
    start_time: datetime.time
    end_time: datetime.time
    headway_secs: int
    exact_times: Optional[ExactTimes] = None
