import datetime
from dataclasses import dataclass
from typing import ClassVar, Annotated

from transitsnake.common import BaseDatasetType, NonStrictEnum


class Operation(NonStrictEnum):
    UNSUPPORTED_VALUE = -1  # Not a part of GTFS Specification

    AVAILABLE = 1
    UNAVAILABLE = 0


@dataclass
class Calendar(BaseDatasetType):
    filename: ClassVar[str] = 'calendar.txt'
    primary_key: ClassVar[tuple] = ('service_id',)

    service_id: str
    monday: Operation
    tuesday: Operation
    wednesday: Operation
    thursday: Operation
    friday: Operation
    saturday: Operation
    sunday: Operation
    start_date: datetime.date
    end_date: datetime.date
