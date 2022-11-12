from dataclasses import dataclass
from typing import ClassVar

from transitsnake.common import BaseDatasetType


@dataclass
class StopArea(BaseDatasetType):
    filename: ClassVar[str] = 'stop_areas.txt'
    primary_key: ClassVar[tuple] = ('area_id', 'stop_id')

    area_id: str
    stop_id: str
