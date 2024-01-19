import unittest

from main.LC0931_Minimum_Falling_Path_Sum import Solution

test = Solution()


class TestClass(unittest.TestCase):
    def test_minFallingPathSum(self):
        self.assertEqual(test.minFallingPathSum([[2, 1, 3], [6, 5, 4], [7, 8, 9]]), 13)
        self.assertEqual(test.minFallingPathSum([[-19, 57], [-40, -5]]), -59)
