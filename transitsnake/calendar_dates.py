import datetime
from dataclasses import dataclass
from enum import Enum
from typing import ClassVar

from . import BaseDatasetType


class ExceptionType(Enum):
    SERVICE_ADDED = 1
    SERVICE_REMOVED = 2


@dataclass
class CalendarDate(BaseDatasetType):
    filename: ClassVar[str] = 'calendar_dates.txt'
    primary_key: ClassVar[tuple] = ('service_id', 'date')

    service_id: str
    date: datetime.date
    exception_type: ExceptionType
