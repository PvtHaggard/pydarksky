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

log = logging.getLogger("darkskypy")


class Weather:
    def __init__(self, json_raw):
        # type:(str) -> None
        self.json = json.loads(json_raw)

    @property
    def latitude(self):
        return self.json.get("latitude")

    @property
    def longitude(self):
        return self.json.get("longitude")

    @property
    def timezone(self):
        return self.json.get("timezone")

    @property
    def offset(self):
        return self.json.get("offset")

    @property
    def currently(self):
        if "currently" in self.json:
            return Currently(self.json["currently"], self)

    @property
    def daily(self):
        if "daily" in self.json:
            daily = []
            for data in self.json["daily"]["data"]:
                daily.append(Daily(data, self))
            return daily

    @property
    def daily_summary(self):
        if "daily" in self.json:
            return self.json["daily"].get("summary")

    @property
    def daily_icon(self):
        if "daily" in self.json:
            return self.json["daily"].get("icon")

    @property
    def hourly(self):
        if "hourly" in self.json:
            hourly = []
            for data in self.json["hourly"]["data"]:
                hourly.append(Hourly(data, self))
            return hourly

    @property
    def hourly_summary(self):
        if "hourly" in self.json:
            return self.json["hourly"].get("summary")

    @property
    def hourly_icon(self):
        if "hourly" in self.json:
            return self.json["hourly"].get("icon")

    # TODO: Find a weather report with minutely data for testing
    @property
    def minutely(self):
        if "minutely" in self.json:
            minutely = []
            for data in self.json["minutely"]["data"]:
                minutely.append(Minutely(data, self))
            return minutely

    @property
    def minutely_summary(self):
        if "minutely" in self.json:
            return self.json["minutely"].get("summary")

    @property
    def minutely_icon(self):
        if "minutely" in self.json:
            return self.json["minutely"].get("icon")

    # TODO: Find a weather report with an alert for testing
    @property
    def alerts(self):
        if "alerts" in self.json:
            return Alerts(self.json["alerts"], self)


class WeatherData:
    def __init__(self, data, parent=None):
        # type:(dict, Weather) -> None
        self.cloud_cover = data.get("cloudCover", None)
        self.dew_point = data.get("dewPoint", None)
        self.humidity = data.get("humidity", None)
        self.icon = data.get("icon", None)
        self.ozone = data.get("ozone", None)
        self.pressure = data.get("pressure", None)
        self.summary = data.get("summary", None)
        self.time = data.get("time", None)
        self.uv_index = data.get("uvIndex", None)
        self.visibility = data.get("visibility", None)
        self.weather = parent
        self.wind_bearing = data.get("windBearing", None)
        self.wind_gust = data.get("windGust", None)
        self.wind_speed = data.get("windSpeed", None)


class Currently(WeatherData):
    def __init__(self, data, parent=None):
        # type:(dict, Weather) -> None
        super().__init__(data, parent)
        self.apparent_temperature = data.get("apparentTemperature", None)
        self.precipitation_intensity = data.get("precipIntensity", None)
        self.precipitation_probability = data.get("precipProbability", None)
        self.precipitation_Type = data.get("precipType", None)
        self.storm_bearing = data.get("nearestStormBearing")
        self.storm_distance = data.get("nearestStormDistance")
        self.temperature = data.get("temperature", None)


class Daily(WeatherData):
    def __init__(self, data, parent=None):
        # type:(dict, Weather) -> None
        super().__init__(data, parent)
        self.apparent_temperature_max = data.get("apparentTemperatureMax", None)
        self.apparent_temperature_max_time = data.get("apparentTemperatureMaxTime", None)
        self.apparent_temperature_min = data.get("apparentTemperatureMin", None)
        self.apparent_temperature_min_time = data.get("apparentTemperatureMinTime", None)
        self.moon_phase = data.get("moonPhase", None)
        self.precipitation_accumulation = data.get("precipAccumulation", None)
        self.precipitation_intensity = data.get("precipIntensity", None)
        self.precipitation_intensity_max = data.get("precipIntensityMax", None)
        self.precipitation_intensity_max_time = data.get("precipIntensityMaxTime", None)
        self.precipitation_probability = data.get("precipProbability", None)
        self.precipitation_type = data.get("precipType", None)
        self.sunrise_time = data.get("sunriseTime", None)
        self.sunset_time = data.get("sunsetTime", None)
        self.temperature = data.get("temperature", None)
        self.temperature_max = data.get("temperatureMax", None)
        self.temperature_max_time = data.get("temperatureMaxTime", None)
        self.temperature_min = data.get("temperatureMin", None)
        self.temperature_min_time = data.get("temperatureMinTime", None)
        self.uv_index_time = data.get("uvIndexTime", None)
        self.wind_gust_time = data.get("windGustTime", None)


class Hourly(WeatherData):
    def __init__(self, data, parent=None):
        # type:(dict, Weather) -> None
        super().__init__(data, parent)
        self.apparent_temperature = data.get("apparentTemperature", None)
        self.precipitation_accumulation = data.get("precipAccumulation", None)
        self.precipitation_intensity = data.get("precipIntensity", None)
        self.precipitation_probability = data.get("precipProbability", None)
        self.precipitation_Type = data.get("precipType", None)
        self.storm_bearing = data.get("nearestStormBearing")
        self.storm_distance = data.get("nearestStormDistance")
        self.temperature = data.get("temperature", None)


class Minutely(WeatherData):
    def __init__(self, data, parent=None):
        # type:(dict, Weather) -> None
        super().__init__(data, parent)
        self.apparent_temperature = data.get("apparentTemperature", None)
        self.precipitation_accumulation = data.get("precipAccumulation", None)
        self.precipitation_intensity = data.get("precipIntensity", None)
        self.precipitation_probability = data.get("precipProbability", None)
        self.precipitation_Type = data.get("precipType", None)
        self.storm_bearing = data.get("nearestStormBearing")
        self.storm_distance = data.get("nearestStormDistance")


class Alerts:
    def __init__(self, data, parent=None):
        # type:(dict, Weather) -> None
        self.weather = parent
        self.description = data.get("description", None)
        self.expires = data.get("expires", None)
        self.regions = data.get("regions", None)
        self.severity = data.get("severity", None)
        self.time = data.get("time", None)
        self.title = data.get("title", None)
        self.uri = data.get("uri", None)
