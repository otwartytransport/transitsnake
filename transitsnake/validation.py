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


currency_codes = [
    'ADP', 'AED', 'AFA', 'AFN', 'ALK', 'ALL', 'AMD', 'ANG', 'ANG', 'ANG', 'AOA', 'AOK', 'AON', 'AOR', 'ARA', 'ARP', 'ARS', 'ARY', 'ATS', 'AUD', 'AUD', 'AUD', 'AUD', 'AUD',
    'AUD', 'AUD', 'AUD', 'AWG', 'AYM', 'AZM', 'AZN', 'BAD', 'BAM', 'BBD', 'BDT', 'BEC', 'BEF', 'BEL', 'BGJ', 'BGK', 'BGL', 'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BOP',
    'BOV', 'BRB', 'BRC', 'BRE', 'BRL', 'BRN', 'BRR', 'BSD', 'BTN', 'BUK', 'BWP', 'BYB', 'BYN', 'BYR', 'BZD', 'CAD', 'CDF', 'CHC', 'CHE', 'CHF', 'CHF', 'CHW', 'CLF', 'CLP',
    'CNY', 'COP', 'COU', 'CRC', 'CSD', 'CSJ', 'CSK', 'CUC', 'CUP', 'CVE', 'CYP', 'CZK', 'DDM', 'DEM', 'DJF', 'DKK', 'DKK', 'DKK', 'DOP', 'DZD', 'ECS', 'ECV', 'EEK', 'EGP',
    'ERN', 'ESA', 'ESB', 'ESP', 'ESP', 'ETB', 'EUR', 'EUR', 'EUR', 'EUR', 'EUR', 'EUR', 'EUR', 'EUR', 'EUR', 'EUR', 'EUR', 'EUR', 'EUR', 'EUR', 'EUR', 'EUR', 'EUR', 'EUR',
    'EUR', 'EUR', 'EUR', 'EUR', 'EUR', 'EUR', 'EUR', 'EUR', 'EUR', 'EUR', 'EUR', 'EUR', 'EUR', 'EUR', 'EUR', 'EUR', 'EUR', 'EUR', 'FIM', 'FIM', 'FJD', 'FKP', 'FRF', 'FRF',
    'FRF', 'FRF', 'FRF', 'FRF', 'FRF', 'FRF', 'FRF', 'FRF', 'FRF', 'FRF', 'GBP', 'GBP', 'GBP', 'GBP', 'GEK', 'GEL', 'GHC', 'GHP', 'GHS', 'GIP', 'GMD', 'GNE', 'GNF', 'GNS',
    'GQE', 'GRD', 'GTQ', 'GWE', 'GWP', 'GYD', 'HKD', 'HNL', 'HRD', 'HRK', 'HRK', 'HTG', 'HUF', 'IDR', 'IDR', 'IEP', 'ILP', 'ILR', 'ILS', 'INR', 'INR', 'IQD', 'IRR', 'ISJ',
    'ISK', 'ITL', 'ITL', 'ITL', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KMF', 'KPW', 'KRW', 'KWD', 'KYD', 'KZT', 'LAJ', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LSM', 'LTL',
    'LTT', 'LUC', 'LUF', 'LUL', 'LVL', 'LVR', 'LYD', 'MAD', 'MAD', 'MDL', 'MGA', 'MGF', 'MKD', 'MLF', 'MMK', 'MNT', 'MOP', 'MRO', 'MRU', 'MTL', 'MTP', 'MUR', 'MVQ', 'MVR',
    'MWK', 'MWK', 'MXN', 'MXP', 'MXV', 'MYR', 'MZE', 'MZM', 'MZN', 'NAD', 'NGN', 'NIC', 'NIO', 'NLG', 'NOK', 'NOK', 'NOK', 'NPR', 'NZD', 'NZD', 'NZD', 'NZD', 'NZD', 'OMR',
    'PAB', 'PEH', 'PEI', 'PEN', 'PEN', 'PES', 'PGK', 'PHP', 'PKR', 'PLN', 'PLZ', 'PTE', 'PYG', 'QAR', 'RHD', 'ROK', 'ROL', 'RON', 'RON', 'RSD', 'RUB', 'RUR', 'RUR', 'RUR',
    'RUR', 'RUR', 'RUR', 'RUR', 'RUR', 'RUR', 'RUR', 'RUR', 'RWF', 'SAR', 'SBD', 'SCR', 'SDD', 'SDG', 'SDG', 'SDP', 'SEK', 'SGD', 'SHP', 'SIT', 'SKK', 'SLL', 'SOS', 'SRD',
    'SRG', 'SSP', 'STD', 'STN', 'SUR', 'SVC', 'SYP', 'SZL', 'SZL', 'THB', 'TJR', 'TJS', 'TMM', 'TMT', 'TND', 'TOP', 'TPE', 'TRL', 'TRY', 'TRY', 'TTD', 'TWD', 'TZS', 'UAH',
    'UAK', 'UGS', 'UGW', 'UGX', 'USD', 'USD', 'USD', 'USD', 'USD', 'USD', 'USD', 'USD', 'USD', 'USD', 'USD', 'USD', 'USD', 'USD', 'USD', 'USD', 'USD', 'USD', 'USD', 'USN',
    'USS', 'UYI', 'UYN', 'UYP', 'UYU', 'UYW', 'UZS', 'VEB', 'VEF', 'VEF', 'VEF', 'VES', 'VNC', 'VND', 'VUV', 'WST', 'XAF', 'XAF', 'XAF', 'XAF', 'XAF', 'XAF', 'XAG', 'XAU',
    'XBA', 'XBB', 'XBC', 'XBD', 'XCD', 'XCD', 'XCD', 'XCD', 'XCD', 'XCD', 'XCD', 'XCD', 'XDR', 'XEU', 'XFO', 'XFU', 'XOF', 'XOF', 'XOF', 'XOF', 'XOF', 'XOF', 'XOF', 'XOF',
    'XPD', 'XPF', 'XPF', 'XPF', 'XPT', 'XRE', 'XSU', 'XTS', 'XUA', 'XXX', 'YDD', 'YER', 'YUD', 'YUM', 'YUN', 'ZAL', 'ZAL', 'ZAR', 'ZAR', 'ZAR', 'ZMK', 'ZMW', 'ZRN', 'ZRZ',
    'ZWC', 'ZWD', 'ZWD', 'ZWL', 'ZWN', 'ZWR'
]


def currency_code(value):
    if value not in currency_codes:
        raise ValueError('invalid currency code')


_type_validators = {
    'url': [url]
}
