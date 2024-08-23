import unittest
from main.LC0592_Fraction_Addition_and_Subtraction import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_fractionAddition(self):
        self.assertEqual(test.fractionAddition("-1/2+1/2"), "0/1")
        self.assertEqual(test.fractionAddition("-1/2+1/2+1/3"), "1/3")
        self.assertEqual(test.fractionAddition("1/3-1/2"), "-1/6")
