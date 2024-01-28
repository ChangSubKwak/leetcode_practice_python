import unittest

from main.LC1074_Number_of_Submatrices_That_Sum_to_Target import Solution

test = Solution()


class TestClass(unittest.TestCase):
    def test_numSubmatrixSumTarget(self):
        self.assertEqual(test.numSubmatrixSumTarget([[0, 1, 0], [1, 1, 1], [0, 1, 0]], 0), 4)
        self.assertEqual(test.numSubmatrixSumTarget([[1, -1], [-1, 1]], 0), 5)
        self.assertEqual(test.numSubmatrixSumTarget([[904]], 0), 0)
