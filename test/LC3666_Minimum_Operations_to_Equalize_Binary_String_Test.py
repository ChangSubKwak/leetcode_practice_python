import unittest
from main.LC3666_Minimum_Operations_to_Equalize_Binary_String import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.minOperations("110", 1), 1)
        self.assertEqual(test.minOperations("0101", 3), 2)
        self.assertEqual(test.minOperations("101", 2), 2)
