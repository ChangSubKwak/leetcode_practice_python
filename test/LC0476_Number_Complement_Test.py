import unittest

from main.LC0476_Number_Complement import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_findContentChildren(self):
        self.assertEqual(test.findComplement(5), 2)
        self.assertEqual(test.findComplement(1), 0)


