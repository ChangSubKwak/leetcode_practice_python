import unittest

from main.LC0514_Freedom_Trail import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_findBottomLeftValue(self):
        self.assertEqual(test.findRotateSteps("godding", "gd"), 4)
        self.assertEqual(test.findRotateSteps("godding", "godding"), 13)