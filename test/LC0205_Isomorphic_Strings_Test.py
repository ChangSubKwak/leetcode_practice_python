import unittest

from main.LC0205_Isomorphic_Strings import Solution


test = Solution()

class SolutionTest(unittest.TestCase):
    def test_isIsomorphic(self):
        self.assertEqual(test.isIsomorphic("egg", "add"), True)
        self.assertEqual(test.isIsomorphic("foo", "bar"), False)
        self.assertEqual(test.isIsomorphic("paper", "title"), True)