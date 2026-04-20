import unittest

from main.LC2078_Two_Furthest_Houses_With_Different_Colors import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_timeRequiredToBuy(self):
        self.assertEqual(test.maxDistance([1, 1, 1, 6, 1, 1, 1]), 3)
        self.assertEqual(test.maxDistance([1, 8, 3, 8, 3]), 4)
        self.assertEqual(test.maxDistance([0, 1]), 1)

