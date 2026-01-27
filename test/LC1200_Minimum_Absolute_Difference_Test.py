import unittest

from main.LC1200_Minimum_Absolute_Difference import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_uniqueOccurrences(self):
        self.assertEqual(test.minimumAbsDifference([4, 2, 1, 3]), [[1, 2], [2, 3], [3, 4]])
        self.assertEqual(test.minimumAbsDifference([1, 3, 6, 10, 15]), [[1, 3]])
        self.assertEqual(test.minimumAbsDifference([3, 8, -10, 23, 19, -4, -14, 27]), [[-14, -10], [19, 23], [23, 27]])
