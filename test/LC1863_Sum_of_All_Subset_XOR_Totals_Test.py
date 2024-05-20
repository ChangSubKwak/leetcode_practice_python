import unittest
from main.LC1863_Sum_of_All_Subset_XOR_Totals import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_makeEqual(self):
        self.assertEqual(test.subsetXORSum([1, 3]), 6)
        self.assertEqual(test.subsetXORSum([5, 1, 6]), 28)
        self.assertEqual(test.subsetXORSum([3, 4, 5, 6, 7, 8]), 480)
