import logging

from .darksky import DarkSky
from .darksky import weather
from .weather import Weather
from .weather import DataBlock
from .weather import Now
from .weather import Day
from .weather import Hour
from .weather import Minute
from .weather import Alert
from .weather import Flag

from .weather import NoDataError
from .weather import RequiredDataError

__version__ = "2.0"
__status__ = "Release"

logging.getLogger(__name__).setLevel(logging.DEBUG)
logging.getLogger(__name__).addHandler(logging.NullHandler())
