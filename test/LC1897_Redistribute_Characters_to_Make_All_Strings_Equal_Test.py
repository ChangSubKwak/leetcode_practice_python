import unittest

from main.LC1897_Redistribute_Characters_to_Make_All_Strings_Equal import LC1897_Redistribute_Characters_to_Make_All_Strings_Equal

test = LC1897_Redistribute_Characters_to_Make_All_Strings_Equal()


class LC1897_Redistribute_Characters_to_Make_All_Strings_Equal_Test(unittest.TestCase):
    def test_makeEqual(self):
        self.assertEqual(test.makeEqual(["abc", "aabc", "bc"]), True)
        self.assertEqual(test.makeEqual(["ab", "a"]), False)
