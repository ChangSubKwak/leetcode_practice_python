import unittest

from main.LC0881_Boats_Save_People import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_numRescueBoats(self):
        self.assertEqual(test.middleNode([1, 2], 3), 1)
        self.assertEqual(test.middleNode([3, 2, 2, 1], 3), 3)
        self.assertEqual(test.middleNode([3, 5, 3, 4], 5), 4)
