from dataclasses import dataclass
from typing import ClassVar, Optional

from .common import BaseDatasetType


@dataclass
class Level(BaseDatasetType):
    filename: ClassVar[str] = 'levels.txt'
    primary_key: ClassVar[tuple] = ('level_id',)

    level_id: str
    level_index: float
    level_name: Optional[str] = None
