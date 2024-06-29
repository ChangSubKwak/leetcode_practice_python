import unittest
from main.LC2285_Maximum_Total_Importance_of_Roads import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_maximumImportance(self):
        self.assertEqual(test.maximumImportance([[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]]), 43)
        self.assertEqual(test.maximumImportance([[0, 3], [2, 4], [1, 3]]), 20)
