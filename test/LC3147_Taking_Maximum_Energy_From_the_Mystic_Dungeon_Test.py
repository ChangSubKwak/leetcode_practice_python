import unittest
from main.LC3147_Taking_Maximum_Energy_From_the_Mystic_Dungeon import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.maximumEnergy([5, 2, -10, -5, 1], 3), 3)
        self.assertEqual(test.maximumEnergy([5, 2, -10, -5, 1], 3), 3)
