import logging
import json

__author__ = "PvtHaggard"

__license__ = "GPLv3"
__version__ = "N/A"
__maintainer__ = "PvtHaggard"
__email__ = "pvtgaggard@gmail.com"
__status__ = "Development Pre-alpha"

log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())


class Weather:
    def __init__(self, data: dict):
        self.time = data.get("time", None)
        self.summary = data.get("summary", None)
        self.icon = data.get("icon", None)
        self.precip_intensity = data.get("precipIntensity", None)
        self.precip_probability = data.get("precipProbability", None)
        self.temperature = data.get("temperature", None)
        self.apparent_temperature = data.get("apparentTemperature", None)
        self.dew_point = data.get("dewPoint", None)
        self.humidity = data.get("humidity", None)
        self.wind_speed = data.get("windSpeed", None)
        self.wind_gust = data.get("windGust", None)
        self.wind_bearing = data.get("windBearing", None)
        self.cloud_cover = data.get("cloudCover", None)
        self.pressure = data.get("pressure", None)
        self.ozone = data.get("ozone", None)
        self.uv_index = data.get("uvIndex", None)
