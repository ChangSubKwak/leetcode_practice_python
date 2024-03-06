import unittest

from main.LC0948_Bag_of_Tokens import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_bagOfTokensScore(self):
        self.assertEqual(test.bagOfTokensScore([100], 50), 0)
        self.assertEqual(test.bagOfTokensScore([200, 100], 150), 1)
        self.assertEqual(test.bagOfTokensScore([100, 200, 300, 400], 200), 2)
