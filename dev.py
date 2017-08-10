import logging
import sys
import os

from darkskypy import DarkSkyPy
from darkskypy import Weather

logging.basicConfig(level=logging.DEBUG)
logging.getLogger("urllib3").setLevel(level=logging.CRITICAL)
logging.getLogger("chardet").setLevel(level=logging.CRITICAL)
logging.getLogger("darkskypy").setLevel(level=logging.DEBUG)

log = logging.getLogger(__name__)

tmp_path = os.path.join(sys.path[0], 'tests')
tmp_path = os.path.join(tmp_path, "testdata.json")
assert os.path.isfile(tmp_path)
with open(tmp_path) as f:
    test_json = f.read()


def main():
    darksky = DarkSkyPy(sys.argv[1])
    weather = Weather(test_json)
    pass


if __name__ == "__main__":
    main()
