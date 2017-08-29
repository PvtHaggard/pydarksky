# -*- coding: utf-8 -*-
import requests
import logging
from datetime import datetime

from .weather import Weather

__author__ = "PvtHaggard"

__license__ = "GPLv3"
__version__ = "N/A"
__maintainer__ = "PvtHaggard"
__email__ = "pvtgaggard@gmail.com"
__status__ = "Development Pre-alpha"

log = logging.getLogger("pydarksky")


class DarkSky(object):
    # TODO: Add weather property to get last weather
    # TODO: lang() should also accept any _LANGS values
    """
    :param str api_key: Darksky.net API key

    :var list[str] _EXCLUDES: Valid Dark Sky API data excludes

    :var str api_key: Darksky.net API key
    :var float latitude: latitude
    :var float longitude: Darksky.net API key

    """
    _LANGS = {"auto": "auto", "Arabic": "ar", "Azerbaijani": "az", "Belarusian": "be", "Bulgarian": "bg",
              "Bosnian": "bs", "Catalan": "ca", "Czech": "cs", "German": "de", "Greek": "el", "English": "en",
              "Spanish": "es", "Estonian": "et", "French": "fr", "Croatian": "hr", "Hungarian": "hu",
              "Indonesian": "id", "Italian": "it", "Icelandic": "is", "Georgian": "ka", "Cornish": "kw",
              "Norwegian Bokmål": "nb", "Dutch": "nl", "Polish": "pl", "Portuguese": "pt", "Russian": "ru",
              "Slovak": "sk", "Slovenian": "sl", "Serbian": "sr", "Swedish": "sv", "Tetum": "tet",
              "Turkish": "tr", "Ukrainian": "uk", "Igpay Atinlay": "x-pig-latin", "simplified Chinese": "zh",
              "traditional Chinese": "zh-tw"}

    def __init__(self, api_key=None):
        log.debug("Caution: Logging at debug level may expose API key")

        self._api_key = None
        self._date_time = None
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

    @property
    def url(self):
        # type:() -> str
        assert type(self.latitude) is float, "latitude must be <class 'float'>, is type {}".format(
            type(self.latitude))
        assert type(self.longitude) is float, "longitude must be <class 'float'>, is type {}".format(
            type(self.longitude))

        url = "https://api.darksky.net/forecast/{}/{},{}".format(self.api_key, self.latitude, self.longitude)

        if type(self._date_time) is datetime:
            url += ",{:%Y-%m-%dT%H:%M:%S}".format(self._date_time)

        url += "?units={}".format(self.units)

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
        return ["currently", "minutely", "hourly", "daily", "alerts", "flags"]

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
    def LANGS(self):
        # type:() -> list
        keys = list(self._LANGS.keys())
        keys.sort()
        return keys

    @property
    def lang(self):
        # type:() -> str
        return self._lang

    @property
    def UNITS(self):
        # type:() -> list
        return ["auto", "ca", "uk2", "ui", "si"]

    @property
    def units(self):
        # type:() -> str
        """
        Units to be returned by the Dark Sky API.
        Valid values can be found in UNITS.

        :return: Dark Sky unit type.
        :rtype: str
        """
        return self._units

    @property
    def date_time(self):
        # type:() -> datetime
        return self._date_time

    @api_key.setter
    def api_key(self, api_key):
        # type:(str) -> None
        api_key = str(api_key)

        if len(api_key) != 32:
            log.debug("api_key must be 32 characters long.")
            raise ValueError("api_key must be 32 characters long.")

        self._api_key = api_key

    @latitude.setter
    def latitude(self, latitude):
        # type:(float) -> None
        self._latitude = float(latitude)

    @longitude.setter
    def longitude(self, longitude):
        # type:(float) -> None
        self._longitude = float(longitude)

    @extend.setter
    def extend(self, extend):
        # type:(str) -> None
        self._extend = bool(extend)

    @exclude.setter
    def exclude(self, excludes):
        # type:(list) -> None
        if type(excludes) is str:
            if excludes in self.EXCLUDES:
                self._exclude = [excludes]
        elif type(excludes) is list:
            _e = []
            for exclude in excludes:
                if exclude in self.EXCLUDES:
                    _e.append(exclude)
                else:
                    log.debug("'{}' is not a valid exclude value".format(exclude))
                    raise ValueError("'{}' is not a valid exclude value".format(exclude))
            self._exclude = _e
        else:
            log.debug("excludes must be type '<class 'str'>' is type '{}'".format(type(excludes)))
            raise TypeError("excludes must be type '<class 'str'>' is type '{}'".format(type(excludes)))

    @lang.setter
    def lang(self, language):
        # type:(str) -> None
        self._lang = self._LANGS[language]

    @units.setter
    def units(self, unit):
        # type:(str) -> None
        if unit not in self._UNITS:
            raise ValueError("{} is not a valid unit type".format(unit))
        self._units = unit

    @date_time.setter
    def date_time(self, date_time):
        # type:(datetime) -> None
        if type(date_time) is not datetime:
            log.debug("datetime must be type '<class 'datetime'>' is type '{}'".format(type(date_time)))
            raise TypeError("excludes must be type '<class 'datetime'>' is type '{}'".format(type(date_time)))
        self._date_time = date_time

    def weather(self, latitude=None, longitude=None, date_time=None):
        # type:(float, float, datetime) -> Weather
        """

        :param float or None latitude: Locations latitude
        :param float or None longitude: Locations longitude
        :param datetime date_time: Date/time for historical weather data

        :var str url: Dark Sky API URL.

        :return: Weather data from the last successful weather() call.
        :rtype: Weather

        This may need reworking at some point. As it stands date_time must be set to None manually,
        otherwise it will always receive historical data. I may not be thinking about this right.. It is 3am.
        """

        if latitude is not None:
            self.latitude = latitude
        if longitude is not None:
            self.longitude = longitude
        if date_time is not None:
            self.date_time = date_time

        url = self.url

        log.debug(url)

        self._response = requests.get(url, headers={"Accept-Encoding": "gzip"})
        self._response.raise_for_status()

        self._weather = Weather(self._response.text)
        return self._weather

    def weather_last(self):
        # type:() -> Weather
        """
        :return: Weather data from the last successful weather() call.
        :rtype: Weather or None
        """
        return self._weather

    def exclude_invert(self):
        # type:() -> None
        tmp = self.exclude
        self._exclude = []
        for i in self.EXCLUDES:
            if i not in tmp:
                self._exclude.append(i)
