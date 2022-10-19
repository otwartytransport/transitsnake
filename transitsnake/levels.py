from dataclasses import dataclass
from typing import ClassVar, Optional

from . import BaseDatasetType


@dataclass
class Level(BaseDatasetType):
    filename: ClassVar[str] = 'levels.txt'

    level_id: str
    level_index: float
    level_name: Optional[str] = None
