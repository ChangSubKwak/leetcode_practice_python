import unittest
from main.LC3074_Apple_Redistribution_into_Boxes import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_minOperations(self):
        self.assertEqual(test.minimumBoxes([1, 3, 2], [4, 3, 1, 5, 2]), 2)
        self.assertEqual(test.minimumBoxes([5, 5, 5], [2, 4, 2, 7]), 4)
