import unittest
from main.LC3354_Make_Array_Elements_Equal_to_Zero import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.countValidSelections([1, 0, 2, 0, 3]), 2)
        self.assertEqual(test.countValidSelections([2, 3, 4, 0, 4, 1, 0]), 0)
