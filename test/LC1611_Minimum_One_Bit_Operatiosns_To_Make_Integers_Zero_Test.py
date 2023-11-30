import unittest

from main.LC1611_Minimum_One_Bit_Operations_to_Make_Integers_Zero import LC1611_Minimum_One_Bit_Operations_to_Make_Integers_Zero

test = LC1611_Minimum_One_Bit_Operations_to_Make_Integers_Zero()


class LC1611_Minimum_One_Bit_Operations_to_Make_Integers_Zero_Test(unittest.TestCase):
    def test(self):
        self.assertEqual(test.minimumOneBitOperations(3), 2)
        self.assertEqual(test.minimumOneBitOperations(6), 4)
