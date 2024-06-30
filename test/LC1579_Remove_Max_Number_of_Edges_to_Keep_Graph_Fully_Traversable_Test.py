import unittest
from main.LC1579_Remove_Max_Number_of_Edges_to_Keep_Graph_Fully_Traversable import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_makeGood(self):
        self.assertEqual(test.maxNumEdgesToRemove(4, [[3, 1, 2], [3, 2, 3], [1, 1, 3], [1, 2, 4], [1, 1, 2], [2, 3, 4]]), 2)
        self.assertEqual(test.maxNumEdgesToRemove(4, [[3, 1, 2], [3, 2, 3], [1, 1, 4], [2, 1, 4]]), 0)
        self.assertEqual(test.maxNumEdgesToRemove(4, [[3, 2, 3], [1, 1, 2], [2, 3, 4]]), -1)
