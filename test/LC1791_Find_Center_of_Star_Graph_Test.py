import unittest
from main.LC1791_Find_Center_of_Star_Graph import Solution

test = Solution()


class TestClass(unittest.TestCase):
    def test_findCenter(self):
        self.assertEqual(test.findCenter([[1, 2], [2, 3], [4, 2]]), 2)
        self.assertEqual(test.findCenter([[1, 2], [5, 1], [1, 3], [1, 4]]), 1)
        