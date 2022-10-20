from dataclasses import dataclass
from typing import ClassVar

from . import BaseDatasetType


@dataclass
class StopArea(BaseDatasetType):
    filename = 'stop_areas.txt'
    primary_key: ClassVar[tuple] = ('area_id', 'stop_id')

    area_id: str
    stop_id: str
