import unittest
from main.LC1513_Number_of_Substrings_With_Only_1s import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.numSub("0110111"), 9)
        self.assertEqual(test.numSub("101"), 2)
        self.assertEqual(test.numSub("111111"), 21)
