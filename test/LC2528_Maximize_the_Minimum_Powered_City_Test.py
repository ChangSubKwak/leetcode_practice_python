import unittest
from main.LC2528_Maximize_the_Minimum_Powered_City import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_beautifulSubsets(self):
        self.assertEqual(test.maxPower([1, 2, 4, 5, 0], 1, 2), 5)
        self.assertEqual(test.maxPower([4, 4, 4, 4], 0, 3), 4)