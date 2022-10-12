import datetime
from enum import Enum

from . import BaseDatasetType


class ExceptionType(Enum):
    SERVICE_ADDED = 1
    SERVICE_REMOVED = 2


class CalendarDate(BaseDatasetType):
    filename = 'calendar_dates.txt'

    def __init__(
            self,
            service_id: str,
            date: datetime.date,
            exception_type: ExceptionType
    ):
        self.service_id = service_id
        self.date = date
        self.exception_type = exception_type
