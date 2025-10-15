import unittest
from main.LC3350_Adjacent_Increasing_Subarrays_Detection_II import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.maxIncreasingSubarrays([2, 5, 7, 8, 9, 2, 3, 4, 3, 1]), 3)
        self.assertEqual(test.maxIncreasingSubarrays([1, 2, 3, 4, 4, 4, 4, 5, 6, 7]), 2)
