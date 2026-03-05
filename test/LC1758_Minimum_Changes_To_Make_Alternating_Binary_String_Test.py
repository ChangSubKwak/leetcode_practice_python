import unittest

from main.LC1758_Minimum_Changes_To_Make_Alternating_Binary_String import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_minOperations(self):
        self.assertEqual(test.minOperations("0100"), 1)
        self.assertEqual(test.minOperations("10"), 0)
        self.assertEqual(test.minOperations("1111"), 2)
