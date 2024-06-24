import unittest
from main.LC0995_Minimum_Number_of_K_Consecutive_Bit_Flips import Solution

test = Solution()


class TestClass(unittest.TestCase):
    def test_minKBitFlips(self):
        self.assertEqual(test.minKBitFlips([0, 1, 0], 1), 2)
        self.assertEqual(test.minKBitFlips([1, 1, 0], 2), -1)
        self.assertEqual(test.minKBitFlips([0, 0, 0, 1, 0, 1, 1, 0], 3), 3)
