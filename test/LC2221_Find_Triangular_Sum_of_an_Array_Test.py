import unittest

from main.LC2221_Find_Triangular_Sum_of_an_Array import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_triangularSum(self):
        self.assertEqual(test.triangularSum([1, 2, 3, 4, 5]), 8)
        self.assertEqual(test.triangularSum([5]), 5)

