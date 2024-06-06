import unittest
from main.LC0846_Hand_of_Straights import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_sumOfDistancesInTree(self):
        self.assertEqual(test.isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3), True)
        self.assertEqual(test.isNStraightHand([1, 2, 3, 4, 5], 4), False)
