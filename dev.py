import logging
from darkskypy.DarkSkyPy import DarkSkyPy

logging.basicConfig(level=logging.WARNING)
logging.getLogger("requests").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)
# logging.getLogger("darkskypy.DarkSkyPy").setlevel(logging.WARNING)

log = logging.getLogger(__name__)
log.setLevel(level=logging.INFO)

def main():
    log.debug("debug")
    log.info("info")
    log.critical("critical")
    log.warning("warning")
    log.error("error")

    darksky = DarkSkyPy("677540efddd5db9d74337dc6a2da26e6")
    darksky.weather()


if __name__ == "__main__":
    main()
