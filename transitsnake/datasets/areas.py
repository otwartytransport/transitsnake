from dataclasses import dataclass
from typing import ClassVar, Optional

from transitsnake.common import BaseDatasetType


@dataclass
class Area(BaseDatasetType):
    filename: ClassVar[str] = 'areas.txt'
    primary_key: ClassVar[tuple] = ('area_id',)

    area_id: str
    area_name: Optional[str] = None
