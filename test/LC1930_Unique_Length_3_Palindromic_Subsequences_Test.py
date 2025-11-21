import unittest

from main.LC1930_Unique_Length_3_Palindromic_Subsequences import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_numberOfMatches(self):
        self.assertEqual(test.countPalindromicSubsequence("aabca"), 3)
        self.assertEqual(test.countPalindromicSubsequence("adc"), 0)
        self.assertEqual(test.countPalindromicSubsequence("bbcbaba"), 4)
