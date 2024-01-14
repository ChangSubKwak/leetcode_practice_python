import unittest

from main.LC1657_Determine_if_Two_Strings_Are_Close import Solution

test = Solution()


class LC1637_Widest_Vertical_Area_Between_Two_Points_Containing_No_Points_Test(unittest.TestCase):
    def test_maxWidthOfVerticalArea(self):
        self.assertEqual(test.closeStrings("abc", "bca"), True)
        self.assertEqual(test.closeStrings("a", "aa"), False)
        self.assertEqual(test.closeStrings("cabbba", "abbccc"), True)
