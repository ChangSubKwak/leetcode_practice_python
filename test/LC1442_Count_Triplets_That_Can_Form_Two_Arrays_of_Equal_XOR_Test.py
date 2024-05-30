import unittest

from main.LC1442_Count_Triplets_That_Can_Form_Two_Arrays_of_Equal_XOR import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_maxScore(self):
        self.assertEqual(test.countTriplets([2, 3, 1, 6, 7]), 4)
        self.assertEqual(test.countTriplets([1, 1, 1, 1, 1]), 10)
