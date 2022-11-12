from .agency import Agency
from .areas import Area
from .attributions import Attribution
from .calendar import Calendar
from .calendar_dates import CalendarDate
from .fare_leg_rules import FareLegRule
from .fare_products import FareProduct
from .fare_transfer_rules import FareTransferRule
from .feed_info import FeedInfo
from .frequencies import Frequency
from .levels import Level
from .pathways import Pathway
from .routes import Route
from .shapes import Shape
from .stop_areas import StopArea
from .stop_times import StopTime
from .stops import Stop
from .transfers import Transfer
from .translations import Translation
from .trips import Trip


types = [
    Agency, Area, Attribution, Calendar, CalendarDate, FeedInfo,
    Frequency, Level, Pathway, Route, Shape, StopArea, StopTime,
    Stop, Transfer, Translation, Trip, FareProduct, FareLegRule, FareTransferRule
]
types_filename_mappings = dict(((file_type.filename, file_type) for file_type in types))
