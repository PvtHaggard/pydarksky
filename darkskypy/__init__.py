import logging

from .darkskypy import DarkSkyPy
from .weather import Weather


logging.getLogger(__name__).setLevel(logging.DEBUG)
logging.getLogger(__name__).addHandler(logging.NullHandler())
