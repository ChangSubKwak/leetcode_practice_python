import unittest

from main.LC0757_Set_Intersection_Size_At_Least_Two import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_findErrorNums(self):
        self.assertEqual(test.intersectionSizeTwo([[1, 3], [3, 7], [8, 9]]), 5)
        self.assertEqual(test.intersectionSizeTwo([[1, 3], [1, 4], [2, 5], [3, 5]]), 3)
        self.assertEqual(test.intersectionSizeTwo([[1, 2], [2, 3], [2, 4], [4, 5]]), 5)
