import unittest

from main.LC1637_Widest_Vertical_Area_Between_Two_Points_Containing_No_Points import LC1637_Widest_Vertical_Area_Between_Two_Points_Containing_No_Points

test = LC1636_Sort_Array_by_Increasing_Frequency()


class SolutionTest(unittest.TestCase):
    def test_maxWidthOfVerticalArea(self):
        self.assertEqual(test.frequencySort([1, 1, 2, 2, 2, 3]), [3, 1, 1, 2, 2, 2])
