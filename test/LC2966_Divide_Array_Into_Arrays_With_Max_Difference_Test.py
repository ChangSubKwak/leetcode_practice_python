import unittest

from main.LC2966_Divide_Array_Into_Arrays_With_Max_Difference import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_minOperations(self):
        self.assertEqual(test.divideArray([1, 3, 4, 8, 7, 9, 3, 5, 1], 2), [[1, 1, 3], [3, 4, 5], [7, 8, 9]])
        self.assertEqual(test.divideArray([1, 3, 3, 2, 7, 3], 3), [])
