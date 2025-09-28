import unittest

from main.LC0977_Squares_of_a_Sorted_Array import Solution

test = Solution()


class TestClass(unittest.TestCase):
    def test_largestPerimeter(self):
        self.assertEqual(test.largestPerimeter([2, 1, 2]), 5)
        self.assertEqual(test.largestPerimeter([1, 2, 1, 10]), 0)
