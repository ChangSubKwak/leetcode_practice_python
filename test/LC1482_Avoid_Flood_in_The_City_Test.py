import unittest
from main.LC1482_Avoid_Flood_in_The_City import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_minDays(self):
        self.assertEqual(test.avoidFlood([1, 2, 3, 4]), [-1, -1, -1, -1])
        self.assertEqual(test.avoidFlood([1, 2, 0, 0, 2, 1]), [-1, -1, 2, 1, -1, -1])
        self.assertEqual(test.avoidFlood([1, 2, 0, 1, 2]), [])
