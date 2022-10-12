from . import BaseDatasetType


class StopArea(BaseDatasetType):
    filename = 'stop_areas.txt'

    def __init__(
            self,
            area_id: str,
            stop_id: str
    ):
        self.area_id = area_id
        self.stop_id = stop_id
