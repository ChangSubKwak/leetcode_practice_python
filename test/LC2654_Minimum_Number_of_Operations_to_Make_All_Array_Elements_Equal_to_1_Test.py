import unittest
from main.LC2654_Minimum_Number_of_Operations_to_Make_All_Array_Elements_Equal_to_1 import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_countSeniors(self):
        self.assertEqual(test.minOperations([2, 6, 3, 4]), 4)
        self.assertEqual(test.minOperations([2, 10, 6, 14]), -1)
