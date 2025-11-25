import unittest

from main.LC1015_Smallest_Integer_Divisible_by_K import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.smallestRepunitDivByK(1), 1)
        self.assertEqual(test.smallestRepunitDivByK(2), -1)
        self.assertEqual(test.smallestRepunitDivByK(3), 3)
