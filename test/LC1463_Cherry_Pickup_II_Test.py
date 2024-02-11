import unittest

from main.LC1463_Cherry_Pickup_II import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_cherryPickup(self):
        self.assertEqual(test.cherryPickup([
            [3, 1, 1],
            [2, 5, 1],
            [1, 5, 5],
            [2, 1, 1]
        ]), 24)
        self.assertEqual(test.cherryPickup([
            [1, 0, 0, 0, 0, 0, 1],
            [2, 0, 0, 0, 0, 3, 0],
            [2, 0, 9, 0, 0, 0, 0],
            [0, 3, 0, 5, 4, 0, 0],
            [1, 0, 2, 3, 0, 0, 6],
        ]), 28)
