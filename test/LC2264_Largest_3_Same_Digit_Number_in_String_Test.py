import unittest

from main.LC2264_Largest_3_Same_Digit_Number_in_String import LC2264_Largest_3_Same_Digit_Number_in_String

test = LC2264_Largest_3_Same_Digit_Number_in_String()


class LC2147_Number_of_Ways_to_Divide_a_Long_Corridor_Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(test.largestGoodInteger("6777133339"), "777")
        self.assertEqual(test.largestGoodInteger("2300019"), "000")
        self.assertEqual(test.largestGoodInteger("42352338"), "")
