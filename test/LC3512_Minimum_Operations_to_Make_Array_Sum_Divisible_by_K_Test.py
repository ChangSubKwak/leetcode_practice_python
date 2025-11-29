import unittest
from main.LC3512_Minimum_Operations_to_Make_Array_Sum_Divisible_by_K import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.minOperations([3, 9, 7], 5), 4)
        self.assertEqual(test.minOperations([4, 1, 3], 4), 0)
        self.assertEqual(test.minOperations([3, 2], 6), 5)
