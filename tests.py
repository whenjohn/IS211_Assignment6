#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Unit test for conversions.py"""
import conversions
import unittest

class testKnownValues(unittest.TestCase):
    cel_to_kev_known_values = { 500.00:773.15,
                                250.00:523.15,
                                0.00:273.15,
                                -250.00:23.15,
                                -273.15:0.00,
    }
    cel_to_far_known_values = { 500.00:932.00,
                                250.00:482.00,
                                0.00:32.00,
                                -250.00:-418.00,
                                -273.15:-459.67,
    }
    def test_convertCelsiusToKelvin(self):
        """convertCelsiusToKelvin() should give known result with known input"""
        for cel in self.cel_to_kev_known_values:
            result = conversions.convertCelsiusToKelvin(cel)
            self.assertEqual(self.cel_to_kev_known_values[cel], result)
    def test_convertCelsiusToFahrenheit(self):
        """convertCelsiusToFahrenheit() should give known result with known input"""
        for cel in self.cel_to_far_known_values:
            result = conversions.convertCelsiusToFahrenheit(cel)
            self.assertEqual(self.cel_to_far_known_values[cel], result)


class TestBadInputsConvertCelsiusToKelvin(unittest.TestCase):
    #def testNotInt(self):
        #"""convertCelsiusToKelvin should fail with int"""
        #self.assertRaises(conversions.NotFoatError, conversions.convertCelsiusToKelvin, 5)
    def testNotBool(self):
        """convertCelsiusToKelvin should fail with Bool"""
        self.assertRaises(conversions.NotFoatError, conversions.convertCelsiusToKelvin, True)
    def testNotString(self):
        """convertCelsiusToKelvin should fail with letters"""
        self.assertRaises(conversions.NotFoatError, conversions.convertCelsiusToKelvin, 'A')
    def testNotSymbol(self):
        """convertCelsiusToKelvin should fail with symbols"""
        self.assertRaises(conversions.NotFoatError, conversions.convertCelsiusToKelvin, '$')

class TestBadInputsConvertCelsiusToFahrenheit(unittest.TestCase):
    #def testNotInt(self):
        #"""convertCelsiusToFahrenheit should fail with int"""
        #self.assertRaises(conversions.NotFoatError, conversions.convertCelsiusToFahrenheit, 5)
    def testNotBool(self):
        """convertCelsiusToFahrenheit should fail with Bool"""
        self.assertRaises(conversions.NotFoatError, conversions.convertCelsiusToFahrenheit, True)
    def testNotString(self):
        """convertCelsiusToFahrenheit should fail with letters"""
        self.assertRaises(conversions.NotFoatError, conversions.convertCelsiusToFahrenheit, 'A')
    def testNotSymbol(self):
        """convertCelsiusToFahrenheit should fail with symbols"""
        self.assertRaises(conversions.NotFoatError, conversions.convertCelsiusToFahrenheit, '$')


if __name__ == '__main__':
    unittest.main()
