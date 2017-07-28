import requests
import logging

from .weather import Weather

__author__ = "PvtHaggard"

__license__ = "GPLv3"
__version__ = "N/A"
__maintainer__ = "PvtHaggard"
__email__ = "pvtgaggard@gmail.com"
__status__ = "Development Pre-alpha"

log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())


class DarkSkyPy:
    def __init__(self, api_key=None):
        self._api_key = None
        self._latitude = None
        self._longitude = None
        self._response = None
        self._weather = None

        self.api_key = api_key

    @property
    def api_key(self):
        return self._api_key

    @property
    def latitude(self):
        return self._latitude

    @property
    def longitude(self):
        return self._longitude

    @property
    def url(self):
        if self.latitude is None or self.longitude is None:
            log.warning("Can't build url, longitude or latitude is 'None'. Returning 'None'")
            return None
        return "https://api.darksky.net/forecast/{}/{},{}".format(self.api_key, self.latitude, self.longitude)

    @property
    def api_call_count(self):
        try:
            return self._response.headers["x-forecast-api-calls"]
        except AttributeError as e:
            log.warning(e)
            return None

    @property
    def response_time(self):
        try:
            return self._response.headers["x-response-time"]
        except AttributeError as e:
            log.warning(e)
            return None

    @property
    def response_date(self):
        try:
            return self._response.headers["date"]
        except AttributeError as e:
            log.warning(e)
            return None

    @property
    def response_status_code(self):
        try:
            return self._response.status_code
        except AttributeError as e:
            log.warning(e)
            return None

    @api_key.setter
    def api_key(self, api_key: str):
        if type(api_key) is not str:
            raise TypeError("api key must be 'str'. Received type {}".format(type(api_key)))

        if len(api_key) != 32:
            raise ValueError("api key must be 32 characters long.")

        self._api_key = api_key

    @latitude.setter
    def latitude(self, latitude: float):
        self._latitude = float(latitude)

    @longitude.setter
    def longitude(self, longitude: float):
        self._longitude = float(longitude)

    def weather(self, latitude=None, longitude=None):
        if latitude is not None:
            self.latitude = latitude
        if longitude is not None:
            self.longitude = longitude

        if self.url is None:
            return None

        self._response = requests.get(self.url)
        if self._response.status_code == 200:
            self._weather = Weather(self._response.text)
            return self._weather
