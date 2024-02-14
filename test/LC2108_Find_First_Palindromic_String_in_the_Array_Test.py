import unittest

from main.LC2108_find_First_Palindromic_String_in_the_Array import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_numberOfBeams(self):
        self.assertEqual(test.firstPalindrome(["abc", "car", "ada", "racecar", "cool"]), "ada")
        self.assertEqual(test.firstPalindrome(["notapalindrome", "racecar"]), "racecar")
        self.assertEqual(test.firstPalindrome(["def", "ghi"]), "")

