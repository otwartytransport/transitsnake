from dataclasses import dataclass
from typing import ClassVar, Optional, Dict
from .common import BaseDatasetType, Field
from .validation import url, email


@dataclass
class Attribution(BaseDatasetType):
    filename: ClassVar[str] = 'attributions.txt'
    primary_key: ClassVar[tuple] = ('attribution_id',)

    organization_name: str
    attribution_id: Optional[str] = None
    agency_id: Optional[str] = None
    route_id: Optional[str] = None
    trip_id: Optional[str] = None
    is_producer: Optional[bool] = None
    is_operator: Optional[bool] = None
    is_authority: Optional[bool] = None
    attribution_url: Optional[str] = None
    attribution_email: Optional[str] = None
    attribution_phone: Optional[str] = None

    meta: ClassVar[Dict[str, Field]] = {
        'attribution_url': Field(validators=url),
        'attribution_email': Field(validators=email),
    }
