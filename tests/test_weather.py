# -*- coding: utf-8 -*-
import unittest
import logging
import sys
import os

sys.path.insert(0, os.path.abspath("."))

from pydarksky import DarkSky
from pydarksky import Weather

logging.basicConfig(level=logging.INFO)
logging.getLogger("darkskypy")


with open(os.path.join(sys.path[0], "tests/test_data_basic.json")) as f:
    json_basic = f.read()

# with open(os.path.join(sys.path[0], "tests/test_data_minutely.json")) as f:
#     json_minutely = f.read()
#
# with open(os.path.join(sys.path[0], "tests/test_data_alerts.json")) as f:
#     json_alerts = f.read()


class TestCase(unittest.TestCase):
    def test_weather_init(self):
        Weather(json_basic)


if __name__ == '__main__':
    unittest.main()
