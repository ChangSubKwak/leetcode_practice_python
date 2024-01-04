import unittest

from main.LC1624_Largest_Substring_Between_Two_Equal_Characters import LC1624_Largest_Substring_Between_Two_Equal_Characters

test = LC1624_Largest_Substring_Between_Two_Equal_Characters()


class LC1624_Largest_Substring_Between_Two_Equal_Characters_Test(unittest.TestCase):
    def test(self):
        self.assertEqual(test.maxLengthBetweenEqualCharacters("aa"), 0)
        self.assertEqual(test.maxLengthBetweenEqualCharacters("abca"), 2)
        self.assertEqual(test.maxLengthBetweenEqualCharacters("cbzxy"), -1)
