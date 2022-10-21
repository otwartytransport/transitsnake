from dataclasses import dataclass
from typing import Optional, ClassVar, Dict

from .common import BaseDatasetType
from .validation import Field, url, email


@dataclass
class Agency(BaseDatasetType):
    filename: ClassVar[str] = 'agency.txt'
    primary_key: ClassVar[tuple] = ('agency_id',)

    agency_name: str
    agency_url: str
    agency_timezone: str
    agency_id: Optional[str] = None
    agency_lang: Optional[str] = None
    agency_phone: Optional[str] = None
    agency_fare_url: Optional[str] = None
    agency_email: Optional[str] = None

    meta: ClassVar[Dict[str, Field]] = {
        'agency_id': Field(global_conditional_required=lambda full, dataset: len(dataset[Agency]) > 1),
        'agency_url': Field(validators=url),
        'agency_fare_url': Field(validators=url),
        'agency_email': Field(validators=email),
    }
