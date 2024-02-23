import unittest

from main.LC0201_Bitwise_AND_of_Numbers_Range import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_isPowerOfTwo(self):
        self.assertEqual(test.rangeBitwiseAnd(5, 7), 4)
        self.assertEqual(test.rangeBitwiseAnd(0, 0), 0)
        self.assertEqual(test.rangeBitwiseAnd(1, 2147483647), 0)
