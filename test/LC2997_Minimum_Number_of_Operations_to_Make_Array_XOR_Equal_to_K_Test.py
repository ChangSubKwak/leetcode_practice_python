import unittest

from main.LC2997_Minimum_Number_of_Operations_to_Make_Array_XOR_Equal_to_K import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_minOperations(self):
        self.assertEqual(test.minOperations([2, 1, 3, 4], 1), 2)
        self.assertEqual(test.minOperations([2, 0, 2, 0], 0), 0)
