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


class DarkSkyPy(object):
    _LANGS = {"auto": "auto", "Arabic": "ar", "Azerbaijani": "az", "Belarusian": "be", "Bulgarian": "bg",
              "Bosnian": "bs", "Catalan": "ca", "Czech": "cs", "German": "de", "Greek": "el", "English": "en",
              "Spanish": "es", "Estonian": "et", "French": "fr", "Croatian": "hr", "Hungarian": "hu",
              "Indonesian": "id", "Italian": "it", "Icelandic": "is", "Georgian": "ka", "Cornish": "kw",
              "Norwegian Bokmål": "nb", "Dutch": "nl", "Polish": "pl", "Portuguese": "pt", "Russian": "ru",
              "Slovak": "sk", "Slovenian": "sl", "Serbian": "sr", "Swedish": "sv", "Tetum": "tet",
              "Turkish": "tr", "Ukrainian": "uk", "Igpay Atinlay": "x-pig-latin", "simplified Chinese": "zh",
              "traditional Chinese": "zh-tw"}

    _UNITS = ["auto", "ca", "uk2", "ui", "si"]

    _EXCLUDES = ["currently", "minutely", "hourly", "daily", "alerts", "flags"]

    def __init__(self, api_key=None):
        self._api_key = None
        self._latitude = None
        self._longitude = None
        self._response = None
        self._weather = None
        self._lang = self._LANGS["auto"]
        self._units = "auto"
        self._extend = False
        self._exclude = []

        self.api_key = api_key

    @property
    def api_key(self):
        # type:() -> str
        return self._api_key

    @property
    def latitude(self):
        # type:() -> float
        return self._latitude

    @property
    def longitude(self):
        # type:() -> float
        return self._longitude

    '''
    Raises AssertionError
    '''

    @property
    def url(self):
        # type:() -> str
        assert type(self.latitude) is float, "latitude must be <class 'float'>, is type {}".format(
            type(self.latitude))
        assert type(self.longitude) is float, "longitude must be <class 'float'>, is type {}".format(
            type(self.longitude))

        url = "https://api.darksky.net/forecast/{}/{},{}?units={}".format(self.api_key, self.latitude,
                                                                                  self.longitude, self._units)
        if self.lang != "auto":
            url += "&lang={}".format(self.lang)

        if len(self._exclude) > 0:
            url += "&exclude="
            for e in self._exclude:
                url += "{},".format(e)
            url = url.strip(",")

        if self._extend:
            url += "&extend=hourly"

        return url

    @property
    def extend(self):
        # type:() -> bool
        return self._extend

    @property
    def exclude(self):
        # type:() -> list
        return self._exclude

    @property
    def EXCLUDES(self):
        # type:() -> list
        return self._EXCLUDES

    @property
    def api_call_count(self):
        # type:() -> str
        return self._response.headers["x-forecast-api-calls"]

    @property
    def response_time(self):
        # type:() -> str
        return self._response.headers["x-response-time"]

    @property
    def response_date(self):
        # type:() -> str
        return self._response.headers["date"]

    @property
    def response_status_code(self):
        # type:() -> int
        return self._response.status_code

    @property
    def LANG(self):
        # type:() -> dict_keys
        return self._LANGS.keys()

    @property
    def lang(self):
        # type:() -> str
        return self._lang

    @property
    def UNITS(self):
        # type:() -> list
        return _UNITS

    @property
    def units(self):
        # type:() -> str
        return self._units

    '''
    Raises ValueError 
    '''

    @api_key.setter
    def api_key(self, api_key):
        # type:(str) -> None
        api_key = str(api_key)

        if len(api_key) != 32:
            log.debug("api_key():api_key must be 32 characters long.")
            raise ValueError("api_key must be 32 characters long.")

        self._api_key = api_key

    '''
    Raises TypeError
    '''

    @latitude.setter
    def latitude(self, latitude):
        # type:(float) -> None
        self._latitude = float(latitude)

    '''
    Raises TypeError
    '''

    @longitude.setter
    def longitude(self, longitude):
        # type:(float) -> None
        self._longitude = float(longitude)

    '''
    Raises TypeError
    '''

    @extend.setter
    def extend(self, extend):
        # type:(str) -> None
        self._extend = bool(extend)

    '''
    Raises TypeError
    Raises ValueError
    '''

    @exclude.setter
    def exclude(self, excludes):
        # type:(list) -> None
        if type(excludes) is str:
            if excludes in self._EXCLUDES:
                self._exclude = [excludes]
        elif type(excludes) is list:
            _e = []
            for exclude in excludes:
                if exclude in self._EXCLUDES:
                    _e.append(exclude)
                else:
                    log.debug("exclude():'{}' is not a valid exclude value".format(exclude))
                    raise ValueError("'{}' is not a valid exclude value".format(exclude))
            self._exclude = _e
        else:
            log.debug("exclude():excludes must be type '<class 'str'>' was type '{}'".format(type(excludes)))
            raise TypeError("excludes must be type '<class 'str'>' was type '{}'".format(type(excludes)))

    '''
    Raises KeyError
    '''

    @lang.setter
    def lang(self, language):
        # type:(str) -> None
        self._lang = self._LANGS[language]

    '''
    Raises ValueError
    '''

    @units.setter
    def units(self, unit):
        # type:(str) -> None
        if unit not in self._UNITS:
            raise ValueError("{} is not a valid unit type".format(unit))
        self._units = unit

    def weather(self, latitude=None, longitude=None):
        # type:(float, float) -> Weather
        if latitude is not None:
            self.latitude = latitude
        if longitude is not None:
            self.longitude = longitude

        self._response = requests.get(self.url, headers={"Accept-Encoding": "gzip"})
        self._response.raise_for_status()

        self._weather = Weather(self._response.text)
        return self._weather
