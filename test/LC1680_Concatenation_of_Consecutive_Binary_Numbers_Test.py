import unittest

from main.LC1680_Concatenation_of_Consecutive_Binary_Numbers import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.concatenatedBinary(1), 1)
        self.assertEqual(test.concatenatedBinary(3), 27)
        self.assertEqual(test.concatenatedBinary(12), 505379714)
