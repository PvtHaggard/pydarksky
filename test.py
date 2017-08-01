import unittest

from darkskypy import DarkSkyPy


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
        url = "https://api.darksky.net/forecast/00000000000000000000000000000000/-1.2,1.2?units=si&lang=en"
        darksky = DarkSkyPy("0" * 32)
        darksky.longitude = 1.2
        darksky.latitude = -1.2
        self.assertEqual(darksky.url, url)

    def test_lang_set_pass(self):
        darksky = DarkSkyPy("0" * 32)
        darksky.response_lang = "Arabic"
        self.assertEqual(darksky.response_lang, "ar")

    def test_lang_set_fail(self):
        darksky = DarkSkyPy("0" * 32)
        with self.assertRaises(KeyError):
            darksky.response_lang = "bad key"

    def test_units_set_pass(self):
        darksky = DarkSkyPy("0" * 32)
        darksky.response_units = "ui"
        self.assertEqual(darksky.response_units, "ui")

    def test_units_set_fail(self):
        darksky = DarkSkyPy("0" * 32)
        with self.assertRaises(AssertionError):
            darksky.response_units = "bad units"


if __name__ == '__main__':
    unittest.main()
