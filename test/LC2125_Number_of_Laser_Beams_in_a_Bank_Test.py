import unittest

from main.LC2125_Number_of_Laser_Beams_in_a_Bank import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_numberOfBeams(self):
        self.assertEqual(test.numberOfBeams(["011001", "000000", "010100", "001000"]), 8)
        self.assertEqual(test.numberOfBeams(["000", "111", "000"]), 0)
