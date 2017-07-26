import requests
import logging

__author__ = "PvtHaggard"

log = logging.getLogger(__name__)


class DarkSkyPy:
    def __init__(self, api_key=None):
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

    # TODO: Return None or raise Exception?
    @property
    def url(self):
        try:
            return "https://api.darksky.net/forecast/{}/{},{}".format(self.api_key, self.latitude, self.longitude)
        except AttributeError:
            log.warning("Can't build URL longitude or latitude not defined")
            return None

    @api_key.setter
    def api_key(self, api_key: str):
        if len(api_key) == 32:
            self._api_key = api_key
        else:
            raise ValueError("API key must be 32 characters long.")

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

        if self.url is not None:
            response = requests.get(self.url)
        '''
        .text
        headers: date, x-forecast-api-calls, x-response-time

        '''

