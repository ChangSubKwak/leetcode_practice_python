import unittest
from main.LC0350_Intersection_of_Two_Arrays_II import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_intersect(self):
        self.assertEqual(test.intersect([1, 2, 2, 1], [2, 2]), [2, 2])
        self.assertEqual(test.intersect([4, 9, 5], [9, 4, 9, 8, 4]), [4, 9])
