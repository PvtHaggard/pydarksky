Pydarksky!
==========
[![Build Status](https://travis-ci.org/PvtHaggard/pydarksky.svg?branch=master)](https://travis-ci.org/PvtHaggard/pydarksky)



Pydarksky is a work in progress wrapper for the [Dark Sky](https://www.darksky.net) API.

-----

This is the first python library I have written so any advice and help will be greatly appreciated.

----

# Basic usage
Example uses [Arrow](https://github.com/crsmithdev/arrow) for timestamp conversion.
```python
darksky = DarkSky(api_key)
darksky.latitude = -34.9285
darksky.longitude = 138.6005
weather = darksky.weather()

# Current weather
date = arrow.get(weather.currently.time).to(weather.timezone)
print("Time: {}, Temp: {}\n".format(date.format("DD-MM-YY hh:mm"), weather.currently.temperature))

# Iterating over forecast
for day in weather.daily:
    temp = day.temperature_max
    date = arrow.get(day.time).to(weather.timezone)
    print("Date: {}, Max: {}".format(date.format("DD-MM-YY"), temp))
```

<img src="https://darksky.net/dev/img/attribution/poweredby-oneline.png" alt="Dark Sky" width="500px"/>