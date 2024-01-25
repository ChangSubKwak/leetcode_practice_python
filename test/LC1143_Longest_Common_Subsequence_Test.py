import unittest

from main.LC1143_Longest_Common_Subsequence import Solution

class SolutionTest(unittest.TestCase):

  def test_numRollsToTarget(self):
    test = Solution()
    self.assertEqual(test.longestCommonSubsequence("abcde", "ace"), 3)
    self.assertEqual(test.longestCommonSubsequence("abc", "abc"), 3)
    self.assertEqual(test.longestCommonSubsequence("abc", "def"), 0)
