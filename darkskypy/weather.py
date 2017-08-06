import logging
import json
import sys
import os

from .currently import Currently

__author__ = "PvtHaggard"

__license__ = "GPLv3"
__version__ = "N/A"
__maintainer__ = "PvtHaggard"
__email__ = "pvtgaggard@gmail.com"
__status__ = "Development Pre-alpha"

log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())


class Weather:
    def __init__(self, json_raw: str):
        self.json = json.loads(json_raw)
        self.latitude = self.json["latitude"]
        self.longitude = self.json["longitude"]
        self.timezone = self.json["timezone"]
        self.offset = self.json["offset"]  # deprecated

        if "currently" in self.json:
            self.currently = Currently(self.json["currently"])
        else:
            self.currently = None



tmp_path = "testdata.json"
assert os.path.isfile(tmp_path), "JSON file missing can not run tests"
with open(tmp_path) as f:
    test_json = f.read()
Weather(test_json)