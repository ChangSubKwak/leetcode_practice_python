import unittest
from main.LC2370_Longest_Ideal_Subsequence import Solution

test = Solution()


class SolutionTest(unittest.case):
    def test_longestIdealString(self):
        self.assertEqual(test.longestIdealString("acfgbd", 2), 4)
        self.assertEqual(test.longestIdealString("abcd", 3), 4)
