import unittest
from main.LC3190_Find_Minimum_Operations_to_Make_All_Elements_Divisible_by_Three import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.minimumOperations([1, 2, 3, 4]), 3)
        self.assertEqual(test.minimumOperations([3, 6, 9]), 0)
