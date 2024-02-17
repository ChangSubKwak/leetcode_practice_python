import unittest

from main.LC1642_Furthest_Building_You_Can_Reach import Solution

test = Solution()


class LC1637_Widest_Vertical_Area_Between_Two_Points_Containing_No_Points_Test(unittest.TestCase):
    def test_maxWidthOfVerticalArea(self):
        self.assertEqual(test.furthestBuilding([4, 2, 7, 6, 9, 14, 12], 5, 1), 4)
        self.assertEqual(test.furthestBuilding([4, 12, 2, 7, 3, 18, 20, 3, 19], 10, 2), 7)
        self.assertEqual(test.furthestBuilding([14, 3, 19, 3], 17, 0), 3)
