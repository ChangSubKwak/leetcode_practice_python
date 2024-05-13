import unittest
from main.LC3005_Count_Elements_With_Maximum_Frequency import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_minOperations(self):
        self.assertEqual(test.maxFrequencyElements([1, 2, 2, 3, 1, 4]), 4)
        self.assertEqual(test.maxFrequencyElements([1, 2, 3, 4, 5]), 5)
