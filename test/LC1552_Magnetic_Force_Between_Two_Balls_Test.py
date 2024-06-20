import unittest
from main.LC1552_Magnetic_Force_Between_Two_Balls import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_makeGood(self):
        self.assertEqual(test.maxDistance([1, 2, 3, 4, 7], 3), 3)
        self.assertEqual(test.maxDistance([5, 4, 3, 2, 1, 10000000000], 2), 999999999)
