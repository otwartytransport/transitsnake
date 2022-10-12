from . import BaseDatasetType


class Level(BaseDatasetType):
    filename = 'levels.txt'

    def __init__(
            self,
            level_id: str,
            level_index: float,
            level_name: str | None = None
    ):
        self.level_id = level_id
        self.level_index = level_index
        self.level_name = level_name
