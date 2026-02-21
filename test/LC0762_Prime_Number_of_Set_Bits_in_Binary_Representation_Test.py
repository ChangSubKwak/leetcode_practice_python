import unittest

from main.LC0762_Prime_Number_of_Set_Bits_in_Binary_Representation import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.countPrimeSetBits(4, 10), 4)
        self.assertEqual(test.countPrimeSetBits(10, 15), 5)
