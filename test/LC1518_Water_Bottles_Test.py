import unittest
from main.LC1518_Water_Bottles import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_maxProbability1(self):
        self.assertEqual(test.numWaterBottles(9, 3), 13)
        self.assertEqual(test.numWaterBottles(15, 4), 19)
