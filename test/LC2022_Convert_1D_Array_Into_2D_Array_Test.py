import unittest
from main.LC2022_Convert_1D_Array_Into_2D_Array import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_timeRequiredToBuy(self):
        self.assertEqual(test.construct2DArray([1, 2, 3, 4], 2, 2), [[1, 2], [3, 4]])
        self.assertEqual(test.construct2DArray([1, 2, 3], 1, 3), [[1, 2, 3]])
        self.assertEqual(test.construct2DArray([1, 2], 1, 1), [])
