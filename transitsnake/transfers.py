from enum import Enum

from . import BaseDatasetType


class TransferType(Enum):
    RECOMMENDED = 0
    TIMED = 1
    MINIMUM_TIME = 2
    IMPOSSIBLE = 3


class Transfer(BaseDatasetType):
    filename = 'transfers.txt'

    def __init__(
            self,
            transfer_type: TransferType,
            from_stop_id: str | None = None,
            to_stop_id: str | None = None,
            from_route_id: str | None = None,
            to_route_id: str | None = None,
            from_trip_id: str | None = None,
            to_trip_id: str | None = None,
            min_transfer_time: int | None = None
    ):
        self.transfer_type = transfer_type
        self.from_stop_id = from_stop_id
        self.to_stop_id = to_stop_id
        self.from_route_id = from_route_id
        self.to_route_id = to_route_id
        self.from_trip_id = from_trip_id
        self.to_trip_id = to_trip_id
        self.min_transfer_time = min_transfer_time
