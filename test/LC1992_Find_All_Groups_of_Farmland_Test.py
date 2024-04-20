import unittest

from main.LC1992_Find_All_Groups_of_Farmland import Solution

test = LC1992_Find_All_Groups_of_Farmland()


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
            [1, 1, 1, 1]
        ]), [
            [0, 0, 1, 1]
        ])

    def test_findFarmland3(self):
        self.assertEqual(test.findFarmland([
            [0]
        ]), [
            []
        ])