import logging

from .darksky import DarkSky
from .darksky import weather
from .weather import Weather

from .weather import NoDataError

__version__ = "1.0"
__status__ = "Release"

logging.getLogger(__name__).setLevel(logging.DEBUG)
logging.getLogger(__name__).addHandler(logging.NullHandler())
