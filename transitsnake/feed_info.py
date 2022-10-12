import datetime

from . import BaseDatasetType
from .types import URL, Email


class FeedInfo(BaseDatasetType):
    filename = 'feed_info.txt'

    def __init__(
            self,
            feed_publisher_name: str,
            feed_publisher_url: URL,
            feed_lang: str,
            default_lang: str | None = None,
            feed_start_date: datetime.datetime | None = None,
            feed_end_date: datetime.datetime | None = None,
            feed_version: str | None = None,
            feed_contact_email: Email | None = None,
            feed_contact_url: URL | None = None
    ):
        self.feed_publisher_name = feed_publisher_name
        self.feed_publisher_url = feed_publisher_url
        self.feed_lang = feed_lang
        self.default_lang = default_lang
        self.feed_start_date = feed_start_date
        self.feed_end_date = feed_end_date
        self.feed_version = feed_version
        self.feed_contact_email = feed_contact_email
        self.feed_contact_url = feed_contact_url
