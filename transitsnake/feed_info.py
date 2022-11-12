import datetime
from dataclasses import dataclass
from typing import Optional, ClassVar, Annotated

from dataclass_wizard import Pattern

from .common import BaseDatasetType


@dataclass
class FeedInfo(BaseDatasetType):
    filename: ClassVar[str] = 'feed_info.txt'
    primary_key: ClassVar[tuple] = None

    feed_publisher_name: str
    feed_publisher_url: str
    feed_lang: str
    default_lang: Optional[str] = None
    feed_start_date: Optional[Annotated[datetime.date, Pattern('%Y%m%d')]] = None
    feed_end_date: Optional[Annotated[datetime.date, Pattern('%Y%m%d')]] = None
    feed_version: Optional[str] = None
    feed_contact_email: Optional[str] = None
    feed_contact_url: Optional[str] = None
