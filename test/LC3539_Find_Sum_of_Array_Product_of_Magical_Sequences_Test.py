import unittest
from main.LC3539_Find_Sum_of_Array_Product_of_Magical_Sequences import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.magicalSum(5, 5, [1, 10, 100, 10000, 1000000]), 991600007)
        self.assertEqual(test.magicalSum(2, 2, [5, 4, 3, 2, 1]), 170)
        self.assertEqual(test.magicalSum(1, 1, [28]), 28)
