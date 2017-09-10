# -*- coding: utf-8 -*-
import unittest
import logging
import sys
import os

sys.path.insert(0, os.path.abspath("."))

from pydarksky import DarkSky, Weather, NoDataError

logging.basicConfig(level=logging.DEBUG)
logging.getLogger("darkskypy")

# For local testing
if sys.path[0].endswith("tests"):
    with open(os.path.join(sys.path[0], "test_data_basic.json")) as f:
        json_basic = f.read()

    with open(os.path.join(sys.path[0], "test_data_minutely.json")) as f:
        json_minutely = f.read()

    with open(os.path.join(sys.path[0], "test_data_alerts.json")) as f:
        json_alerts = f.read()

# For Travis-ci testing
else:
    with open(os.path.join(sys.path[0], "tests/test_data_basic.json")) as f:
        json_basic = f.read()

    with open(os.path.join(sys.path[0], "tests/test_data_minutely.json")) as f:
        json_minutely = f.read()

    with open(os.path.join(sys.path[0], "tests/test_data_alerts.json")) as f:
        json_alerts = f.read()


class TestBasic(unittest.TestCase):
    def test_weather_init(self):
        Weather(json_basic)

    def test_get_attribute_data(self):
        weather = Weather(json_basic)
        var = weather.currently.temperature

    def test_get_attribute_no_data(self):
        weather = Weather(json_basic)
        with self.assertRaises(NoDataError):
            var = weather.currently.nearestStormDistance

    def test_get_attribute_no_attribute(self):
        weather = Weather(json_basic)
        with self.assertRaises(AttributeError):
            var = weather.currently.fail


class TestMinutely(unittest.TestCase):
    def test_weather_init(self):
        Weather(json_minutely)


class TestAlerts(unittest.TestCase):
    def test_weather_init(self):
        Weather(json_alerts)


if __name__ == '__main__':
    unittest.main()
