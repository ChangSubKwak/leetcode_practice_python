import unittest

from main.LC2092_Find_All_People_With_Secret import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_sortJumbled(self):
        self.assertEqual(test.findAllPeople(6, [[1, 2, 5], [2, 3, 8], [1, 5, 10]], 1), [0, 1, 2, 3, 5])
        self.assertEqual(test.findAllPeople(4, [[3, 1, 3], [1, 2, 2], [0, 3, 3]], 3), [0, 1, 3])
        self.assertEqual(test.findAllPeople(5, [[3, 4, 2], [1, 2, 1], [2, 3, 1]], 1), [0, 1, 2, 3, 4])
