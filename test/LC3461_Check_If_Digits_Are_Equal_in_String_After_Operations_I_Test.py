import unittest
from main.LC3461_Check_If_Digits_Are_Equal_in_String_After_Operations_I import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.hasSameDigits("3902"), True)
        self.assertEqual(test.hasSameDigits("34789"), False)
