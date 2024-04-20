import unittest

from main.LC1992_Find_All_Groups_of_Farmland import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_findFarmland1(self):
        self.assertEqual(test.findFarmland([
            [1, 0, 0],
            [0, 1, 1],
            [0, 1, 1]
        ]), [
            [0, 0, 0, 0],
            [1, 1, 2, 2]
        ])

    def test_findFarmland2(self):
        self.assertEqual(test.findFarmland([
            [1, 1], [1, 1]
        ]), [
            [0, 0, 1, 1]
        ])

    def test_findFarmland3(self):
        self.assertEqual(test.findFarmland([
            [0]
        ]), [
        ])

    def test_findFarmland4(self):
        self.assertEqual(test.findFarmland([
            [0], [0], [1], [1], [1], [0], [1], [1]
        ]), [
            [2, 0, 4, 0], [6, 0, 7, 0]
        ])