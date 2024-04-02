import unittest

from main.LC0205_Isomorphic_Strings import Solution


class SolutionTest(unittest.TestCase):
    def test_isIsomorphic(self):
        self.assertEqual(Solution.isIsomorphic("egg", "add"), True)
        self.assertEqual(Solution.isIsomorphic("foo", "bar"), False)
        self.assertEqual(Solution.isIsomorphic("paper", "title"), True)