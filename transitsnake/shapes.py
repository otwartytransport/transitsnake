from typing import ClassVar, Optional, List

from pydantic import BaseModel, NonNegativeInt, NonNegativeFloat

from . import BaseDatasetType
from .types import Point


class Shape(BaseModel, BaseDatasetType):
    filename: ClassVar[str] = 'shapes.txt'

    shape_id: str
    shape_pt_lat: float
    shape_pt_lon: float
    shape_pt_sequence: NonNegativeInt
    shape_dist_traveled: Optional[NonNegativeFloat]

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
