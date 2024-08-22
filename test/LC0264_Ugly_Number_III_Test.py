import unittest
from main.LC0264_Ugly_Number_II import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_nthUglyNumber(self):
        self.assertEqual(test.nthUglyNumber(10), 12)
        self.assertEqual(test.nthUglyNumber(1), 1)
