from dataclasses import dataclass
from typing import Optional, ClassVar, Dict

from transitsnake.common import BaseDatasetType, Field, NonStrictEnum
from transitsnake.validation import non_negative


class TransferType(NonStrictEnum):
    UNSUPPORTED_VALUE = -1  # Not a part of GTFS Specification

    RECOMMENDED = 0
    TIMED = 1
    MINIMUM_TIME = 2
    IMPOSSIBLE = 3
    IN_SEAT = 4
    IN_SEAT_FORBIDDEN = 5


@dataclass
class Transfer(BaseDatasetType):
    filename: ClassVar[str] = 'transfers.txt'
    primary_key: ClassVar[tuple] = ('from_stop_id', 'to_stop_id', 'from_trip_id', 'to_trip_id', 'from_route_id', 'to_route_id')

    transfer_type: TransferType
    from_stop_id: Optional[str] = None
    to_stop_id: Optional[str] = None
    from_route_id: Optional[str] = None
    to_route_id: Optional[str] = None
    from_trip_id: Optional[str] = None
    to_trip_id: Optional[str] = None
    min_transfer_time: Optional[int] = None

    @staticmethod
    def in_seat_check(transfer):
        return transfer.transfer_type in [TransferType.IN_SEAT, TransferType.IN_SEAT_FORBIDDEN]

    meta: ClassVar[Dict[str, Field]] = {
        'min_transfer_time': Field(validators=non_negative),
        'from_stop_id': Field(conditional_required=in_seat_check),
        'to_stop_id': Field(conditional_required=in_seat_check),
        'from_trip_id': Field(conditional_required=in_seat_check),
        'to_trip_id': Field(conditional_required=in_seat_check)
    }
