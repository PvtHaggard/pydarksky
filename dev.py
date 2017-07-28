import logging
from darkskypy import DarkSkyPy

logging.basicConfig(level=logging.DEBUG)
logging.getLogger("urllib3").setLevel(level=logging.CRITICAL)
logging.getLogger("chardet").setLevel(level=logging.CRITICAL)
logging.getLogger("darkskypy").setLevel(level=logging.DEBUG)

log = logging.getLogger(__name__)


def main():
    darksky = DarkSkyPy("677540efddd5db9d74337dc6a2da26e6")
    weather = darksky.weather(-34.9286, 138.5999)
    pass


if __name__ == "__main__":
    main()
