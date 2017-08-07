# -*- coding: utf-8 -*-
import requests
import logging

from .weather import Weather

__author__ = "PvtHaggard"

__license__ = "GPLv3"
__version__ = "N/A"
__maintainer__ = "PvtHaggard"
__email__ = "pvtgaggard@gmail.com"
__status__ = "Development Pre-alpha"

log = logging.getLogger("darkskypy")

_languages = {"Arabic": "ar", "Azerbaijani": "az", "Belarusian": "be", "Bulgarian": "bg", "Bosnian": "bs",
              "Catalan": "ca", "Czech": "cs", "German": "de", "Greek": "el", "English": "en", "Spanish": "es",
              "Estonian": "et", "French": "fr", "Croatian": "hr", "Hungarian": "hu", "Indonesian": "id",
              "Italian": "it", "Icelandic": "is", "Georgian": "ka", "Cornish": "kw", "Norwegian Bokmål": "nb",
              "Dutch": "nl", "Polish": "pl", "Portuguese": "pt", "Russian": "ru", "Slovak": "sk",
              "Slovenian": "sl", "Serbian": "sr", "Swedish": "sv", "Tetum": "tet", "Turkish": "tr",
              "Ukrainian": "uk", "Igpay Atinlay": "x-pig-latin", "simplified Chinese": "zh",
              "traditional Chinese": "zh-tw"}

_units = ["auto", "ca", "uk2", "ui", "si"]

_excludes = ["currently", "minutely", "hourly", "daily", "alerts", "flags"]


class DarkSkyPy:
    def __init__(self, api_key=None):
        self._api_key = None
        self._latitude = None
        self._longitude = None
        self._response = None
        self._weather = None
        self._language = _languages["English"]
        self._units = "si"
        self._extend = False
        self._exclude = []

        self.api_key = api_key

    @property
    def api_key(self) -> str:
        return self._api_key

    @property
    def latitude(self) -> float:
        return self._latitude

    @property
    def longitude(self) -> float:
        return self._longitude

    '''
    Raises AssertionError
    '''
    @property
    def url(self) -> str:
        assert type(self.latitude) is float, "latitude must be <class 'float'>, is type {}".format(type(self.latitude))
        assert type(self.longitude) is float, "longitude must be <class 'float'>, is type {}".format(type(self.longitude))

        url = "https://api.darksky.net/forecast/{}/{},{}?units={}&lang={}".format(self.api_key, self.latitude,
                                                                                  self.longitude, self._units,
                                                                                  self._language)
        if len(self._exclude) > 0:
            url += "&exclude="
            for e in self._exclude:
                url += "{},".format(e)
            url = url.strip(",")

        if self._extend:
            url += "&extend=hourly"

        return url

    @property
    def languages(self):
        return _languages.keys()

    @property
    def units(self) -> str:
        return self._units

    @property
    def extend(self) -> bool:
        return self._extend

    @property
    def exclude(self):
        return self._exclude

    @property
    def excludes(self):
        return _excludes

    @property
    def api_call_count(self) -> str:
        return self._response.headers["x-forecast-api-calls"]

    @property
    def response_time(self) -> str:
        return self._response.headers["x-response-time"]

    @property
    def response_date(self) -> str:
        return self._response.headers["date"]

    @property
    def response_status_code(self):
        return self._response.status_code

    @property
    def languages(self):
        return _languages.keys()

    @property
    def response_lang(self):
        return self._language

    @property
    def units(self):
        return _units

    @property
    def response_units(self):
        return self._units

    '''
    Raises ValueError 
    '''
    @api_key.setter
    def api_key(self, api_key: str):
        api_key = str(api_key)

        if len(api_key) != 32:
            log.debug("api_key():api_key must be 32 characters long.")
            raise ValueError("api_key must be 32 characters long.")

        self._api_key = api_key

    '''
    Raises TypeError
    '''
    @latitude.setter
    def latitude(self, latitude: float):
        self._latitude = float(latitude)

    '''
    Raises TypeError
    '''
    @longitude.setter
    def longitude(self, longitude: float):
        self._longitude = float(longitude)

    '''
    Raises TypeError
    '''
    @extend.setter
    def extend(self, extend):
        self.extend = bool(extend)

    '''
    Raises TypeError
    Raises ValueError
    '''
    @exclude.setter
    def exclude(self, excludes):
        if type(excludes) is str:
            if excludes in _excludes:
                self._exclude = [excludes]
        elif type(excludes) is list:
            tmp = []
            for exclude in excludes:
                if exclude in _excludes:
                    tmp.append(exclude)
                else:
                    log.debug("exclude():'{}' is not a valid exclude value".format(exclude))
                    raise ValueError("'{}' is not a valid exclude value".format(exclude))
            self._exclude = tmp
        else:
            log.debug("exclude():excludes must be type '<class 'str'>' was type '{}'".format(type(excludes)))
            raise TypeError("excludes must be type '<class 'str'>' was type '{}'".format(type(excludes)))

    '''
    Raises KeyError
    '''
    @response_lang.setter
    def response_lang(self, language):
        self._language = _languages[language]

    '''
    Raises KeyError
    '''
    @response_units.setter
    def response_units(self, units):
        assert units in _units, "{} is not a valid unit type".format(units)
        self._units = units

    def weather(self, latitude=None, longitude=None):
        if latitude is not None:
            self.latitude = latitude
        if longitude is not None:
            self.longitude = longitude

        self._response = requests.get(self.url)
        self._response.raise_for_status()

        self._weather = Weather(self._response.text)
        return self._weather


