import unittest

from main.LC3010_Divide_an_Array_Into_Subarrays_With_Minimum_Cost_I import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_minOperations(self):
        self.assertEqual(test.minimumCost([1, 2, 3, 12]), 6)
        self.assertEqual(test.minimumCost([5, 4, 3]), 12)
        self.assertEqual(test.minimumCost([10, 3, 1, 1]), 12)
