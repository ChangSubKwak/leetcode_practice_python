import unittest

from main.LC1590_Make_Sum_Divisible_by_P import Solution

test = Solution()


class LC1582_Special_Positions_in_a_Binary_Matrix_test(unittest.TestCase):
    def test1(self):
        self.assertEqual(test.minSubarray([3, 1, 4, 2], 6), 1)
        self.assertEqual(test.minSubarray([6, 3, 5, 2], 9), 2)
        self.assertEqual(test.minSubarray([1, 2, 3], 3), 3)
