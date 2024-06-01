import unittest
from main.LC3110_Score_of_a_String import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_minOperations(self):
        self.assertEqual(test.scoreOfString("hello"), 13)
        self.assertEqual(test.scoreOfString("zaz"), 50)
