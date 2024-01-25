import unittest

from main.LC1143_Longest_Common_Subsequence import Solution

class SolutionTest(unittest.TestCase):

  def test_numRollsToTarget(self):
    test = Solution()
    self.assertEqual(test.longestCommonsubsequence("abcde", "ace"), 3)
    self.assertEqual(test.longestCommonsubsequence("abc", "abc"), 3)
    self.assertEqual(test.longestCommonsubsequence("abc", "def"), 0)
