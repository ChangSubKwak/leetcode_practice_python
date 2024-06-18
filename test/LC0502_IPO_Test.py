import unittest
from main.LC0502_IPO import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_findMaximizedCapital(self):
        self.assertEqual(test.findMaximizedCapital(2, 0, [1, 2, 3], [0, 1, 1]), 4)
        self.assertEqual(test.findMaximizedCapital(3, 0, [1, 2, 3], [0, 1, 2]), 6)
