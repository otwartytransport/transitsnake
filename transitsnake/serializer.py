import dataclasses
import datetime
import functools
import typing

from transitsnake.common import NonStrictEnum
from transitsnake.utils import is_optional


class FieldDefinition:
    def __init__(self, field_type, optional):
        self.field_type = field_type
        self.optional = optional


def serialize(cls, instance):
    result = dict()
    definition = get_dataset_definition(cls)

    for field_name, field_definition in definition.items():
        value = instance.__dict__[field_name]
        if value is None:
            continue

        if field_definition.field_type == datetime.date:
            result[field_name] = value.strftime("%Y%m%d")
        elif issubclass(field_definition.field_type, NonStrictEnum):
            if value.value == -1:
                result[field_name] = str(value._value)
            else:
                result[field_name] = str(value.value)
        else:
            result[field_name] = str(value)

    return result


def deserialize(cls, instance):
    result = dict()
    definition = get_dataset_definition(cls)

    for field_name, value in instance.items():
        field_definition = definition[field_name]
        if field_definition.field_type == datetime.date:
            result[field_name] = datetime.datetime.strptime(value, "%Y%m%d")
        else:
            result[field_name] = field_definition.field_type(value)

    return cls(**result)


@functools.cache
def get_dataset_definition(cls):
    fields = dataclasses.fields(cls)
    fields_definitions = dict()

    for field in fields:
        field_type = field.type
        optional = is_optional(field_type)

        args = typing.get_args(field.type)
        if optional:
            field_type = args[0]

        fields_definitions[field.name] = FieldDefinition(
            field_type=field_type,
            optional=optional
        )

    return fields_definitions
