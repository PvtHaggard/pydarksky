import unittest
import logging
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from darkskypy import DarkSkyPy
from darkskypy import Weather

logging.basicConfig(level=logging.INFO)
logging.getLogger("darkskypy")

# assert os.path.isfile("testdata.json"), "JSON file missing can not run tests"
logging.info(os.listdir(os.curdir))
with open("testdata.json") as f:
    test_json = f.read()


class TestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
