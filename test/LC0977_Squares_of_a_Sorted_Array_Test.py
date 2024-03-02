import unittest

from main.LC0977_Squares_of_a_Sorted_Array import Solution

test = Solution()


class TestClass(unittest.TestCase):
    def test_minFallingPathSum(self):
        self.assertEqual(test.sortedSquares([-4, -1, 0, 3, 10]), [0, 1, 9, 16, 100])
        self.assertEqual(test.sortedSquares([-7, -3, 2, 3, 11]), [4, 9, 9, 49, 121])
