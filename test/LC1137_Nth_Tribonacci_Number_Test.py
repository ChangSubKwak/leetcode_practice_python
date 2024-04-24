import unittest

from main.LC1137_Nth_Tribonacci_Number import Solution


class SolutionTest(unittest.TestCase):

    def test_tribonacci(self):
        test = Solution()
        self.assertEqual(test.tribonacci(4), 4)
        self.assertEqual(test.tribonacci(25), 1389537)
