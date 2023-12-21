import unittest

from main.LC1637_Widest_Vertical_Area_Between_Two_Points_Containing_No_Points import LC1637_Widest_Vertical_Area_Between_Two_Points_Containing_No_Points

test = LC1637_Widest_Vertical_Area_Between_Two_Points_Containing_No_Points()


class LC1637_Widest_Vertical_Area_Between_Two_Points_Containing_No_Points_Test(unittest.TestCase):
    def test_maxWidthOfVerticalArea(self):
        self.assertEqual(test.maxWidthOfVerticalArea([[8, 7], [9, 9], [7, 4], [9, 7]]), 1)
        self.assertEqual(test.maxWidthOfVerticalArea([[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]]), 3)
