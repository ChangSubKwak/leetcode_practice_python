import unittest
from main.LC3607_Power_Grid_Maintenance import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.processQueries(5, [[1, 2], [2, 3], [3, 4], [4, 5]], [[1, 3], [2, 1], [1, 1], [2, 2], [1, 2]]), [3, 2, 3])
        self.assertEqual(test.processQueries(3, [], [[1, 1], [2, 1], [1, 1]]), [1, -1])
