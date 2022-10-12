from . import BaseDatasetType
from .types import Timezone, Email, URL


class Agency(BaseDatasetType):
    filename = 'agency.txt'

    def __init__(
            self,
            agency_name: str,
            agency_url: URL,
            agency_timezone: Timezone,
            agency_id: str | None = None,
            agency_lang: str | None = None,
            agency_phone: str | None = None,
            agency_fare_url: URL | None = None,
            agency_email: Email | None = None
    ):
        self.agency_name = agency_name
        self.agency_url = agency_url
        self.agency_timezone = agency_timezone
        self.agency_id = agency_id
        self.agency_lang = agency_lang
        self.agency_phone = agency_phone
        self.agency_fare_url = agency_fare_url
        self.agency_email = agency_email
