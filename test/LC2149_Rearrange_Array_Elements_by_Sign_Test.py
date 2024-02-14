import unittest

from main.LC2149_Rearrange_Array_Elements_by_Sign import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_numberOfBeams(self):
        self.assertEqual(test.rearrangeArray([3, 1, -2, -5, 2, -4]), [3, -2, 1, -5, 2, -4])
        self.assertEqual(test.rearrangeArray([-1, 1]), [1, -1])

