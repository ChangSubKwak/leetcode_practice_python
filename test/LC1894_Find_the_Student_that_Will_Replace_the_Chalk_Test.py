import unittest
from main.LC1894_Find_the_Student_that_Will_Replace_the_Chalk import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_chalkReplacer1(self):
        self.assertEqual(test.chalkReplacer([5, 1, 5], 22), 0)

    def test_chalkReplacer2(self):
        self.assertEqual(test.chalkReplacer([3, 4, 1, 2], 25), 1)
