from collections import defaultdict
from typing import List, Union

from . import BaseDatasetType


class Repository(dict):
    def __init__(self):
        super().__init__()

    def append(self, entry: BaseDatasetType):
        primary_key = entry.primary_key_values()
        if primary_key not in self:
            self[primary_key] = list()

        self[primary_key].append(entry)

    def __iter__(self):
        for key, value in self.items():
            if isinstance(value, list):
                for entry in value:
                    yield entry
            else:
                yield value


class Feed:
    def __init__(self):
        self.data = defaultdict(Repository)

    def add(self, *args: Union[BaseDatasetType, List[BaseDatasetType]]):
        for arg in args:
            if isinstance(arg, list):
                for subarg in arg:
                    self.data[subarg.__class__].append(subarg)
            else:
                self.data[arg.__class__].append(arg)
