from collections import defaultdict

from . import BaseDatasetType


class Feed:
    def __init__(self):
        self.data = defaultdict(list)

    def add(self, *args: BaseDatasetType | list[BaseDatasetType]):
        for arg in args:
            if isinstance(arg, list):
                for subarg in arg:
                    self.data[subarg.__class__].append(subarg)
            else:
                self.data[arg.__class__].append(arg)