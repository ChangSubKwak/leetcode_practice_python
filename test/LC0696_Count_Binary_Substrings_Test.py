import unittest
from main.LC0696_Count_Binary_Substrings import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.countBinarySubstrings("00110011"), 6)
        self.assertEqual(test.countBinarySubstrings("10101"), 4)
