import unittest
from main.LC1334_Find_the_City_With_the_Smallest_Number_of_Neighbors_at_a_Threshold_Distance import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_findTheCity(self):
        self.assertEqual(test.findTheCity(4, [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], 4), 3)
        self.assertEqual(test.findTheCity(4, [[0, 1, 3], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]], 2), 0)
