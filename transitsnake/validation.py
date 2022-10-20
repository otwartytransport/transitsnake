import re
from typing import Callable, Union, Any, Dict, Type, List

import validators as valid


class Field:
    def __init__(
            self,
            validators: Union[list[Callable[[Any], None]], Callable[[Any], None]] = None,
            conditional_required: Callable[[Any], bool] = None,
            global_conditional_required: Callable[[Any, Dict[Type, List[Any]]], bool] = None,
            conditional_forbidden: Callable[[Any], bool] = None
    ):
        self.conditional_required = conditional_required
        self.global_conditional_required = global_conditional_required
        self.conditional_forbidden = conditional_forbidden
        self.validators = validators

    def validate(self, field_name, type_instance, field_value):
        if field_value is None:
            if self.conditional_required and self.conditional_required(type_instance):
                raise ValueError(f'"{field_name}" is conditionally required')
            elif type_instance.__annotations__[field_name]._name == 'Optional':
                return
        elif self.conditional_forbidden and self.conditional_forbidden(type_instance):
            raise ValueError(f'"{field_name}" is conditionally forbidden')

        if not self.validators:
            return

        if isinstance(self.validators, list):
            for validator_func in self.validators:
                validator_func(field_value)
        else:
            self.validators(field_value)


def validator(fields: Union[str, List[str]] = None):
    def outer_wrapper(f):
        def inner_wrapper(*args, **kwargs):
            return f(*args, **kwargs)

        inner_wrapper._is_validator = True
        return inner_wrapper

    return outer_wrapper


def global_validator(fields: Union[str, List[str]] = None):
    def outer_wrapper(f):
        def inner_wrapper(*args, **kwargs):
            return f(*args, **kwargs)

        inner_wrapper._is_global_validator = True
        return inner_wrapper

    return outer_wrapper


def url(value):
    result = valid.url(value)
    if result is not True:
        raise ValueError(f'invalid url "{result.value}"')


def email(value):
    result = valid.email(value)
    if result is not True:
        raise ValueError(f'invalid email "{result.value}"')


def non_negative(value):
    if value < 0:
        raise ValueError('is negative')


def positive(value):
    if value <= 0:
        raise ValueError('is non positive')


def longitude(value):
    if value < -180 or value > 180:
        raise ValueError('invalid longitude')


def latitude(value):
    if value < -90 or value > 90:
        raise ValueError('invalid latitude')


color_regex = re.compile(
    r'[A-Fa-f0-9]{6}'
)


def color(value):
    m = color_regex.fullmatch(value)
    if not m:
        raise ValueError('invalid color format')


_type_validators = {
    'url': [url]
}
