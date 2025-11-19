import unittest

from main.LC2154_Keep_Multiplying_Found_Values_by_Two import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_numberOfBeams(self):
        self.assertEqual(test.findFinalValue([5, 3, 6, 1, 12], 3), 24)
        self.assertEqual(test.findFinalValue([2, 7, 9], 4), 4)
