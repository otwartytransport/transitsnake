from . import BaseDatasetType


class Area(BaseDatasetType):
    filename = 'areas.txt'

    def __init__(
            self,
            area_id: str,
            area_name: str | None = None
    ):
        self.area_id = area_id
        self.area_name = area_name
