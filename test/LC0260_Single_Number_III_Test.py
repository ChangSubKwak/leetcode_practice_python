import unittest
from main.LC0260_Single_Number_III import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_singleNumber(self):
        self.assertEqual(test.singleNumber([1, 2, 1, 3, 2, 5]), [3, 5])
        self.assertEqual(test.singleNumber([-1, 0]), [-1, 0])
        self.assertEqual(test.singleNumber([0, 1]), [0, 1])
