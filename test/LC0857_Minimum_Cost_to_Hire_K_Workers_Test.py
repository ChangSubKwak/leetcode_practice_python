import unittest

from main.LC0857_Minimum_Cost_to_Hire_K_Workers import Solution
test = Solution()


class SolutionTest(unittest.TestCase):
    def test_sumOfDistancesInTree(self):
        self.assertEqual(test.mincostToHireWorkers([10, 20, 5], [70, 50, 30], 2), 105.00000)
        self.assertEqual(test.mincostToHireWorkers([10, 20, 5], [70, 50, 30], 2), 30.66667)
