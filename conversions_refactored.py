#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""unit conversions"""

import numbers

#Define exceptions
class ConversionNotPossible(Exception): pass


def convert(fromUnit,toUnit,value):
    if not isinstance(value, numbers.Number) or isinstance(value, bool):
        raise ConversionNotPossible, "non number entered"

    if (fromUnit == toUnit):
        raise ConversionNotPossible, "No conversions"

    if ((fromUnit == 'celsius' or fromUnit == 'kelvin' or fromUnit == 'fahrenheit') and (toUnit == 'meter' or toUnit == 'yard' or toUnit == 'mile')):
        raise ConversionNotPossible, "Mismatch units"

    if ((fromUnit == 'meter' or fromUnit == 'yard' or fromUnit == 'mile') and (toUnit == 'celsius' or toUnit == 'kelvin' or toUnit == 'fahrenheit')):
        raise ConversionNotPossible, "Mismatch units"


    if (fromUnit == 'celsius'):
        if (toUnit == 'kelvin'):
            return value + 273.15
        elif (toUnit == 'fahrenheit'):
            return value * 1.8 + 32
    elif (fromUnit == 'kelvin'):
        if (toUnit == 'celsius'):
            return value - 273.15
        elif (toUnit == 'fahrenheit'):
            return value * 1.8 - 459.67
    elif (fromUnit == 'fahrenheit'):
        if (toUnit == 'celsius'):
            return (value - 32) * 0.555555555555556
        elif (toUnit == 'kelvin'):
            return (value + 459.67) * 0.555555555555556

    elif (fromUnit == 'meter'):
        if (toUnit == 'yard'):
            return value * 1.093613
        elif (toUnit == 'mile'):
            return value / 1609.344
    elif (fromUnit == 'yard'):
        if (toUnit == 'meter'):
            return value / 1.0936
        elif (toUnit == 'mile'):
            return value * 0.00056818
    elif (fromUnit == 'mile'):
        if (toUnit == 'yard'):
            return value * 1760.0
        elif (toUnit == 'meter'):
            return value * 1609.344
