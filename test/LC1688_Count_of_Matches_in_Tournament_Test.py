import unittest

from main.LC1688_Count_of_Matches_in_Tournament import LC1688_Count_of_Matches_in_Tournament

test = LC1688_Count_of_Matches_in_Tournament()


class LC1688_Count_of_Matches_in_Tournament_Test(unittest.TestCase):
    def test_numberOfMatches(self):
        self.assertEqual(test.numberOfMatches(7), 6)
        self.assertEqual(test.numberOfMatches(14), 13)
