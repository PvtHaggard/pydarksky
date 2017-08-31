# -*- coding: utf-8 -*-
from datetime import datetime
import unittest
import logging
import sys
import os

sys.path.insert(0, os.path.abspath("."))

from pydarksky import DarkSky

logging.basicConfig(level=logging.INFO)
logging.getLogger("pydarksky").disabled = True

_adelaide_lat = -34.9285
_adelaide_long = 138.6005


class TestCase(unittest.TestCase):
    def test_api_key_fail(self):
        with self.assertRaises(ValueError):
            DarkSky("123")

    def test_api_key_pass(self):
        darksky = DarkSky("0" * 32)
        self.assertEqual("0" * 32, darksky.api_key)

    def test_longitude_fail(self):
        darksky = DarkSky("0" * 32)
        with self.assertRaises(ValueError):
            darksky.longitude = "fail"

    def test_longitude_pass(self):
        darksky = DarkSky("0" * 32)
        darksky.longitude = "1.0"
        self.assertEqual(darksky.longitude, 1.0)

    def test_url_fail(self):
        darksky = DarkSky("0" * 32)
        with self.assertRaises(AssertionError):
            darksky.weather()

    def test_url_basic_pass(self):
        url = "https://api.darksky.net/forecast/00000000000000000000000000000000/-34.9285,138.6005?units=auto"
        darksky = DarkSky("0" * 32)
        darksky.longitude = _adelaide_long
        darksky.latitude = _adelaide_lat
        self.assertEqual(darksky.url, url)

    def test_lang_pass(self):
        darksky = DarkSky("0" * 32)
        darksky.lang = "Arabic"
        self.assertEqual(darksky.lang, "ar")

    def test_lang_fail(self):
        darksky = DarkSky("0" * 32)
        with self.assertRaises(KeyError):
            darksky.lang = "bad key"

    def test_url_lang_pass(self):
        url = "https://api.darksky.net/forecast/00000000000000000000000000000000/-34.9285," \
              "138.6005?units=auto&lang=en"
        darksky = DarkSky("0" * 32)
        darksky.longitude = _adelaide_long
        darksky.latitude = _adelaide_lat
        darksky.lang = "English"
        self.assertEqual(darksky.url, url)

    def test_units_pass(self):
        darksky = DarkSky("0" * 32)
        darksky.units = "ui"
        self.assertEqual(darksky.units, "ui")

    def test_units_fail(self):
        darksky = DarkSky("0" * 32)
        with self.assertRaises(ValueError):
            darksky.units = "bad units"

    def test_const_units_pass(self):
        darksky = DarkSky("0" * 32)
        self.assertEqual(darksky.UNITS, ["auto", "ca", "uk2", "ui", "si"])

    def test_const_langs_pass(self):
        darksky = DarkSky("0" * 32)
        self.assertEqual(darksky.LANGS,
                         ['Arabic', 'Azerbaijani', 'Belarusian', 'Bosnian', 'Bulgarian', 'Catalan',
                          'Cornish', 'Croatian', 'Czech', 'Dutch', 'English', 'Estonian', 'French',
                          'Georgian', 'German', 'Greek', 'Hungarian', 'Icelandic', 'Igpay Atinlay',
                          'Indonesian', 'Italian', 'Norwegian Bokmål', 'Polish', 'Portuguese', 'Russian',
                          'Serbian', 'Slovak', 'Slovenian', 'Spanish', 'Swedish', 'Tetum', 'Turkish',
                          'Ukrainian', 'auto', 'simplified Chinese', 'traditional Chinese']
                         )

    def test_exclude_list_pass(self):
        darksky = DarkSky("0" * 32)
        excludes = darksky.EXCLUDES
        darksky.exclude = [excludes[0], excludes[1]]

    def test_exclude_str_pass(self):
        darksky = DarkSky("0" * 32)
        darksky.exclude = "currently"
        self.assertEqual(darksky.exclude, ["currently"])

    def test_exclude_set_fail(self):
        darksky = DarkSky("0" * 32)
        excludes = darksky.EXCLUDES
        with self.assertRaises(ValueError):
            darksky.exclude = [excludes[0], "bad val"]

    def test_exclude_set_int_fail(self):
        darksky = DarkSky("0" * 32)
        with self.assertRaises(TypeError):
            darksky.exclude = 1234

    def test_url_exclude_pass(self):
        url = "https://api.darksky.net/forecast/00000000000000000000000000000000/-34.9285," \
              "138.6005?units=auto&exclude=minutely,hourly,daily,alerts,flags"
        darksky = DarkSky("0" * 32)
        darksky.exclude = ["minutely", "hourly", "daily", "alerts", "flags"]
        darksky.longitude = _adelaide_long
        darksky.latitude = _adelaide_lat
        self.assertEqual(darksky.url, url)

    def test_extend_pass(self):
        darksky = DarkSky("0" * 32)
        darksky.extend = True
        self.assertEqual(darksky.extend, True)
        darksky.extend = False
        self.assertEqual(darksky.extend, False)

    def test_url_extend_pass(self):
        url = "https://api.darksky.net/forecast/00000000000000000000000000000000/-34.9285," \
              "138.6005?units=auto&extend=hourly"
        darksky = DarkSky("0" * 32)
        darksky.longitude = _adelaide_long
        darksky.latitude = _adelaide_lat
        darksky.extend = True
        self.assertEqual(darksky.url, url)


if __name__ == '__main__':
    unittest.main()
