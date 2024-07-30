import unittest

from main.LC1653_Minimum_Deletions_to_Make_String_Balanced import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_minimumDeletions(self):
        self.assertEqual(test.minimumDeletions("aababbab"), 2)
        self.assertEqual(test.minimumDeletions("bbaaaaabb"), 2)
