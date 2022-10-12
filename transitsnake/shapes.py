from . import BaseDatasetType
from .types import Latitude, Longitude, Point


class Shape(BaseDatasetType):
    filename = 'shapes.txt'

    def __init__(
            self,
            shape_id: str,
            shape_pt_lat: Latitude,
            shape_pt_lon: Longitude,
            shape_pt_sequence: int,
            shape_dist_traveled: float | None = None
    ):
        self.shape_id = shape_id
        self.shape_pt_lat = shape_pt_lat
        self.shape_pt_lon = shape_pt_lon
        self.shape_pt_sequence = shape_pt_sequence
        self.shape_dist_traveled = shape_dist_traveled

    @staticmethod
    def path(shape_id: str, points: list[Point]):
        return [
            Shape(shape_id, point.lat, point.lon, i)
            for i, point in enumerate(points)
        ]
