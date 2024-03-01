import unittest

from main.LC2864_Maximum_Odd_Binary_Number import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_maximumOddBinaryNumber(self):
        self.assertEqual(test.maximumOddBinaryNumber("010"), "001")
