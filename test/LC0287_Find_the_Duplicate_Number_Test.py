import unittest

from main.LC0287_Find_the_Duplicate_Number import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_isAnagram(self):
        self.assertEqual(test.findDuplicate([1, 3, 4, 2, 2]), 2)
        self.assertEqual(test.findDuplicate([3, 1, 3, 4, 2]), 3)
        self.assertEqual(test.findDuplicate([3, 3, 3, 3, 3]), 3)


