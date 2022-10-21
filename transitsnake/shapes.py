from dataclasses import dataclass
from typing import ClassVar, Optional, List

from . import BaseDatasetType, Field
from .types import Point
from .validation import non_negative


@dataclass
class Shape(BaseDatasetType):
    filename: ClassVar[str] = 'shapes.txt'
    primary_key: ClassVar[tuple] = ('shape_id', 'shape_pt_sequence')

    shape_id: str
    shape_pt_lat: float
    shape_pt_lon: float
    shape_pt_sequence: int
    shape_dist_traveled: Optional[float] = None

    _meta = {
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
