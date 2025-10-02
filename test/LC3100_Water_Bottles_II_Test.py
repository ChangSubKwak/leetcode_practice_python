import unittest
from main.LC3100_Water_Bottles_II import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_minOperations(self):
        self.assertEqual(test.maxBottlesDrunk(13, 6), 15)
        self.assertEqual(test.maxBottlesDrunk(10, 3), 13)
