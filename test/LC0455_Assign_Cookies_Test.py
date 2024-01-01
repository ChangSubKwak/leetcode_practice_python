import unittest

from main.LC0455_Assign_Cookies import LC0455_Assign_Cookies

test = LC0455_Assign_Cookies()


class LC0242_Valid_Anagram_Test(unittest.TestCase):
    def test_findContentChildren(self):
        self.assertEqual(test.findContentChildren([1, 2, 3], [1, 1]), 1)
        self.assertEqual(test.findContentChildren([1, 2], [1, 2, 3]), 2)


