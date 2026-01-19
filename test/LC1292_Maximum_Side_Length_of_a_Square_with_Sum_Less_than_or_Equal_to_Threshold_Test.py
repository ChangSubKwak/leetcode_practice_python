import unittest

from main.LC1292_Maximum_Side_Length_of_a_Square_with_Sum_Less_than_or_Equal_to_Threshold import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.maxSideLength([
            [1, 1, 3, 2, 4, 3, 2],
            [1, 1, 3, 2, 4, 3, 2],
            [1, 1, 3, 2, 4, 3, 2]
        ], 4), 2)

        self.assertEqual(test.maxSideLength([
            [2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2]
        ], 1), 0)
