from dataclasses import dataclass

from . import BaseDatasetType


@dataclass
class StopArea(BaseDatasetType):
    filename = 'stop_areas.txt'

    area_id: str
    stop_id: str
