import unittest

from main.LC1140_Stone_Game_II import Solution

class SolutionTest(unittest.TestCase):

  def test_numRollsToTarget(self):
    test = Solution()
    self.assertEqual(test.stoneGameII([2, 7, 9, 4, 4]), 10)
    self.assertEqual(test.stoneGameII([1, 2, 3, 4, 5, 100]), 104)
