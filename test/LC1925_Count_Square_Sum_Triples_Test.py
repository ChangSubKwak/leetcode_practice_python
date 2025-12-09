import unittest

from main.LC1925_Count_Square_Sum_Triples import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.countTriples(5), 2)
        self.assertEqual(test.countTriples(10), 4)
