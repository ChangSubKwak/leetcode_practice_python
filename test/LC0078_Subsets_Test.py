import unittest
from main.LC0078_Subsets import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_climbStairs(self):
        self.assertEqual(test.subsets([1, 2, 3]), [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]])
        self.assertEqual(test.subsets([0]), [[], [0]])
