from dataclasses import dataclass
from typing import ClassVar, Optional, List, Dict

from transitsnake.common import BaseDatasetType, Field
from transitsnake.validation import non_negative


class Point:
    def __init__(self, lon: float, lat: float):
        self.lon = lon
        self.lat = lat


@dataclass
class Shape(BaseDatasetType):
    filename: ClassVar[str] = 'shapes.txt'
    primary_key: ClassVar[tuple] = ('shape_id', 'shape_pt_sequence')
    partial_keys: ClassVar[List[tuple]] = [('shape_id',)]

    shape_id: str
    shape_pt_lat: float
    shape_pt_lon: float
    shape_pt_sequence: int
    shape_dist_traveled: Optional[float] = None

    meta: ClassVar[Dict[str, Field]] = {
        'shape_pt_sequence': Field(validators=non_negative),
        'shape_dist_traveled': Field(validators=non_negative),
    }

    @staticmethod
    def path(shape_id: str, points: List[Point]):
        return [
            Shape(
                shape_id=shape_id,
                shape_pt_lat=point.lat,
                shape_pt_lon=point.lon,
                shape_pt_sequence=i
            )
            for i, point in enumerate(points)
        ]
