import unittest
from main.LC3186_Maximum_Total_Damage_With_Spell_Casting import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.maximumTotalDamage([1, 1, 3, 4]), 6)
        self.assertEqual(test.maximumTotalDamage([7, 1, 6, 6]), 13)
