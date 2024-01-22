import unittest

from main.LC0645_Set_Mismatch import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_findErrorNums(self):
        self.assertEqual(test.findErrorNums([1, 2, 2, 4]), [2, 3])
        self.assertEqual(test.findErrorNums([1, 1]), [1, 2])


