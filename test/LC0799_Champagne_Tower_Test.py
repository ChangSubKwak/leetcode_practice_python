import unittest

from main.LC0799_Champagne_Tower import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_customSortString(self):
        self.assertEqual(test.champagneTower(1, 1, 1), 0.00000)
        self.assertEqual(test.champagneTower(2, 1, 1), 0.50000)
        self.assertEqual(test.champagneTower(100000009, 33, 17), 1.00000)

