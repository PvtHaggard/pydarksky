import unittest
import logging
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from darkskypy import DarkSkyPy
from darkskypy import Weather

logging.basicConfig(level=logging.INFO)
logging.getLogger("darkskypy")


class TestCase(unittest.TestCase):
    def test_weather_init(self):
        pass


if __name__ == '__main__':
    unittest.main()
