import unittest

from main.LC0075_Sort_Colors import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_sortColors1(self):
        nums = [2, 0, 2, 1, 1, 0]
        test.sortColors(nums)
        self.assertEqual(nums, [0, 0, 1, 1, 2, 2])

    def test_sortColors2(self):
        nums = [2, 0, 1]
        test.sortColors(nums)
        self.assertEqual(nums, [0, 1, 2])
