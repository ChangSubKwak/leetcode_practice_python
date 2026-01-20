import unittest
from main.LC3314_Construct_the_Minimum_Bitwise_Array_I import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.minBitwiseArray([2, 3, 5, 7]),  [-1, 1, 4, 3])
        self.assertEqual(test.minBitwiseArray([11, 13, 31]),  [9, 12, 15])
