import unittest

from main.LC0076_Minimum_Window_Substring import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
  def test_climbStairs(self):
    self.assertEqual(test.minWindow("ADOBECODEBANC", "ABC"), "BANC")
    self.assertEqual(test.minWindow("a", "a"), "a")
    self.assertEqual(test.minWindow("a", "aa"), "")
