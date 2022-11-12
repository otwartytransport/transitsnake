import datetime
from dataclasses import dataclass
from typing import ClassVar, Annotated

from dataclass_wizard import Pattern

from transitsnake.common import BaseDatasetType, NonStrictEnum


class ExceptionType(NonStrictEnum):
    UNSUPPORTED_VALUE = -1  # Not a part of GTFS Specification

    SERVICE_ADDED = 1
    SERVICE_REMOVED = 2


@dataclass
class CalendarDate(BaseDatasetType):
    filename: ClassVar[str] = 'calendar_dates.txt'
    primary_key: ClassVar[tuple] = ('service_id', 'date')

    service_id: str
    date: Annotated[datetime.date, Pattern('%Y%m%d')]
    exception_type: ExceptionType
