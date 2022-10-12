import datetime
from enum import Enum

from . import BaseDatasetType


class Operation(Enum):
    AVAILABLE = 1
    UNAVAILABLE = 0


class Calendar(BaseDatasetType):
    filename = 'calendar.txt'

    def __init__(
            self,
            service_id: str,
            monday: Operation,
            tuesday: Operation,
            wednesday: Operation,
            thursday: Operation,
            friday: Operation,
            saturday: Operation,
            sunday: Operation,
            start_date: datetime.datetime,
            end_date: datetime.datetime
    ):
        self.service_id = service_id
        self.monday = monday
        self.tuesday = tuesday
        self.wednesday = wednesday
        self.thursday = thursday
        self.friday = friday
        self.saturday = saturday
        self.sunday = sunday
        self.start_date = start_date
        self.end_date = end_date
