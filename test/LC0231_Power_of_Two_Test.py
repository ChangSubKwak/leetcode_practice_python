import unittest

from main.LC0231_Power_of_Two import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_isPowerOfTwo(self):
        self.assertEqual(test.isPowerOfTwo(1), True)
        self.assertEqual(test.isPowerOfTwo(16), True)
        self.assertEqual(test.isPowerOfTwo(3), False)
