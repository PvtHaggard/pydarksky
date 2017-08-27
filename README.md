Pydarksky!
==========
[![Build Status](https://travis-ci.org/PvtHaggard/pydarksky.svg?branch=master)](https://travis-ci.org/PvtHaggard/pydarksky) [![License](https://img.shields.io/badge/License-GNU%20v3.0-blue.svg)](https://github.com/PvtHaggard/pydarksky/blob/master/LICENSE) ![Python](https://img.shields.io/badge/Python-2.7%2C%203.3%2C%203.4%2C%203.5%2C%203.6-blue.svg) ![Status](https://img.shields.io/badge/Status-Development-orange.svg)



Pydarksky is a work in progress wrapper for the [Dark Sky](https://www.darksky.net) API.

-----

This is the first python library I have written so any advice and help will be greatly appreciated.

## TODO:
* Documentation
    * Docstrings
    * Readme
* Unittests
    * Find weather data with alerts/minutely data for testing
* Example uses


----
## Install
Python versions 2.7, 3.3+
```
pip install pydarksky
```

## Basic usage
Example uses [pendulum](https://github.com/sdispater/pendulum) for timestamp conversion.
```python
import pendulum
import pydarksky

pendulum.set_formatter("alternative")

darksky = pydarksky.DarkSky(api_key=API_KEY)
darksky.latitude = -34.9285
darksky.longitude = 138.6005
weather = darksky.weather()

# Current weather
date = pendulum.from_timestamp(weather.currently.time, tz=weather.timezone)
print("Time: {}, Temp: {}\n".format(date.format("DD-MM-YY hh:mm"), weather.currently.temperature))

# Iterating over forecast
for day in weather.daily:
    temp = day.temperature_max
    date = pendulum.from_timestamp(day.time, tz=weather.timezone)
    print("Date: {}, Max: {}".format(date.format("DD-MM-YY"), temp))
```

<a href="https://darksky.net/poweredby/"> <img src="https://darksky.net/dev/img/attribution/poweredby-oneline.png" alt="Dark Sky" width="500px"/></a>
