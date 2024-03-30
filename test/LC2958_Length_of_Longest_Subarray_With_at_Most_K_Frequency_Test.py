import unittest

from main.LC2958_Length_of_Longest_Subarray_With_at_Most_K_Frequency import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_maxSubarrayLength(self):
        self.assertEqual(test.maxSubarrayLength([1, 2, 3, 1, 2, 3, 1, 2], 2), 6)
        self.assertEqual(test.maxSubarrayLength([1, 2, 1, 2, 1, 2, 1, 2], 1), 2)
        self.assertEqual(test.maxSubarrayLength([5, 5, 5, 5, 5, 5, 5], 4), 4)
