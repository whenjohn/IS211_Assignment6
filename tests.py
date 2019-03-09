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
    far_to_cel_known_values = { 932.00:500.00,
                                482.00:250.00,
                                32.00:0.00,
                                -238.00:-150.00,
                                -459.67:-273.15,
    }
    far_to_kev_known_values = { 932.00:773.15,
                                500.00:533.15,
                                158.00:343.15,
                                -256.00:113.15,
                                -459.67:0.00,
    }
    kev_to_cel_known_values = { 773.15:500.00,
                                523.15:250.00,
                                273.15:0.00,
                                23.15:-250.00,
                                0.00:-273.15,
    }
    kev_to_far_known_values = { 773.15:932.00,
                                533.15:500.00,
                                343.15:158.00,
                                113.15:-256.00,
                                0.00:-459.67,
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
    def test_convertFahrenheitToCelsius(self):
        """convertFahrenheitToCelsius() should give known result with known input"""
        for cel in self.far_to_cel_known_values:
            result = conversions.convertFahrenheitToCelsius(cel)
            self.assertEqual(self.far_to_cel_known_values[cel], result)
    def test_convertFahrenheitToKelvin(self):
        """convertFahrenheitToKelvin() should give known result with known input"""
        for cel in self.far_to_kev_known_values:
            result = conversions.convertFahrenheitToKelvin(cel)
            self.assertEqual(self.far_to_kev_known_values[cel], result)
    def test_convertKelvinToCelsius(self):
        """convertKelvinToCelsius() should give known result with known input"""
        for cel in self.kev_to_cel_known_values:
            result = conversions.convertKelvinToCelsius(cel)
            self.assertEqual(self.kev_to_cel_known_values[cel], result)
    def test_convertKelvinToFahrenheit(self):
        """convertKelvinToFahrenheit() should give known result with known input"""
        for cel in self.kev_to_far_known_values:
            result = conversions.convertKelvinToFahrenheit(cel)
            self.assertEqual(self.kev_to_far_known_values[cel], result)



class TestBadInputs(unittest.TestCase):
    def testNotBoolC2K(self):
        """convertCelsiusToKelvin should fail with Bool"""
        self.assertRaises(conversions.NotNumError, conversions.convertCelsiusToKelvin, True)
    def testNotStringC2K(self):
        """convertCelsiusToKelvin should fail with letters"""
        self.assertRaises(conversions.NotNumError, conversions.convertCelsiusToKelvin, 'A')
    def testNotSymbolC2K(self):
        """convertCelsiusToKelvin should fail with symbols"""
        self.assertRaises(conversions.NotNumError, conversions.convertCelsiusToKelvin, '$')

    def testNotBoolC2F(self):
        """convertCelsiusToFahrenheit should fail with Bool"""
        self.assertRaises(conversions.NotNumError, conversions.convertCelsiusToFahrenheit, True)
    def testNotStringC2F(self):
        """convertCelsiusToFahrenheit should fail with letters"""
        self.assertRaises(conversions.NotNumError, conversions.convertCelsiusToFahrenheit, 'A')
    def testNotSymbolC2F(self):
        """convertCelsiusToFahrenheit should fail with symbols"""
        self.assertRaises(conversions.NotNumError, conversions.convertCelsiusToFahrenheit, '$')

    def testNotBoolF2C(self):
        """convertFahrenheitToCelsius should fail with Bool"""
        self.assertRaises(conversions.NotNumError, conversions.convertFahrenheitToCelsius, True)
    def testNotStringF2C(self):
        """convertFahrenheitToCelsius should fail with letters"""
        self.assertRaises(conversions.NotNumError, conversions.convertFahrenheitToCelsius, 'A')
    def testNotSymbolF2C(self):
        """convertFahrenheitToCelsius should fail with symbols"""
        self.assertRaises(conversions.NotNumError, conversions.convertFahrenheitToCelsius, '$')

    def testNotBoolF2K(self):
        """convertFahrenheitToKelvin should fail with Bool"""
        self.assertRaises(conversions.NotNumError, conversions.convertFahrenheitToKelvin, True)
    def testNotStringF2K(self):
        """convertFahrenheitToKelvin should fail with letters"""
        self.assertRaises(conversions.NotNumError, conversions.convertFahrenheitToKelvin, 'A')
    def testNotSymbolF2K(self):
        """convertFahrenheitToKelvin should fail with symbols"""
        self.assertRaises(conversions.NotNumError, conversions.convertFahrenheitToKelvin, '$')

    def testNotBoolK2C(self):
        """convertKelvinToCelsius should fail with Bool"""
        self.assertRaises(conversions.NotNumError, conversions.convertKelvinToCelsius, True)
    def testNotStringK2C(self):
        """convertKelvinToCelsius should fail with letters"""
        self.assertRaises(conversions.NotNumError, conversions.convertKelvinToCelsius, 'A')
    def testNotSymbolK2C(self):
        """convertKelvinToCelsius should fail with symbols"""
        self.assertRaises(conversions.NotNumError, conversions.convertKelvinToCelsius, '$')

    def testNotBoolF2K(self):
        """convertKelvinToFahrenheit should fail with Bool"""
        self.assertRaises(conversions.NotNumError, conversions.convertKelvinToFahrenheit, True)
    def testNotStringF2K(self):
        """convertKelvinToFahrenheit should fail with letters"""
        self.assertRaises(conversions.NotNumError, conversions.convertKelvinToFahrenheit, 'A')
    def testNotSymbolF2K(self):
        """convertKelvinToFahrenheit should fail with symbols"""
        self.assertRaises(conversions.NotNumError, conversions.convertKelvinToFahrenheit, '$')


class SanityCheck(unittest.TestCase):
    def testSanityC2K(self):
        """convertCelsiusToKelvin(convertKelvinToCelsius(n))==n for all n"""
        for temp in range(-100, 100):
            compare1 = conversions.convertCelsiusToKelvin(temp)
            compare2 = conversions.convertKelvinToCelsius(compare1)
            self.assertEqual(temp, compare2)

    def testSanityC2F(self):
        for temp in range(-100, 100):
            """convertCelsiusToFahrenheit(convertFahrenheitToCelsius(n))==n for all n"""
            compare1 = conversions.convertCelsiusToFahrenheit(temp)
            compare2 = conversions.convertFahrenheitToCelsius(compare1)
            self.assertEqual(temp, compare2)

    def testSanityF2K(self):
        for temp in range(-100, 100):
            """convertFahrenheitToKelvin(convertKelvinToFahrenheit(n))==n for all n"""
            compare1 = conversions.convertFahrenheitToKelvin(temp)
            compare2 = conversions.convertKelvinToFahrenheit(compare1)
            self.assertEqual(temp, round(compare2))


if __name__ == '__main__':
    unittest.main()
