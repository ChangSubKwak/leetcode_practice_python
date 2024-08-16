import unittest
from main.LC0624_Maximum_Distance_in_Arrays import Solution

test = Solution

class SolutionTest(unittest.TestCase):
    def test_maxDistance(self):
        self.assertEqual(Solution.maxDistance([[1, 2, 3], [4, 5], [1, 2, 3]]), 4)
        self.assertEqual(Solution.maxDistance([[1], [1]]), 0)
