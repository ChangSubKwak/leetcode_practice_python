import unittest
from main.LC0451_Sort_Characters_By_Frequency import Solution

test = Solution()

class SolutionTest(unittest.TestCase):
    def test_frequencySort(self):
        self.assertIn(test.frequencySort("tree"), ["eert", "eetr"])
        self.assertIn(test.frequencySort("cccaaa"), ["aaaccc", "cccaaa"])
        self.assertIn(test.frequencySort("Aabb"), ["bbAa", "bbaA"])
