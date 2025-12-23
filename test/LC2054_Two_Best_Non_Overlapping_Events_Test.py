import unittest
from main.LC2054_Two_Best_Non_Overlapping_Events import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.maxTwoEvents([[1, 3, 2], [4, 5, 2], [2, 4, 3]]), 4)
        self.assertEqual(test.maxTwoEvents([[1, 3, 2], [4, 5, 2], [1, 5, 5]]), 5)
        self.assertEqual(test.maxTwoEvents([[1, 5, 3], [1, 5, 1], [6, 6, 5]]), 8)
