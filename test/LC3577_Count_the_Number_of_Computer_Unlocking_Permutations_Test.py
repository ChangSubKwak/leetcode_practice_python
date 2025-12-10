import unittest
from main.LC3577_Count_the_Number_of_Computer_Unlocking_Permutations import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.countPermutations([1, 2, 3]), 2)
        self.assertEqual(test.countPermutations([3, 3, 3, 4, 4, 4]), 0)
