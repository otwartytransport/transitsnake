import dataclasses
import functools
import typing


@functools.cache
def get_optional_fields(instance):
    fields = dataclasses.fields(instance)
    return [field.name for field in fields if is_optional(field.type)]


def is_optional(field):
    return typing.get_origin(field) is typing.Union and \
           type(None) in typing.get_args(field)
