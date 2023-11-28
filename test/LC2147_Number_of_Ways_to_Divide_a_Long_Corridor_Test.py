import unittest

from main.LC2147_Number_of_Ways_to_Divide_a_Long_Corridor import LC2147_Number_of_Ways_to_Divide_a_Long_Corridor

test = LC2147_Number_of_Ways_to_Divide_a_Long_Corridor()


class LC2147_Number_of_Ways_to_Divide_a_Long_Corridor_Test(unittest.TestCase):
    def numberOfWays(self):
        self.assertEqual(test.numberOfWays("SSPPSPS"), 3)
        self.assertEqual(test.numberOfWays("PPSPSP"), 1)
        self.assertEqual(test.numberOfWays("S"), 0)
