import abc
import re
from urllib.parse import urlparse
import pytz


class BaseType(metaclass=abc.ABCMeta):
    def __init__(self, value):
        self._value = None
        self.value = value

    def __str__(self):
        return self.value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self.validator(new_value)
        self._value = new_value

    @abc.abstractmethod
    def validator(self, value):
        pass


class Color(BaseType):
    def validator(self, value):
        if not re.match(r'^[A-Fa-f0-9]{6}$', value):
            raise ValueError('invalid color')


class Email(BaseType):
    def validator(self, value):
        pass


class Latitude(BaseType):
    def validator(self, value):
        if value < -90.0 or value > 90.0:
            raise ValueError('invalid latitude')


class Longitude(BaseType):
    def validator(self, value):
        if value < -180.0 or value > 180.0:
            raise ValueError('invalid longitude')


class Point:
    def __init__(self, lon: Longitude, lat: Latitude):
        self.lon = lon
        self.lat = lat


class Timezone(BaseType):
    def validator(self, value):
        if value not in pytz.all_timezones:
            raise ValueError('invalid timezone')


class NonNegativeInt(BaseType):
    def validator(self, value):
        if value < 0:
            raise ValueError('number have to be non-negative')


class NonNegativeFloat(BaseType):
    def validator(self, value):
        if value < 0.0:
            raise ValueError('number have to be non-negative')


class URL(BaseType):
    @staticmethod
    def is_url(url):
        try:
            result = urlparse(url)
            return all([result.scheme in ['http', 'https'], result.netloc])
        except ValueError:
            return False

    def validator(self, value):
        if not self.is_url(value):
            raise ValueError('invalid url')
