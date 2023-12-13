import unittest

from main.LC1582_Special_Positions_in_a_Binary_Matrix import LC1582_Special_Positions_in_a_Binary_Matrix

test = LC1582_Special_Positions_in_a_Binary_Matrix()


class LC1582_Special_Positions_in_a_Binary_Matrix_test(unittest.TestCase):
    def test1(self):
        self.assertEqual(test.numSpecial([[1, 0, 0], [0, 0, 1], [1, 0, 0]]), 1)
        self.assertEqual(test.numSpecial([[1, 0, 0], [0, 1, 0], [0, 0, 1]]), 3)



