import unittest

from main.LC0629_K_Inverse_Pairs_Array import Solution

class SolutionTest(unittest.TestCase):

  def test_numRollsToTarget(self):
    test = Solution()
    self.assertEqual(test.kInversePairs(3, 0), 1)
    self.assertEqual(test.kInversePairs(3, 1), 2)
