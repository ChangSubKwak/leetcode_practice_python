import unittest

from main.LC0912_Sort_an_Array import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_sortArray(self):
        self.assertEqual(test.sortArray([5, 2, 3, 1]), [1, 2, 3, 5])
        self.assertEqual(test.sortArray([5, 1, 1, 2, 0, 0]), [0, 0, 1, 1, 2, 5])
