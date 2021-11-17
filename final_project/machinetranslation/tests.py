"""method-docstring"""
import unittest
from translator import englishToFrench

class test_englishToFrench(unittest.TestCase):
    """class docsting"""
    def test1(self):
        self.assertEqual(englishToFrench(0), 0)
        self.assertEqual(englishToFrench(Hello), Bonjour)

from translator import frenchToEnglish

class test_frenchToEnglish(unittest.TestCase):
    """class docstring"""
    def test1(self):
        self.assertEqual(frenchToEnglish(0), 0)
        self.assertEqual(frenchToEnglish(Bonjour), Hello)

unittest.main()
