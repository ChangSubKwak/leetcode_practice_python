import unittest

from main.LC0242_Valid_Anagram import LC0242_Valid_Anagram

test = LC0242_Valid_Anagram()


class LC0242_Valid_Anagram_Test(unittest.TestCase):
    def test_isAnagram(self):
        self.assertEqual(test.isAnagram("anagram", "nagaram"), True)
        self.assertEqual(test.isAnagram("rat", "car"), False)


