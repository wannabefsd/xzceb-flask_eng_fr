"""method-docstring"""
import unittest
from translator import english_to_french

class test_english_to_french(unittest.TestCase):
    """class docsting"""
    def test1(self):
        self.assertEqual(english_to_french(0), 0)
        self.assertEqual(english_to_french(Hello), Bonjour)

from translator import french_to_english

class test_french_to_english(unittest.TestCase):
    """class docstring"""
    def test1(self):
        self.assertEqual(french_to_english(0), 0)
        self.assertEqual(french_to_english(Bonjour), Hello)

unittest.main()
