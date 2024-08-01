import unittest
from main.LC2678_Number_of_Senior_Citizens import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_countSeniors(self):
        self.assertEqual(test.countSeniors(["7868190130M7522", "5303914400F9211", "9273338290F4010"]), 2)
        self.assertEqual(test.countSeniors(["1313579440F2036", "2921522980M5644"]), 0)
