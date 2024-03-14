import unittest

from main.LC2485_Find_the_Pivot_Integer import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_pivotInteger(self):
        self.assertEqual(test.pivotInteger(8), 6)
        self.assertEqual(test.pivotInteger(1), 1)
        self.assertEqual(test.pivotInteger(4), -1)
