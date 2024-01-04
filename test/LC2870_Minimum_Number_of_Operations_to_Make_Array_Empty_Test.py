import unittest

from main.LC2870_Minimum_Number_of_Operations_to_Make_Array_Empty import LC2870_Minimum_Number_of_Operations_to_Make_Array_Empty

test = LC2870_Minimum_Number_of_Operations_to_Make_Array_Empty()


class LC2870_Minimum_Number_of_Operations_to_Make_Array_Empty_Test(unittest.TestCase):
    def test_minOperations(self):
        self.assertEqual(test.minOperations([2, 3, 3, 2, 2, 4, 2, 3, 4]), 4)
        self.assertEqual(test.minOperations([2, 1, 2, 2, 3, 3]), -1)
