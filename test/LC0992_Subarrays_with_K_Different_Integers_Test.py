import unittest

from main.LC0992_Subarrays_with_K_Different_Integers import Solution

test = Solution()


class TestClass(unittest.TestCase):
    def test_minFallingPathSum(self):
        self.assertEqual(test.subarraysWithKDistinct([1, 2, 1, 2, 3], 2), 7)
        self.assertEqual(test.subarraysWithKDistinct([1, 2, 1, 3, 4], 3), 3)
