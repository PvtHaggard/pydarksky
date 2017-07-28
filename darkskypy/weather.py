import logging

__author__ = "PvtHaggard"

__license__ = "GPLv3"
__version__ = "N/A"
__maintainer__ = "PvtHaggard"
__email__ = "pvtgaggard@gmail.com"
__status__ = "Development Pre-alpha"

log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())


class Weather:
    def __init__(self, json):
        self.json = json
