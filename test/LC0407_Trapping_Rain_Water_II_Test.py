import unittest

from main.LC0407_Trapping_Rain_Water import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_sumOfLeftLeaves(self):
        self.assertEqual(test.trapRainWater([[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]), 4)
        self.assertEqual(test.trapRainWater([[3, 3, 3, 3, 3], [3, 2, 2, 2, 3], [3, 2, 1, 2, 3], [3, 2, 2, 2, 3], [3, 3, 3, 3, 3]]), 4)
