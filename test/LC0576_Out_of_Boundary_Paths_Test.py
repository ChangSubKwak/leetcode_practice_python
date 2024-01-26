import unittest

from main.LC0576_Out_of_Boundary_Paths import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_findContentChildren(self):
        self.assertEqual(test.findPaths(2, 2, 2, 0, 0), 6)
        self.assertEqual(test.findPaths(1, 3, 3, 0, 1), 12)
