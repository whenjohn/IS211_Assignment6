#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Unit test for conversions.py"""
import conversions_refactored
import unittest

known_values = {
      "celsius-kelvin":{
          250.00:523.15,
          0.00:273.15,
          -250.00:23.15,
      },
      "celsius-fahrenheit":{
          250.00:482.00,
          0.00:32.00,
          -250.00:-418.00,
      },
      "fahrenheit-celsius":{
          482.00:250.00,
          32.00:0.00,
          -238.00:-150.00,
      },
      "fahrenheit-kelvin":{
          500.00:533.15,
          158.00:343.15,
          -256.00:113.15,
      },
      "kelvin-celsius":{
          273.15:0.00,
          23.15:-250.00,
          0.00:-273.15,
      },
      "kelvin-fahrenheit":{
          343.15:158.00,
          113.15:-256.00,
          0.00:-459.67,
      },
    "mile-yard":{
          1:1760,
          3:5280,
          10:17600,
      },
      "mile-meter":{
          1:1609.34,
          50:80467.20,
          100:160934.40,
      },
      "yard-mile":{
          9:0.01,
          27:0.02,
          45:0.03,
      },
      "yard-meter":{
          1:0.91,
          50:45.72,
          100:91.44,
      },
      "meter-mile":{
          10:0.01,
          25:0.02,
          57:0.04,

      },
      "meter-yard":{
          1:1.09,
          25:27.34,
          50:54.68,
      }
}

class testKnownValues(unittest.TestCase):
    def test_convert(self):
        """convert should give known result with known input"""
        for from_to in known_values:
            #print from_to
            (a,b) = from_to.split('-')
            for value in known_values[from_to]:
                #print "value:",value
                result = conversions_refactored.convert(a,b,value)
                #print self.known_values[from_to][value]," = ",result
                self.assertEqual(known_values[from_to][value], round(result, 2))


class TestBadInput(unittest.TestCase):
    def test_bad_inputs(self):
        """convert should fail with bad inputs"""
        for a, b, c in (('meter','yard',True), ('meter','yard','A'), ('meter','yard','$')):
            with self.assertRaises(conversions_refactored.ConversionNotPossible):
                conversions_refactored.convert(a,b,c)
    def test_wrong_inputs(self):
        """convert should fail with wrong inputs"""
        inputs = (  ('meter','meter',1),
                    ('yard','yard',1),
                    ('mile','mile',1),
                    ('celsius','celsius',1),
                    ('kelvin','kelvin',1),
                    ('fahrenheit','fahrenheit',1),

                    ('meter','celsius',1),
                    ('meter','kelvin',1),
                    ('meter','fahrenheit',1),
                    ('yard','celsius',1),
                    ('yard','kelvin',1),
                    ('yard','fahrenheit',1),
                    ('mile','celsius',1),
                    ('mile','kelvin',1),
                    ('mile','fahrenheit',1),

                    ('celsius','meter',1),
                    ('celsius','yard',1),
                    ('celsius','mile',1),
                    ('kelvin','meter',1),
                    ('kelvin','yard',1),
                    ('kelvin','mile',1),
                    ('fahrenheit','meter',1),
                    ('fahrenheit','yard',1),
                    ('fahrenheit','mile',1),
        )
        for a, b, c in inputs:
            #print inputs
            with self.assertRaises(conversions_refactored.ConversionNotPossible):
                conversions_refactored.convert(a,b,c)


class SanityCheck(unittest.TestCase):
    def testSanity(self):
        """converting from one unit to itself"""
        for from_to in known_values:
            #print from_to
            (a,b) = from_to.split('-')
            for value in range (int(min(known_values[from_to])), int(max(known_values[from_to]))):
                #print "testing value:",value
                compare1 = conversions_refactored.convert(a,b,value)
                compare2 = conversions_refactored.convert(b,a,compare1)
                self.assertEqual(value, round(compare2))


if __name__ == '__main__':
    unittest.main()

#suite = unittest.TestLoader().loadTestsFromTestCase(SanityCheck)
#unittest.TextTestRunner(verbosity=3).run(suite)
