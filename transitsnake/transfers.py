from dataclasses import dataclass
from enum import Enum
from typing import Optional

from . import BaseDatasetType, Field
from .validation import non_negative


class TransferType(Enum):
    RECOMMENDED = 0
    TIMED = 1
    MINIMUM_TIME = 2
    IMPOSSIBLE = 3


@dataclass
class Transfer(BaseDatasetType):
    filename = 'transfers.txt'

    transfer_type: TransferType
    from_stop_id: Optional[str] = None
    to_stop_id: Optional[str] = None
    from_route_id: Optional[str] = None
    to_route_id: Optional[str] = None
    from_trip_id: Optional[str] = None
    to_trip_id: Optional[str] = None
    min_transfer_time: Optional[int] = None

    _meta = {
        'min_transfer_time': Field(validators=non_negative)
    }
