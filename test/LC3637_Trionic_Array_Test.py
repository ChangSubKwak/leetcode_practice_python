import unittest
from main.LC3637_Trionic_Array import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.isTrionic([1, 3, 5, 4, 2, 6]), True)
        self.assertEqual(test.isTrionic([2, 1, 3]), False)
