#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Temperature unit conversions"""

import numbers

#Define exceptions
class NotFoatError(Exception): pass


def convertCelsiusToKelvin(celsius):
    """convert Celsius to Kelvin"""
    if not isinstance(celsius, numbers.Number) or isinstance(celsius, bool):
        raise NotFoatError, "non−float entered"
    return round((celsius + 273.15), 2)


def convertCelsiusToFahrenheit(celsius):
    """convert Celsius to Fahrenheit"""
    if not isinstance(celsius, numbers.Number) or isinstance(celsius, bool):
        raise NotFoatError, "non−float entered"
    return round((celsius * 1.8 + 32), 2)
