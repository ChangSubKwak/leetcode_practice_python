import unittest
from main.LC2037_Minimum_Number_of_Moves_to_Seat_Everyone import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_timeRequiredToBuy(self):
        self.assertEqual(test.minMovesToSeat([3, 1, 5], [2, 7, 4]), 4)
        self.assertEqual(test.minMovesToSeat([4, 1, 5, 9], [1, 3, 2, 6]), 7)
        self.assertEqual(test.minMovesToSeat([2, 2, 6, 6], [1, 3, 2, 6]), 4)
