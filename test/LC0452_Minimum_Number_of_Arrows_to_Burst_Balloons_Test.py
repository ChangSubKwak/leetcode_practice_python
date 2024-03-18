import unittest
from main.LC0452_Minimum_Number_of_Arrows_to_Burst_Balloons import Solution

test = Solution()

class SolutionTest(unittest.TestCase):
    def test_frequencySort(self):
        self.assertEqual(test.findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]), 2)
        self.assertEqual(test.findMinArrowShots([[1, 2], [3, 4], [5, 6], [7, 8]]), 4)
        self.assertEqual(test.findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]]), 2)
