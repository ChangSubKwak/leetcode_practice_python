import unittest

from main.LC0070_Climbing_Stairs import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
  def test_climbStairs(self):
    self.assertEqual(test.climbStairs(2), 2)
    self.assertEqual(test.climbStairs(3), 3)
