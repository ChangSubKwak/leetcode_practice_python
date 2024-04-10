import unittest

from main.LC0950_Reveal_Cards_In_Increasing_Order import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_deckRevealedIncreasing(self):
        self.assertEqual(test.deckRevealedIncreasing([17, 13, 11, 2, 3, 5, 7]), [2, 13, 3, 11, 5, 17, 7])
        self.assertEqual(test.deckRevealedIncreasing([1, 1000]), [1, 1000])
