from enum import Enum
from . import BaseDatasetType


class PathwayMode(Enum):
    WALKWAY = 1
    STAIRS = 2
    MOVING_SIDEWALK = 3
    ESCALATOR = 4
    ELEVATOR = 5
    FARE_GATE = 6
    EXIT_GATE = 7


class IsBidirectional(Enum):
    UNIDIRECTIONAL = 0
    BIDIRECTIONAL = 1


class Pathway(BaseDatasetType):
    filename = 'pathways.txt'

    def __init__(
            self,
            pathway_id: str,
            from_stop_id: str,
            to_stop_id: str,
            pathway_mode: PathwayMode,
            is_bidirectional: IsBidirectional,
            length: float | None = None,
            traversal_time: int | None = None,
            stair_count: int | None = None,
            max_slope: float | None = None,
            min_width: float | None = None,
            signposted_as: str | None = None,
            reversed_signposted_as: str | None = None
    ):
        self.pathway_id = pathway_id
        self.from_stop_id = from_stop_id
        self.to_stop_id = to_stop_id
        self.pathway_mode = pathway_mode
        self.is_bidirectional = is_bidirectional
        self.length = length
        self.traversal_time = traversal_time
        self.stair_count = stair_count
        self.max_slope = max_slope
        self.min_width = min_width
        self.signposted_as = signposted_as
        self.reversed_signposted_as = reversed_signposted_as
