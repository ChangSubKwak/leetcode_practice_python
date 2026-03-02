import unittest

from main.LC1536_Minimum_Swaps_to_Arrange_a_Binary_Grid import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_getLengthOfOptimalCompression(self):
        self.assertEqual(test.minSwaps([
            [0, 0, 1],
            [1, 1, 0],
            [1, 0, 0]
        ]), 3)

        self.assertEqual(test.minSwaps([
            [0, 1, 1, 0],
            [0, 1, 1, 0],
            [0, 1, 1, 0],
            [0, 1, 1, 0]
        ]), -1)

        self.assertEqual(test.minSwaps([
            [1, 0, 0],
            [1, 1, 0],
            [1, 1, 1]
        ]), 0)