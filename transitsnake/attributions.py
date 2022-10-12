from . import BaseDatasetType
from .types import URL, Email


class Attribution(BaseDatasetType):
    filename = 'attributions.txt'

    def __init__(
            self,
            organization_name: str,
            attribution_id: str | None = None,
            agency_id: str | None = None,
            route_id: str | None = None,
            trip_id: str | None = None,
            is_producer: bool | None = None,
            is_operator: bool | None = None,
            is_authority: bool | None = None,
            attribution_url: URL | None = None,
            attribution_email: Email | None = None,
            attribution_phone: str | None = None
    ):
        self.organization_name = organization_name
        self.attribution_id = attribution_id
        self.agency_id = agency_id
        self.route_id = route_id
        self.trip_id = trip_id
        self.is_producer = is_producer
        self.is_operator = is_operator
        self.is_authority = is_authority
        self.attribution_url = attribution_url
        self.attribution_email = attribution_email
        self.attribution_phone = attribution_phone
