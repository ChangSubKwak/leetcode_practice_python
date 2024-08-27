import unittest
from main.LC1514_Path_with_Maximum_Probability import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_maxProbability1(self):
        self.assertEqual(test.maxProbability(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.2], 0, 2), 0.25000)

    def test_maxProbability2(self):
        self.assertEqual(test.maxProbability(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.3], 0, 2), 0.30000)

    def test_maxProbability3(self):
        self.assertEqual(test.maxProbability(3, [[0, 1]], [0.5], 0, 2), 0.0000)
