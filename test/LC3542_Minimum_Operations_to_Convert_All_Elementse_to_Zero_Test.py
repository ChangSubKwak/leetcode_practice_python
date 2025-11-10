import unittest
from main.LC3542_Minimum_Operations_to_Convert_All_Elementse_to_Zero import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.minOperations([0, 2]), 1)
        self.assertEqual(test.minOperations([3, 1, 2, 1]), 3)
        self.assertEqual(test.minOperations([1, 2, 1, 2, 1, 2]), 4)
