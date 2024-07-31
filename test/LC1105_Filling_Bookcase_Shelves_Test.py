import unittest
from main.LC1105_Filling_Bookcase_Shelves import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_minHeightShelves(self):
        self.assertEqual(test.minHeightShelves([[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]], 4), 6)
        self.assertEqual(test.minHeightShelves([[1, 3], [2, 4], [3, 2]], 6), 4)
