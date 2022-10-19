from dataclasses import dataclass
from typing import ClassVar, Optional

from . import BaseDatasetType


@dataclass
class Area(BaseDatasetType):
    filename: ClassVar[str] = 'areas.txt'

    area_id: str
    area_name: Optional[str] = None
