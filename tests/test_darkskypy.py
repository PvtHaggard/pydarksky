import unittest
import logging
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from darkskypy import DarkSkyPy

logging.basicConfig(level=logging.INFO)
logging.getLogger("darkskypy")

_adelaide_lat = -34.9285
_adelaide_long = 138.6005


class TestCase(unittest.TestCase):
    def test_api_key_fail(self):
        with self.assertRaises(ValueError):
            DarkSkyPy("123")

    def test_api_key_pass(self):
        darksky = DarkSkyPy("0" * 32)
        self.assertEqual("0" * 32, darksky.api_key)

    def test_longitude_fail(self):
        darksky = DarkSkyPy("0" * 32)
        with self.assertRaises(ValueError):
            darksky.longitude = "fail"

    def test_longitude_pass(self):
        darksky = DarkSkyPy("0" * 32)
        darksky.longitude = "1.0"
        self.assertEqual(darksky.longitude, 1.0)

    def test_url_basic_fail(self):
        darksky = DarkSkyPy("0" * 32)
        with self.assertRaises(AssertionError):
            darksky.weather()

    def test_url_basic_pass(self):
        url = "https://api.darksky.net/forecast/00000000000000000000000000000000/-34.9285,138.6005?units=si&lang=en"
        darksky = DarkSkyPy("0" * 32)
        darksky.longitude = _adelaide_long
        darksky.latitude = _adelaide_lat
        self.assertEqual(darksky.url, url)

    def test_lang_set_pass(self):
        darksky = DarkSkyPy("0" * 32)
        darksky.lang = "Arabic"
        self.assertEqual(darksky.lang, "ar")

    def test_lang_set_fail(self):
        darksky = DarkSkyPy("0" * 32)
        with self.assertRaises(KeyError):
            darksky.lang = "bad key"

    def test_units_set_pass(self):
        darksky = DarkSkyPy("0" * 32)
        darksky.units = "ui"
        self.assertEqual(darksky.units, "ui")

    def test_units_set_fail(self):
        darksky = DarkSkyPy("0" * 32)
        with self.assertRaises(ValueError):
            darksky.units = "bad units"

    def test_exclude_set_list_pass(self):
        darksky = DarkSkyPy("0" * 32)
        excludes = darksky.EXCLUDES
        darksky.exclude = [excludes[0], excludes[1]]

    def test_exclude_set_str_pass(self):
        darksky = DarkSkyPy("0" * 32)
        darksky.exclude = "currently"

    def test_exclude_set_fail(self):
        darksky = DarkSkyPy("0" * 32)
        excludes = darksky.EXCLUDES
        with self.assertRaises(ValueError):
            darksky.exclude = [excludes[0], "bad val"]

    def test_exclude_set_int_fail(self):
        darksky = DarkSkyPy("0" * 32)
        with self.assertRaises(TypeError):
            darksky.exclude = 1234

    def test_url_exclude_pass(self):
        darksky = DarkSkyPy("0" * 32)
        darksky.exclude = ["minutely", "hourly", "daily", "alerts", "flags"]
        darksky.longitude = _adelaide_long
        darksky.latitude = _adelaide_lat
        self.assertEqual(darksky.url, "https://api.darksky.net/forecast/00000000000000000000000000000000/-34.9285,138.6005?units=si&lang=en&exclude=minutely,hourly,daily,alerts,flags")

if __name__ == '__main__':
    unittest.main()
