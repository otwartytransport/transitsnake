import datetime
from dataclasses import dataclass
from enum import Enum
from typing import ClassVar
from . import BaseDatasetType


class Operation(Enum):
    AVAILABLE = 1
    UNAVAILABLE = 0


@dataclass
class Calendar(BaseDatasetType):
    filename: ClassVar[str] = 'calendar.txt'

    service_id: str
    monday: Operation
    tuesday: Operation
    wednesday: Operation
    thursday: Operation
    friday: Operation
    saturday: Operation
    sunday: Operation
    start_date: datetime.datetime
    end_date: datetime.datetime
