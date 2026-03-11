import unittest

from main.LC1009_Complement_of_Base_10_Integer import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.bitwiseComplement(5), 2)
        self.assertEqual(test.bitwiseComplement(7), 0)
        self.assertEqual(test.bitwiseComplement(10), 5)
