import unittest

from main.LC0786_Kth_Smallest_Prime_Fracction import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_findCheapestPrice(self):
        self.assertEqual(test.kthSmallestPrimeFraction([1, 2, 3, 5], 3), [2, 5])
        self.assertEqual(test.kthSmallestPrimeFraction([1, 7], 1), [1, 7])
