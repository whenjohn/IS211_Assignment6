#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Temperature unit conversions"""

import numbers

#Define exceptions
class NotNumError(Exception): pass


def convertCelsiusToKelvin(temperature):
    """convert Celsius to Kelvin"""
    if not isinstance(temperature, numbers.Number) or isinstance(temperature, bool):
        raise NotNumError, "non−float entered"
    return round((temperature + 273.15), 2)


def convertCelsiusToFahrenheit(temperature):
    """convert Celsius to Fahrenheit"""
    if not isinstance(temperature, numbers.Number) or isinstance(temperature, bool):
        raise NotNumError, "non−float entered"
    return round((temperature * 1.8 + 32), 2)


def convertFahrenheitToCelsius(temperature):
    """convert Fahrenheit to Celsius"""
    if not isinstance(temperature, numbers.Number) or isinstance(temperature, bool):
        raise NotNumError, "non−float entered"
    return round(((temperature - 32) * 0.555555555555556), 2)


def convertFahrenheitToKelvin(temperature):
    """convert Fahrenheit to Kelvin"""
    if not isinstance(temperature, numbers.Number) or isinstance(temperature, bool):
        raise NotNumError, "non−float entered"
    return round(((temperature + 459.67) * 0.555555555555556), 2)


def convertKelvinToCelsius(temperature):
    """convert Kelvin to Celsius"""
    if not isinstance(temperature, numbers.Number) or isinstance(temperature, bool):
        raise NotNumError, "non−float entered"
    return round((temperature - 273.15), 2)


def convertKelvinToFahrenheit(temperature):
        """convert Kelvin to Fahrenheit"""
        if not isinstance(temperature, numbers.Number) or isinstance(temperature, bool):
            raise NotNumError, "non−float entered"
        return round((temperature * 1.8 - 459.67), 2)
