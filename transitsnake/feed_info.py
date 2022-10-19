import datetime
from dataclasses import dataclass
from typing import Optional, ClassVar

from . import BaseDatasetType


@dataclass
class FeedInfo(BaseDatasetType):
    filename: ClassVar[str] = 'feed_info.txt'

    feed_publisher_name: str
    feed_publisher_url: str
    feed_lang: str
    default_lang: Optional[str] = None
    feed_start_date: Optional[datetime.datetime] = None
    feed_end_date: Optional[datetime.datetime] = None
    feed_version: Optional[str] = None
    feed_contact_email: Optional[str] = None
    feed_contact_url: Optional[str] = None
