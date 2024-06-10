import unittest
from main.LC1051_Height_Checker import Solution

test = Solution()


class TestClass(unittest.TestCase):
    def test_heightChecker(self):
        self.assertEqual(test.heightChecker([1, 1, 4, 2, 1, 3]), 3)
        self.assertEqual(test.heightChecker([5, 1, 2, 3, 4]), 5)
        self.assertEqual(test.heightChecker([1, 2, 3, 4, 5]), 0)
