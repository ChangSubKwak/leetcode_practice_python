import unittest

from main.LC0756_Pyramid_Transition_Matrix import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_findErrorNums(self):
        self.assertEqual(test.pyramidTransition("BCD", ["BCC", "CDE", "CEA", "FFF"]), True)
        self.assertEqual(test.pyramidTransition("AAAA", ["AAB", "AAC", "BCD", "BBE", "DEF"]), False)
