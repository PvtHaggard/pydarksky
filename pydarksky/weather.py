import logging
import json
import sys
import os

__author__ = "PvtHaggard"

__license__ = "GPLv3"
__version__ = "N/A"
__maintainer__ = "PvtHaggard"
__email__ = "pvtgaggard@gmail.com"
__status__ = "Development Pre-alpha"

log = logging.getLogger("pydarksky")


class Weather:
    """
    Do not assume the existence of any property unless stated otherwise.

    :param str json_raw:

    :var dict json: [Required] JSON data returned by the Dark Sky API
    :var float latitude: [Required] The requested latitude. Maybe different from the value passed to DarkSky class.
    :var float longitude: [Required] The requested longitude. Maybe different from the value passed to DarkSky class.
    :var str timezone: [Required] The IANA timezone name for the requested location. This is used for text summaries and for determining when hourly and daily data block objects begin.
    :var float offset: [Deprecated] The current timezone offset in hours. (Use of this property will almost certainly result in Daylight Saving Time bugs. Please use timezone, instead.)

    :var Currently currently: A class containing the current weather conditions at the requested location.

    :var list[Daily] daily: A class containing the current weather conditions at the requested location.
    :var str daily_summary: A human-readable summary of the daily data block.
    :var str daily_icon: A machine-readable text summary of the daily data block.

    :var list[Hourly] hourly: A class containing the current weather conditions day-by-day for the next week.
    :var str hourly_summary: A human-readable summary of the hourly data block.
    :var str hourly_icon: A machine-readable text summary of the daily data block.

    :var list[Minutely] minutely: A class containing the current weather conditions minute-by-minute for the next hour.
    :var str minutely_summary: A human-readable summary of the minutely data block.
    :var str minutely_icon: A machine-readable text summary of the daily data block.

    :var Alert alerts: An alerts array, which, if present, contains any severe weather alerts pertinent to the requested location.
    """

    def __init__(self, json_raw):
        # type:(str) -> None
        self.json = json.loads(json_raw)
        self.latitude = self.json["latitude"]
        self.longitude = self.json["longitude"]
        self.timezone = self.json["timezone"]
        self.offset = self.json["offset"]

        if "currently" in self.json:
            self.currently = Currently(self.json["currently"], self)

        if "daily" in self.json:
            self.daily = []
            if self.json["daily"].get("summary") is not None:
                self.daily_summary = self.json["daily"].get("summary")
            if self.json["daily"].get("icon") is not None:
                self.daily_icon = self.json["daily"].get("icon")
            for data in self.json["daily"]["data"]:
                self.daily.append(Daily(data, self))

        if "hourly" in self.json:
            self.hourly = []
            if self.json["hourly"].get("summary") is not None:
                self.hourly_summary = self.json["hourly"].get("summary")
            if self.json["hourly"].get("icon") is not None:
                self.hourly_icon = self.json["hourly"].get("icon")
            for data in self.json["hourly"]["data"]:
                self.hourly.append(Hourly(data, self))

        if "minutely" in self.json:
            self.minutely = []
            if self.json["minutely"].get("summary") is not None:
                self.minutely_summary = self.json["minutely"].get("summary")
            if self.json["minutely"].get("icon") is not None:
                self.minutely_icon = self.json["minutely"].get("icon")
            for data in self.json["minutely"]["data"]:
                self.minutely.append(Minutely(data, self))

        if "alerts" in self.json:
            self.alerts = Alerts(self.json["alerts"], self)


class WeatherData:
    def __init__(self, data, parent=None):
        # type:(dict, Weather) -> None
        self.parent = parent
        for field, value in data.items():
            setattr(self, field, value)


class Currently(WeatherData):
    def __init__(self, data, parent=None):
        # type:(dict, Weather) -> None
        WeatherData.__init__(self, data, parent)


class Daily(WeatherData):
    def __init__(self, data, parent=None):
        # type:(dict, Weather) -> None
        WeatherData.__init__(self, data, parent)


class Hourly(WeatherData):
    def __init__(self, data, parent=None):
        # type:(dict, Weather) -> None
        WeatherData.__init__(self, data, parent)


class Minutely(WeatherData):
    def __init__(self, data, parent=None):
        # type:(dict, Weather) -> None
        WeatherData.__init__(self, data, parent)


class Alerts:
    """
    :var str description: A detailed description of the alert.
    :var int expires: The UNIX time at which the alert will expire.
    :var str regions: An array of strings representing the names of the regions covered by this weather alert.
    :var str severity: The severity of the weather alert, will be one of the following values:


        * **advisory** (an individual should be aware of potentially severe weather)
        * **watch** (an individual should prepare for potentially severe weather)
        * **warning** (an individual should take immediate action to protect themselves and others from potentially severe weather).

    :var int time: The UNIX time at which the alert was issued.
    :var str title: A brief description of the alert.
    :var str uri: An HTTP(S) URI that one may refer to for detailed information about the alert.
    """
    def __init__(self, data, parent=None):
        # type:(dict, Weather) -> None
        self.weather = parent
        self.description = data["description"]
        self.expires = data["expires"]
        self.regions = data["regions"]
        self.severity = data["severity"]
        self.time = data["time"]
        self.title = data["title"]
        self.uri = data["uri"]
