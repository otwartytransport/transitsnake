from typing import List, Union
from .common import BaseDatasetType
import transitsnake.datasets


class Repository(dict):
    def __init__(self, cls):
        self._cls = cls
        self._partial_keys = dict()
        super().__init__()

    def append(self, entry: BaseDatasetType):
        primary_value = entry.primary_key_values()
        self[primary_value] = entry

        partial_keys_values = entry.partial_keys_values()
        for partial_key, value in partial_keys_values.items():
            if (partial_key, value) not in self._partial_keys:
                self._partial_keys[(partial_key, value)] = []
            self._partial_keys[(partial_key, value)].append(entry)

    def get_by_partial_key(self, partial_key, value):
        if partial_key == self._cls.primary_key:
            return self[value]
        return self._partial_keys[(partial_key, value)]

    def set_by_partial_key(self, partial_key, value, item):
        if partial_key == self._cls.primary_key:
            self[value] = item
            return
        self._partial_keys[(partial_key, value)] = item

    def has_by_partial_key(self, partial_key, value):
        if partial_key == self._cls.primary_key:
            return value in self
        return (partial_key, value) in self._partial_keys

    def __iter__(self):
        for key, value in self.items():
            yield value


class Feed:
    def __init__(self):
        self.data = dict(((cls, Repository(cls)) for cls in transitsnake.datasets.types))
        self.extra_files = dict()

    def add(self, *args: Union[BaseDatasetType, List[BaseDatasetType]]):
        for arg in args:
            if isinstance(arg, list):
                for subarg in arg:
                    self.data[subarg.__class__].append(subarg)
            else:
                self.data[arg.__class__].append(arg)

    def add_extra_file(self, filename, content):
        self.extra_files[filename] = content
