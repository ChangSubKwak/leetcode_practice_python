import unittest

from main.LC0787_Cheapest_Flights_Within_K_Stops import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_findCheapestPrice(self):
        self.assertEqual(test.findCheapestPrice(4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600]], 0, 3, 1), 700)
        self.assertEqual(test.findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [2, 0, 500]], 0, 2, 0), 500)
        self.assertEqual(test.findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0), 500)
