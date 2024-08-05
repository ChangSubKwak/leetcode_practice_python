import unittest
from main.LC2053_Kth_Distinct_String_in_an_Array import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_kthDistinct(self):
        self.assertEqual(test.kthDistinct(["d", "b", "c", "b", "c", "a"], 2), "a")
        self.assertEqual(test.kthDistinct(["aaa", "aa", "a"], 1), "aaa")
        self.assertEqual(test.kthDistinct(["a", "b", "a"], 3), "")
