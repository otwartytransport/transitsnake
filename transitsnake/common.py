from dataclasses import dataclass
from enum import Enum
import abc
from typing import Tuple, Optional, List, Dict
from .utils import get_optional_fields
from .validation import Field


@dataclass
class BaseDatasetType(metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def filename(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def primary_key(self) -> Optional[Tuple]:
        return None

    def primary_key_values(self):
        if self.primary_key is None:
            return None

        return tuple([self.__dict__[x] for x in self.primary_key])

    @property
    def partial_keys(self) -> List[Tuple]:
        return []

    def partial_keys_values(self):
        return dict(((index, tuple([self.__dict__[x] for x in index])) for index in self.partial_keys))

    @property
    def meta(self) -> Dict[str, Field]:
        return dict()

    def global_validate(self, dataset):
        if not self.meta:
            return

        for field_name, field_definition in self.meta.items():
            if not field_definition.global_conditional_required:
                continue

            value = self.__dict__[field_name]
            if value is None and field_definition.global_conditional_required(self, dataset):
                raise ValueError(f'"{field_name}" global conditional requirements not met')

    def validate(self):
        if not self.meta:
            return

        for field_name, field_definition in self.meta.items():
            value = self.__dict__[field_name]
            if value is None and field_name in get_optional_fields(self.__class__):
                continue

            field_definition.validate(field_name, self, value)


class ContinuousPickupDropOff(Enum):
    UNSUPPORTED_VALUE = -1  # Not a part of GTFS Specification

    ALLOWED = 0
    NOT_AVAILABLE = 1
    MUST_PHONE = 2
    ON_REQUEST_TO_DRIVER = 3


class NonStrictEnum(Enum):
    @classmethod
    def _missing_(cls, value):
        if isinstance(value, str):
            return cls(int(value))
        missing = super()._missing_(value)
        if missing:
            return missing

        unknown = cls(-1)
        unknown._value = value
        return unknown
