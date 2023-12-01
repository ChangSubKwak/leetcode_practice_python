import unittest

from main.LC1662_Check_If_Two_String_Arrays_are_Equivalent import LC1662_Check_If_Two_String_Arrays_are_Equivalent

test = LC1662_Check_If_Two_String_Arrays_are_Equivalent()


class LC1662_Check_If_Two_String_Arrays_are_Equivalent_Test(unittest.TestCase):
    def test(self):
        self.assertEqual(test.arrayStringsAreEqual(["ab", "c"], ["a", "bc"]), True)
        self.assertEqual(test.arrayStringsAreEqual(["a", "cb"], ["ab", "c"]), False)
        self.assertEqual(test.arrayStringsAreEqual(["abc", "d", "defg"], ["abcddefg"]), True)
