from dataclasses import dataclass
from typing import ClassVar, Optional

from transitsnake import BaseDatasetType


@dataclass
class FareLegRule(BaseDatasetType):
    filename: ClassVar[str] = 'fare_leg_rules.txt'
    primary_key: ClassVar[tuple] = ('network_id', 'from_area_id', 'to_area_id', 'fare_product_id')

    fare_product_id: str
    leg_group_id: Optional[str] = None
    network_id: Optional[str] = None
    from_area_id: Optional[str] = None
    to_area_id: Optional[str] = None
