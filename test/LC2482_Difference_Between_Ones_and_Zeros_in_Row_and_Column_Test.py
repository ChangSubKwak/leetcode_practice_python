import unittest

from main.LC2482_Difference_Between_Ones_and_Zeros_in_Row_and_Column import LC2482_Difference_Between_Ones_and_Zeros_in_Row_and_Column

test = LC2482_Difference_Between_Ones_and_Zeros_in_Row_and_Column()


class LC2482_Difference_Between_Ones_and_Zeros_in_Row_and_Column_Test(unittest.TestCase):
    def test_onesMinusZeros(self):
        self.assertEqual(test.onesMinusZeros([[0, 1, 1], [1, 0, 1], [0, 0, 1]]), [[0, 0, 4],[0, 0, 4], [-2, -2, 2]])
        self.assertEqual(test.onesMinusZeros([[1, 1, 1], [1, 1, 1]]), [[5, 5, 5], [5, 5, 5]])
