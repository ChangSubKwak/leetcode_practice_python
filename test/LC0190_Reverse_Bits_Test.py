import unittest

from main.LC0190_Reverse_Bits import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.reverseBits(43261596), 964176192)
        self.assertEqual(test.reverseBits(2147483644), 1073741822)
