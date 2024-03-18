import unittest
from main.LC0057_Insert_Interval import Solution


class SolutionTest(unittest.TestCase):
    def test_insert(self):
        self.assertEqual(Solution.insert([[1, 3], [6, 9]], [2, 5]), [[1, 5], [6, 9]])
        self.assertEqual(Solution.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]), [[1, 2], [3, 10], [12, 16]])
