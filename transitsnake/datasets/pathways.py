from dataclasses import dataclass
from typing import ClassVar, Optional, Dict

from transitsnake.common import BaseDatasetType, Field, NonStrictEnum
from transitsnake.validation import positive, non_negative


class PathwayMode(NonStrictEnum):
    UNSUPPORTED_VALUE = -1  # Not a part of GTFS Specification

    WALKWAY = 1
    STAIRS = 2
    MOVING_SIDEWALK = 3
    ESCALATOR = 4
    ELEVATOR = 5
    FARE_GATE = 6
    EXIT_GATE = 7


class IsBidirectional(NonStrictEnum):
    UNSUPPORTED_VALUE = -1  # Not a part of GTFS Specification

    UNIDIRECTIONAL = 0
    BIDIRECTIONAL = 1


@dataclass
class Pathway(BaseDatasetType):
    filename: ClassVar[str] = 'pathways.txt'
    primary_key: ClassVar[tuple] = ('pathway_id',)

    pathway_id: str
    from_stop_id: str
    to_stop_id: str
    pathway_mode: PathwayMode
    is_bidirectional: IsBidirectional
    length: Optional[float] = None
    traversal_time: Optional[int] = None
    stair_count: Optional[int] = None
    max_slope: Optional[float] = None
    min_width: Optional[float] = None
    signposted_as: Optional[str] = None
    reversed_signposted_as: Optional[str] = None

    meta: ClassVar[Dict[str, Field]] = {
        'length': Field(validators=non_negative),
        'traversal_time': Field(validators=positive),
        'min_width': Field(validators=positive)
    }
