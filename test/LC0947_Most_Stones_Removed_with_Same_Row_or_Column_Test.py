import unittest
from main.LC0947_Most_Stones_Removed_with_Same_Row_or_Column import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_removeStones1(self):
        self.assertEqual(test.removeStones([[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]), 5)

    def test_removeStones2(self):
        self.assertEqual(test.removeStones([[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]), 3)

    def test_removeStones3(self):
        self.assertEqual(test.removeStones([[0, 0]]), 0)
