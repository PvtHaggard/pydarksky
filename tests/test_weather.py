import unittest
import logging
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from darkskypy import DarkSkyPy
from darkskypy import Weather

logging.basicConfig(level=logging.INFO)
logging.getLogger("darkskypy")

tmp_path = os.path.join(sys.path[0], 'tests')
tmp_path = os.path.join(tmp_path, "testdata.json")
assert os.path.isfile(tmp_path), "JSON file missing can not run tests"
with open(tmp_path) as f:
    test_json = f.read()


class TestCase(unittest.TestCase):
    def test_weather_init(self):
        Weather(test_json)


if __name__ == '__main__':
    unittest.main()
