import unittest

from main.LC0268_Missing_Number import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_isAnagram(self):
        self.assertEqual(test.missingNumber([3, 0, 1]), 2)
        self.assertEqual(test.missingNumber([0, 1]), 2)
        self.assertEqual(test.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]), 8)


