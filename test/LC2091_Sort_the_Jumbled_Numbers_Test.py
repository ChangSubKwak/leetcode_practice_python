import unittest

from main.LC2091_Sort_the_Jumbled_Numbers import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_sortJumbled(self):
        self.assertEqual(test.sortJumbled([8, 9, 4, 0, 2, 1, 3, 5, 7, 6], [991,338,38]), [338, 38, 991])
        self.assertEqual(test.sortJumbled([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [789,456,123]), [123, 456, 789])

