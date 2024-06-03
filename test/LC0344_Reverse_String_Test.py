import unittest
from main.LC0344_Reverse_String import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_reverseString1(self):
        input_string = ["h", "e", "l", "l", "o"]
        test.reverseString(input_string)
        expected = ["o", "l", "l", "e", "h"]
        self.assertEqual(input_string, expected)

    def test_reverseString2(self):
        input_string = ["H", "a", "n", "n", "a", "h"]
        test.reverseString(input_string)
        expected = ["h", "a", "n", "n", "a", "H"]
        self.assertEqual(input_string, expected)
