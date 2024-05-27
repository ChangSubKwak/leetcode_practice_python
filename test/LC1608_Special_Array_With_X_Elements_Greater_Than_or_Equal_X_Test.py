import unittest

from main.LC1608_Special_Array_With_X_Elements_Greater_Than_or_Equal_X import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_specialArray(self):
        self.assertEqual(test.specialArray([3, 5]), 2)
        self.assertEqual(test.specialArray([0, 0]), -1)
        self.assertEqual(test.specialArray([0, 4, 3, 0, 4]), 3)
