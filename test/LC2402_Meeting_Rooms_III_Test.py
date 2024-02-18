import unittest

from main.LC2402_Meeting_Rooms import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_onesMinusZeros(self):
        self.assertEqual(test.mostBooked(2, [[0, 10], [1, 5], [2, 7], [3, 4]]), 0)
        self.assertEqual(test.mostBooked(3, [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]), 1)
