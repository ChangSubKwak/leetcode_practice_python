import unittest

from main.LC1636_Sort_Array_by_Increasing_Frequency import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_maxWidthOfVerticalArea(self):
        self.assertEqual(test.frequencySort([1, 1, 2, 2, 2, 3]), [3, 1, 1, 2, 2, 2])
        self.assertEqual(test.frequencySort([2, 3, 1, 3, 2]), [1, 3, 3, 2, 2])
        self.assertEqual(test.frequencySort([-1, 1, -6, 4, 5, -6, 1, 4, 1]), [5, -1, 4, 4, -6, -6, 1, 1, 1])
