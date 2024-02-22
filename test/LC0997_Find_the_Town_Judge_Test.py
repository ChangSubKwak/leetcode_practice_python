import unittest

from main.LC0997_Find_the_Town_Judge import Solution

test = Solution()


class TestClass(unittest.TestCase):
    def test_minFallingPathSum(self):
        self.assertEqual(test.findJudge(2, [[1, 2]]), 2)
        self.assertEqual(test.findJudge(3, [[1, 3], [2, 3]]), 3)
        self.assertEqual(test.findJudge(3, [[1, 3], [2, 3], [3, 1]]), -1)
