from dataclasses import dataclass
from typing import ClassVar, Optional, Dict

from transitsnake.common import BaseDatasetType, Field, NonStrictEnum


class FareTransferType(NonStrictEnum):
    UNSUPPORTED_VALUE = -1  # Not a part of GTFS Specification

    A_PLUS_AB = 0
    A_PLUS_AB_PLUS_B = 1
    AB = 2


class DurationLimitType(NonStrictEnum):
    UNSUPPORTED_VALUE = -1  # Not a part of GTFS Specification

    DEPARTURE_TO_ARRIVAL = 0
    DEPARTURE_TO_DEPARTURE = 1
    ARRIVAL_TO_DEPARTURE = 2
    ARRIVAL_TO_ARRIVAL = 3


@dataclass
class FareTransferRule(BaseDatasetType):
    filename: ClassVar[str] = 'fare_transfer_rules.txt'
    primary_key: ClassVar[tuple] = ('from_leg_group_id', 'to_leg_group_id', 'fare_product_id', 'transfer_count', 'duration_limit')

    fare_transfer_type: FareTransferType
    to_leg_group_id: Optional[str] = None
    transfer_count: Optional[int] = None
    duration_limit: Optional[str] = None
    duration_limit_type: Optional[DurationLimitType] = None
    from_leg_group_id: Optional[str] = None
    fare_product_id: Optional[str] = None

    meta: ClassVar[Dict[str, Field]] = {
        'transfer_count': Field(
            conditional_forbidden=lambda rule: rule.from_leg_group_id != rule.to_leg_group_id,
            conditional_required=lambda rule: rule.from_leg_group_id == rule.to_leg_group_id,
        ),
        'duration_limit_type': Field(
            conditional_required=lambda rule: rule.duration_limit is not None,
            conditional_forbidden=lambda rule: rule.duration_limit is None
        )
    }
