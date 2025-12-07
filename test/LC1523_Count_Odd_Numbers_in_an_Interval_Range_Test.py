import unittest

from main.LC1523_Count_Odd_Numbers_in_an_Interval_Range import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.countOdds(3, 7), 3)
        self.assertEqual(test.countOdds(8, 10), 1)
