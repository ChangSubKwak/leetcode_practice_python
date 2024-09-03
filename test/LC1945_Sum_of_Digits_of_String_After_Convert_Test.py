import unittest
from main.LC1945_Sum_of_Digits_of_String_After_Convert import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_getLucky(self):
        self.assertEqual(test.getLucky("iiii", 1), 36)
        self.assertEqual(test.getLucky("leetcode", 2), 6)
        self.assertEqual(test.getLucky("zbax", 2), 8)