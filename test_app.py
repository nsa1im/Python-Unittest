import unittest

from app import changeFromRoman

class TestChangeFromRoman(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(changeFromRoman("V"), 5)
        self.assertEqual(changeFromRoman("VIII"), 8) 
        self.assertEqual(changeFromRoman("IX"), 9)
        self.assertEqual(changeFromRoman("III"), 3)
        self.assertEqual(changeFromRoman("C"), 100)
        self.assertEqual(changeFromRoman("Z"), "invalid")
        # self.assertEqual(changeFromRoman("CIZ"), "invalid")
        # self.assertEqual(changeFromRoman("VV"), "invalid")
        self.assertEqual(changeFromRoman(None), "invalid")
        
unittest.main()